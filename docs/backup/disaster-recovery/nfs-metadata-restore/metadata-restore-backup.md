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

2. Exclude the Redis Persistent Volume Claims (PVCs), Persistent Volumes (PVs)
   and PODs from backup:

    ```bash
    kubectl -n <msr4 namespace> label pod <msr4 redis pod> velero.io/exclude-from-backup=true
    kubectl -n <msr4 namespace> label pvc <msr4 redis pvc> velero.io/exclude-from-backup=true
    kubectl label pv/$(kubectl -n <msr4 namespace> get pvc <msr4 redis pvc> --template={{.spec.volumeName}}) velero.io/exclude-from-backup=true
    ```

3. Exclude the Registry POD, Persistent Volume Claims (PVCs) and Persistent Volumes
   (PVs) from the backup:

    ```bash
    kubectl label pod <msr4 registry pod> velero.io/exclude-from-backup=true
    kubectl label pvc <msr4 registry pvc> velero.io/exclude-from-backup=true
    kubectl label pv/$(kubectl -n <msr4 namespace> get pvc <msr4 registry pvc>  --template={{.spec.volumeName}}) velero.io/exclude-from-backup=true
    ```

4. Create the MSR 4 backup:

    * [Snapshot Backups with Velero](../../ha-backup/snapshot-backups-with-velero.md)
    * [Filesystem-Level Backups with Velero](../../ha-backup/filesystem-level-backups-with-velero.md)

    !!! note

        If Redis and/or Postgres are in a different namespaces than MSR 4,
        include all the namespaces in the `backup` command:

        ```bash
        velero backup create <backup name> --include-namespaces postgres,msr4 [..]
        ```

5. Save the Registry's Persistent Volume Claims (PVCs) and Persistent Volumes
   (PVs) specifications in the YAML files:

    ```bash
    kubectl -n <msr4 namespace> label pod <msr4 registry pod> velero.io/exclude-from-backup=true
    kubectl -n <msr4 namespace> label pvc <msr4 registry pvc> velero.io/exclude-from-backup=true
    kubectl -n <msr4 namespace> label pv/$(kubectl -n <msr4 namespace> get pvc <msr4 registry pvc> --template={{.spec.volumeName}}) velero.io/exclude-from-backup=true
    ```

6. Modify the YAML files that will be applied to the target (recovery)
   Kubernetes cluster:

    * In the `msr4-pvc-registry.yml` file, ensure that:

        * `storageClassName` is empty.
        * `volumeName` matches the PV name.
        * `spec.capacity.storage: 5Gi` is the same as the original.
        * `accessModes: ReadWriteMany` is the same as the original.

        ```yaml
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
          name: msr4-harbor-registry
          namespace: <MSR4 namespace>
        spec:
          accessModes:
          - ReadWriteMany
          resources:
            requests:
              storage: 5Gi
          storageClassName:
          volumeName: <PV name>
        ```

    * In the `msr4-pv-registry.yaml` file, ensure that:

        * `spec.nfs.server` contains the IP or hostname of the NFS server.
        * `spec.nfs.path` contains the exact export path on the NFS server where
          the blobs are stored.
        * `spec.capacity.storage: 5Gi` is the same as the original.
        * `spec.accessModes: ReadWriteMany` is the same as the original.
        * `persistentVolumeReclaimPolicy` is always retained to avoid data loss.
        * The entire `status` section is removed.
        * The entire `spec.claimRef` section is removed.

        ```yaml
        apiVersion: v1
        kind: PersistentVolume
        metadata:
          annotations:
            pv.kubernetes.io/provisioned-by: nfs.csi.k8s.io
            volume.kubernetes.io/provisioner-deletion-secret-name: ""
            volume.kubernetes.io/provisioner-deletion-secret-namespace: ""
          finalizers:
          - external-provisioner.volume.kubernetes.io/finalizer
          - kubernetes.io/pv-protection
          labels:
          name: <PV name>
        spec:
          accessModes:
          - ReadWriteMany
          capacity:
            storage: 5Gi
          csi:
            driver: nfs.csi.k8s.io
            volumeAttributes:
              csi.storage.k8s.io/pv/name: <PV name>
              csi.storage.k8s.io/pvc/name: msr4-harbor-registry
              csi.storage.k8s.io/pvc/namespace: <MSR4 namespace>
              mountPermissions: "0"
              server: <NFS URL>
              share: <NFS path>
              subdir: <PV name>
            volumeHandle: <NFS URL>#var/nfs/general#<NFS path>##
          mountOptions:
          - nfsvers=4.1
          persistentVolumeReclaimPolicy: Delete
          storageClassName: <NFS CSI storage class>
          volumeMode: Filesystem
        ```

