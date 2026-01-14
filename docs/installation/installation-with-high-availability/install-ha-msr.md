# Install highly available MSR

1. Generate a configuration values file for the chart:

    ```bash
    helm show values oci://registry.mirantis.com/harbor/helm/msr --version <MSR-VERSION> > msr-values.yaml
    ```
    !!! note
 
        To ensure you are using the latest MSR version, review the [release notes](../../release-notes/index.md).
        If you need to verify the MSR version directly from the registry, run
        the following command to retrieve available tags:
 
         ```bash
         $ curl -s -H "Authorization: Bearer $(
           curl -s "$(
             curl -sI https://registry.mirantis.com/v2/harbor/helm/msr/tags/list?n=1 \
               | tr -d '\r' \
               | sed -n 's/.*realm="\([^"]*\)".*service="\([^"]*\)".*/\1?service=\2\&scope=repository:harbor\/helm\/msr:pull/p'
           )" | sed -n 's/.*"token":"\([^"]*\)".*/\1/p'
         )" https://registry.mirantis.com/v2/harbor/helm/msr/tags/list?n=1000 \
         | sed -n 's/.*"tags":\[\(.*\)\].*/\1/p' | tr -d '"' | tr ',' '\n' | grep -v -- -
         ```

2. Helm automatically creates certificates. To manually create your own,  
   follow these steps: 

    1. Create a directory for certificates named `certs`:

        ```bash
        mkdir certs
        ```

    2. Create a `certs.conf` text file in the `certs` directory:

        ```bash
        [req]
        distinguished_name = req_distinguished_name
        x509_extensions = v3_req
        prompt = no

        [req_distinguished_name]
        C = US
        ST = State
        L = City
        O = Organization
        OU = Organizational Unit
        CN = msr

        [v3_req]
        keyUsage = digitalSignature, keyEncipherment, dataEncipherment
        extendedKeyUsage = serverAuth
        subjectAltName = @alt_names

        [alt_names]
        IP.1 = <IP-ADDRESS-OF-WORKERNODE>  # Replace with your actual IP address
        ```

    3. Generate the certificate and the key using the `certs.conf` file  
       you just created:

        ```bash
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
            -keyout tls.key -out tls.crt -config certs.conf
        ```

3. If you are using the Helm certificates skip this step. If you manually  
   created your own certificates, create the Kubernetes secret. Run the  
   following command from outside of the `certs` folder:

    ```bash
    kubectl create secret tls <NAME-OF-YOUR-SECRET> \
        --cert=certs/tls.crt \
        --key=certs/tls.key
    ```

