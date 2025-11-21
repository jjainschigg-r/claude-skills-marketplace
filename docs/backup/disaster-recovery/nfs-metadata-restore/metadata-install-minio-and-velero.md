# Install MinIO and Velero

Install MinIO and Velero on the Kubernetes cluster on which you are running
MSR 4.

1. Deploy MinIO Operator in its own namespace:

    ```bash
    helm repo add minio-operator https://operator.min.io
    helm repo up
    helm install   --namespace minio-operator   --create-namespace   operator minio-operator/operator
    ```

2. Set up MinIO Tenant.

    * Download the MinIO Tenant `values.yml` file:

        ```bash
        curl -sLo values.yaml https://raw.githubusercontent.com/minio/operator/master/helm/tenant/values.yaml
        ```

    * Configure a username and password for Minio:

        ```yaml
        [...]
          configSecret:
            name: myminio-env-configuration
            accessKey: <username>
            secretKey: <password>
        [...]
        ```

    * Configure the pools:

        ```yaml
        [...]
          pools:
            ###
            # The number of MinIO Tenant Pods / Servers in this pool.
            # For standalone mode, supply 1. For distributed mode, supply 4 or
            # more.
            # Note that the operator does not support upgrading from
            # standalone to distributed mode.
            - servers: 1
              ###
              # Custom name for the pool
              name: pool-0
              ###
              # The number of volumes attached per MinIO Tenant Pod / Server.
              volumesPerServer: 4
              ###
              # The capacity per volume requested per MinIO Tenant Pod.
              size: 30Gi
        [...]
        ```

    !!! note
        Use NodeSelector to run MinIO Tenant on a specific node on which the
        public IP or DNS will be used to connect to Minio's console.

3. Install MinIO Tenant in its own namespace:

    ```bash
    helm install --namespace minio-tenant --create-namespace --values values.yml minio-tenant minio-operator/tenant
    ```

4. Expose the MinIO API and console using NodePort:

    1. Create the Kubernetes Services' YAML files:

        * `minio-api-svc.yml`

            ```yaml
            $ cat minio-api-svc.yml
            apiVersion: v1
            kind: Service
            metadata:
              name: minio-nodeport
              namespace: minio-tenant
            spec:
              type: NodePort
              selector:
                v1.min.io/tenant: myminio
              ports:
                - name: https-minio
                  port: 9000
                  targetPort: 9000
                  nodePort: 33000
            ```

        * `minio-console-svc.yml`

            ```yaml
            $ cat minio-console-svc.yml
            apiVersion: v1
            kind: Service
            metadata:
              name: minio-console-nodeport
              namespace: minio-tenant
            spec:
              type: NodePort
              selector:
                v1.min.io/tenant: myminio
              ports:
                - name: https-console
                  port: 9443
                  targetPort: 9443
                  nodePort: 33001
            ```

    2. Deploy the Kubernetes Services:

        ```bash
        kubectl apply -f minio-console-svc.yml
        kubectl apply -f minio-api-svc.yml
        ```

    !!! note
        Alternatively, MinIO Tenant can use LoadBalancer and Ingress, refer
        to MinIO official documentation for more details:

        * `Kubernetes <https://docs.min.io/enterprise/aistor-object-store/installation/kubernetes/>`__
        * `Deploy AIStor on Kubernetes <https://docs.min.io/enterprise/aistor-object-store/installation/kubernetes/install/deploy-aistor-on-kubernetes/#deploy-tenant-helm>`__

5. Login to MinIO console:

    ```text
    https://MINIO_CONSOLE_URL:CONSOLE_nodePort
    ```

6. Create a bucket for backup and restore data.

7. Install the Velero CLI on both the source (primary) and target (recovery)
   Kubernetes clusters using the instructions from `the official Velero
   documentation <https://velero.io/docs/v1.8/basic-install/>`__.

8. Install Velero on both the source (primary) and target (recovery)
   Kubernetes cluster:

    1. Create the `credentials-velero` file:

        ```bash
        cat credentials-velero
        [default]
        aws_access_key_id=<access key from mino-tenant>
        aws_secret_access_key=<secret access key from mino-tenant>
        ```

    2. Install Velero:

        1. For the snapshot backup:

            ```bash
            velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.13.0 --bucket msr4-backup --secret-file ./credentials-velero --backup-location-config s3Url=https://<minio-tenant API URL>:<minio-tenant API Port>,s3ForcePathStyle=true,insecureSkipTLSVerify=true --use-volume-snapshots=true --use-node-agent --features=EnableCSI --snapshot-location-config region=default
            ```

        2. For the file system backup:

            ```bash
            velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.13.0 --bucket <Minio bucket name> --secret-file ./credentials-velero --backup-location-config s3Url=https://<minio-tenant API URL>:<minio-tenant API Port>,s3ForcePathStyle=true,insecureSkipTLSVerify=true --use-volume-snapshots=false --use-node-agent
            ```

            !!! note
                Both the source and target clusters must have Velero
                configured to point to the same MinIO Tenant URL and Backup
                Storage Location (BSL) bucket.

    3. Verify backup location on both the source (primary) and target
       (recovery) Kubernetes cluster:

        * For the snapshot backup:

            ```bash
            kubectl -n velero describe VolumeSnapshotLocation
            ```

        * For the file system backup:

            ```bash
            kubectl -n velero describe backupstoragelocations
            ```
