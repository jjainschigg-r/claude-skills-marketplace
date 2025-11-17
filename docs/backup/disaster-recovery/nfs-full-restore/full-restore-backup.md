# Backup and Restore

!!! warning

    The examples herein are illustrative. Always review and adjust all
    deployment details to align with your actual MSR 4 instance before you
    execute any commands.

1. Set MSR 4 to **Repository Read-Only** mode.

    Before you initiate the backup, set MSR 4 to **Repository Read-Only** mode
    to prevent new data from being written during the process, minimizing
    inconsistencies.

    1. Log in to MSR 4 as an administrator.
    2. Navigate to **Administration > Configuration**.
    3. Under **System Settings**, enable the **Repository Read-Only** option.
    4. Click **Save** to apply the changes.

2. Exclude Redis Persistent Volume Claims (PVCs), Persistent Volumes (PVs),
   and PODs from the backup:

    ```bash
    kubectl -n <msr4 namespace> label pod <msr4 redis pod> \
      velero.io/exclude-from-backup=true
    kubectl -n <msr4 namespace> label pvc <msr4 redis pvc> \
      velero.io/exclude-from-backup=true
    kubectl label pv/$(kubectl -n <msr4 namespace> get pvc <msr4 redis pvc> \
      --template={{.spec.volumeName}}) velero.io/exclude-from-backup=true
    ```

3. Create the MSR 4 backup:

    * [Snapshot Backups with Velero](../../ha-backup/snapshot-backups-with-velero.md)
    * [Filesystem-Level Backups with Velero](../../ha-backup/filesystem-level-backups-with-velero.md)

    !!! note

        If Redis and/or Postgres are in different namespaces than MSR 4,
        include all of the namespaces in the `backup` command:

        ```bash
        velero backup create <backup name> --include-namespaces postgres,msr4 [..]
        ```

4. If you use `postgres-operator` as the database provider for MSR 4, verify
   that the target (recovery) Kubernetes cluster includes `ClusterRole
   postgres-pod`:

    1. Verify that the `ClusterRole` exists:

        ```bash
        kubectl get clusterrole postgres-pod
        ```

    2. If the output of the command above is empty, create the role manually:

        ```yaml
        $ cat postgres-pod.yml
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          annotations:
            meta.helm.sh/release-name: postgres-operator
            meta.helm.sh/release-namespace: <msr4 namespace>
          labels:
            app.kubernetes.io/instance: postgres-operator
            app.kubernetes.io/managed-by: Helm
            app.kubernetes.io/name: postgres-operator
            helm.sh/chart: postgres-operator-1.14.0
          name: postgres-pod
          resourceVersion: "66364"
        rules:
        - apiGroups:
          - ""
          resources:
          - endpoints
          verbs:
          - create
          - delete
          - deletecollection
          - get
          - list
          - patch
          - update
          - watch
        - apiGroups:
          - ""
          resources:
          - pods
          verbs:
          - get
          - list
          - patch
          - update
          - watch
        - apiGroups:
          - ""
          resources:
          - services
          verbs:
          - create

        $ kubectl apply -f postgres-pod.yml
        ```

5. Restore MSR 4 on the target (recovery) Kubernetes cluster:

    * [Snapshot Backups with Velero](../../ha-backup/snapshot-backups-with-velero.md)
    * [Filesystem-Level Backups with Velero](../../ha-backup/filesystem-level-backups-with-velero.md)

6. Reconfigure the restored instance of MSR 4 on the target (recovery)
   Kubernetes cluster:

    1. Locate the Postgres Database service IP:

        ```bash
        kubectl get svc \
          -l application=spilo,cluster-name=msr-postgres,spilo-role=master \
          -o jsonpath={.items..spec.clusterIP} -n <postgres or msr4 namespace>
        ```

    2. Reconfigure MSR 4:

        !!! note

            Do not include the URL port for `expose.tls.auto.commonName` and
            `expose.ingress.hosts.core` if either is configured. Use only IP
            or DNS.

        ```bash
        helm upgrade <MSR4 Helm deployment name> \
          oci://registry.mirantis.com/harbor/helm/msr --debug \
          --set externalURL=https://<Restored MSR4 URL> -n <MSR4 namespace> \
          --reuse-values \
          --set expose.tls.auto.commonName=<Restored MSR4 URL> \
          --set expose.ingress.hosts.core=<Restored MSR4 URL> \
          --set database.external.host=<Postgres Database's service IP>
        ```