4. Modify the `msr-values.yaml` file to configure MSR:

    - Set the expose type:

        ```yaml
        expose:
            # Set how to expose the service. Set the type as "ingress",
            # "clusterIP", "nodePort" or "loadBalancer" and fill the
            # information in the corresponding section
            type: nodePort
        ```

    - Set the cert source to TLS and the secret name:

        ```yaml
        certSource: secret
        secret:
            # The name of secret which contains keys named:
            # "tls.crt" - the certificate
            # "tls.key" - the private key
            secretName: "<NAME-OF-YOUR-SECRET>"
        ```

    - Set the `nodePort` ports to allow `nodePort ingress`. You can use any  
      ephemeral port. Some Kubernetes distributions restrict the range.  
      The range ``32768–35535`` is generally accepted.

        ```yaml
        nodePort:
            # The name of NodePort service
            name: harbor
            ports:
                http:
                    # The service port Harbor listens on when serving HTTP
                    port: 80
                    # The node port Harbor listens on when serving HTTP
                    nodePort: <httpNodePort>
                https:
                    # The service port Harbor listens on when serving HTTPS
                    port: 443
                    # The node port Harbor listens on when serving HTTPS
                    nodePort: <httpNodePort>
        ```

    - Set the external URL, if using nodePort use a worker node IP address  
      (the same one that you used in generating the cert):

        ```yaml
        externalURL: https://<A-WORKER-NODE-EXTERNAL-IP:httpsnodePort>
        ```

    - Enable data persistence:

        ```yaml
        persistence:
            enabled: true
        ```

        If you are using a named StorageClass (as opposed to the default  
        StorageClass) you need to specify it as shown in the following sample:

        ```yaml
        persistence:
            enabled: true
            resourcePolicy: "keep"
            persistentVolumeClaim:
                registry:
                    existingClaim: ""
                    storageClass: "<STORAGE-CLASS-NAME>"
                    subPath: ""
                    accessMode: ReadWriteMany
                    size: 5Gi
                    annotations: {}
        ```

    - Set the initial admin password:

        ```yaml
        harborAdminPassword: "Harbor12345"
        ```

        !!! note
            After you launch MSR 4, change the admin password from the  
            MSR web UI, or provide an existing secret using the  
            `existingSecretAdminPasswordKey` parameter.

    - Set the replica number to at least 2 under `portal`, `registry`,  
      `core`, `trivy`, and `jobservice`:

        ```yaml
        jobservice:
            image:
                repository: harbor-jobservice
            replicas: 2
        ```

    - Set PostgreSQL as an external database:

        ```yaml
        database:
            # if external database is used, set "type" to "external"
            # and fill the connection information in "external" section
            type: external
        ```

    - Update external database section to reflect PostgreSQL configuration:

        ```yaml
        external:
            sslmode: require
            host: <POSTGRES-SERVICE-IP-ADDRESS>
            port: <POSTGRES-SERVICE-PORT-NUMBER>
            coreDatabase: registry
            username: msr
            existingSecret: msr.msr-postgres.credentials.postgresql.acid.zalan.do
        ```

    - Set Redis as an external database:

        ```yaml
        redis:
            # if external Redis is used, set "type" to "external"
            # and fill the connection information in "external" section
            type: external
        ```

    - Update the external Redis configuration:

        ```yaml
        external:
            addr: msr-redis-master:<REDIS-PORT-NUMBER>
            existingSecret: msr-redis-secret
        ```

    - Check your settings against a full example of MSR configuration:

        ```yaml
        expose:
            type: loadBalancer
        persistence:
            enabled: true
            resourcePolicy: "keep"
            persistentVolumeClaim:
                registry:
                    storageClass: "<STORAGE-CLASS-NAME>"
                    accessMode: ReadWriteMany
                    size: 5Gi
                jobservice:
                    jobLog:
                        storageClass: "<STORAGE-CLASS-NAME>"
                        accessMode: ReadWriteMany
                        size: 5Gi
                trivy:
                    storageClass: "<STORAGE-CLASS-NAME>"
                    accessMode: ReadWriteMany
                    size: 5Gi
        portal:
            replicas: 2
        core:
            replicas: 2
        jobservice:
            replicas: 2
        registry:
            replicas: 2
        trivy:
            replicas: 2
        database:
            type: external
            external:
                sslmode: require
                host: "<POSTGRES-SERVICE-IP-ADDRESS>"
                port: "<POSTGRES-SERVICE-PORT-NUMBER>"
                coreDatabase: registry
                username: msr
                existingSecret: msr.msr-postgres.credentials.postgresql.acid.zalan.do
        redis:
            type: external
            external:
                addr: "msr-redis-master:<REDIS-PORT-NUMBER>"
                existingSecret: msr-redis-secret
        ```

5. Install MSR using Helm:

    ```bash
    helm install my-release oci://registry.mirantis.com/harbor/helm/msr \
        --version <MSR-VERSION> -f <PATH-TO/msr-values.yaml>
    ```

6. Configure Docker to trust the self-signed certificate.  
   On the system logged into MSR:

    1. Create a directory:

        ```bash
        /etc/docker/certs.d/<IPADDRESS:NODEPORT>
        ```

    2. Move and rename the certificate:

        ```bash
        mv tls.crt /etc/docker/certs.d/<IPADDRESS:NODEPORT>/ca.crt
        ```

    3. Access the MSR web UI at  
       `https://<WORKER-NODE-EXTERNAL-IP>:<httpsNodePort>`  
       provided the same NodePort numbers were used as specified in this  
       guide. You can also log in using:

        ```bash
        docker login <WORKER-NODE-EXTERNAL-IP>:<httpsNodePort>
        ```

    !!! warning
        By default, robot account names start with the `$` character, which  
        some software may interpret as a variable. As such, you should change  
        the default prefix to avoid any potential issues:

        1. Log in to the MSR 4 web UI with an account that has administrator  
           privileges.
        2. Navigate to **Configuration** and select **System Settings**.
        3. In the **Robot Name Prefix** row, modify the prefix.