7. Apply Persistent Volumes (PVs) to the target (recovery) Kubernetes cluster,
   and verify that it is in `Available` status:

    ```bash
    kubectl apply -f msr4-pv-registry.yaml
    kubectl get pv <PV name>
    ```

    Example output:

    ```text
    NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM                                      STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
    pvc-c9383d47-74b6-4c04-857c-6b5f05164171   5Gi        RWX            Delete           Available                                              nfs-csi        <unset>                          5s
    ```

8. Apply Persistent Volume Claim (PVC) and wait until it is in `Bound`
   status:

    ```bash
    kubectl apply -f msr4-pvc-registry.yml
    kubectl get pvc <PVC name>
    ```

    Example output:

    ```bash
    kubectl get pvc
    NAME                   STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
    msr4-harbor-registry   Pending   pvc-c9383d47-74b6-4c04-857c-6b5f05164171   0                         nfs-csi        <unset>                 6s

    kubectl get pvc
    NAME                   STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
    msr4-harbor-registry   Bound    pvc-c9383d47-74b6-4c04-857c-6b5f05164171   5Gi        RWX            nfs-csi        <unset>                 15s
    ```

9. If Postgres Operator is used as the database provider for MSR 4, verify that
   the target (recovery) Kubernetes cluster includes
   `ClusterRole postgres-pod`:

    1. Verify that the `ClusterRole` exists:

        ```bash
        kubectl get clusterrole postgres-pod
        ```

    2. If the output of the command above is empty, manually create the role in
       `postgres-pod.yml`:

        ```yaml
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
        ```

10. Apply Postgres Pod to the target (recovery) Kubernetes cluster:

    ```bash
    kubectl apply -f postgres-pod.yml
    ```

11. Restore MSR 4 on the target (recovery) Kubernetes cluster:

    * [Snapshot Backups with Velero](../../ha-backup/snapshot-backups-with-velero.md)
    * [Filesystem-Level Backups with Velero](../../ha-backup/filesystem-level-backups-with-velero.md)

12. Reconfigure the restored instance of MSR 4 on the target (recovery)
    Kubernetes cluster:

    1. Locate the Postgres Database service IP:

        ```bash
        kubectl get svc \
          -l application=spilo,cluster-name=msr-postgres,spilo-role=master \
          -o jsonpath={.items..spec.clusterIP} -n <postgres or msr4 namespace>
        ```

    2. Reconfigure MSR 4:

        !!! note

            Do not use the URL port for `expose.tls.auto.commonName` and
            `expose.ingress.hosts.core` if either is configured. Use only IP
            or DNS.

        ```bash
        helm upgrade <MSR4 Helm deployment name> \
          oci://registry.mirantis.com/harbor/helm/msr \
          --debug \
          --set externalURL=https://<Restored MSR4 URL> \
          -n <MSR4 namespace> \
          --reuse-values \
          --set expose.tls.auto.commonName=<Restored MSR4 URL> \
          --set expose.ingress.hosts.core=<Restored MSR4 URL> \
          --set database.external.host=<Postgres Database's service IP>
        ```
