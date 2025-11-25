# Install highly available PostgreSQL

1. Install the Zalando Postgres Operator:

    ```bash
    helm install postgres-operator postgres-operator --repo https://opensource.zalando.com/postgres-operator/charts/postgres-operator --set configGeneral.docker_image=registry.mirantis.com/msr/spilo:17-4.0-p3-20251117010013
    ```
   !!! note

       Alternatively, you can configure the deployment to use the default image
       provided in the upstream Zalando Postgres Operator community release:

       ```bash

       helm install postgres-operator postgres-operator --repo https://opensource.zalando.com/postgres-operator/charts/postgres-operator
       ```

2. Create and configure the `msr-postgres-manifest.yaml` file:

    !!! warning "OpenShift deployments only"

        While the default PostgreSQL Operator settings allow the operator
        to run in a general Kubernetes environment, they are not sufficient
        for OpenShift. To ensure proper functionality, enable the
        `kubernetes_use_configmaps` parameter. For details, refer to the
        [Zalando Postgres Operator quickstart guide](https://github.com/zalando/postgres-operator/blob/master/docs/quickstart.md#manual-deployment-setup-on-openshift).

    !!! note

        Adjust `numberOfInstances` to match your desired cluster size.

    ```yaml
    apiVersion: "acid.zalan.do/v1"
    kind: postgresql
    metadata:
      name: msr-postgres
    spec:
      teamId: "msr"
      volume:
        size: 1Gi
      numberOfInstances: 3
      users:
        msr:  # database owner
        - superuser
        - createdb
      databases:
        registry: msr  # dbname: owner
      postgresql:
        version: "17"
    ```

    If you are running RHEL 9.4 or later, exclude the `bg_mon` module from
    the PostgreSQL configuration as shown below. Refer to the
    `known-issues-4.13.2` for more details.

    ```yaml
    apiVersion: "acid.zalan.do/v1"
    kind: postgresql
    metadata:
      name: msr-postgres
    spec:
      teamId: "msr"
      volume:
        size: 1Gi
      numberOfInstances: 3
      users:
        msr:  # database owner
        - superuser
        - createdb
      databases:
        registry: msr  # dbname: owner
      postgresql:
        version: "17"
        parameters:
          shared_preload_libraries: "pg_stat_statements,pgextwlist,pg_auth_mon,set_user,timescaledb,pg_cron,pg_stat_kcache"
    ```

3. Deploy the Postgres instance:

    ```bash
    kubectl create -f msr-postgres-manifest.yaml
    ```

4. Retrieve connection details for the Postgres service:

    **Get the service's IP address:**

    ```bash
    kubectl get svc \
        -l application=spilo,cluster-name=msr-postgres,spilo-role=master \
        -o jsonpath={.items..spec.clusterIP}
    ```

    **Get the service's port number:**

    ```bash
    kubectl get svc \
        -l application=spilo,cluster-name=msr-postgres,spilo-role=master \
        -o jsonpath={.items..spec.ports..port}
    ```

## Upgrade highly available PostgreSQL

1. Verify the Zalando Postgres Operator image:

   ```bash

   kubectl get operatorconfiguration.acid.zalan.do -o=jsonpath='{.items[0].configuration.docker_image}'
   ```

2. Perform the upgrade:

   ```bash

   helm upgrade postgres-operator postgres-operator --repo https://opensource.zalando.com/postgres-operator/charts/postgres-operator --set configGeneral.docker_image=registry.mirantis.com/msr/spilo:17-4.0-p3-20251117010013
   ```

