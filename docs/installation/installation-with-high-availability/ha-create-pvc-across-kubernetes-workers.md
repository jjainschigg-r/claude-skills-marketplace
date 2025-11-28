# Create PVC across Kubernetes workers

HA MSR requires a Persistent Volume Claim (PVC) that can be shared across all
worker nodes.

!!! note

    MSR 4 can use any StorageClass and PVC that you configure on your
    Kubernetes cluster. The following example sets up `cephfs` or NFS your
    default StorageClass. For more information, see
    [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
    in the official Kubernetes documentation.


## Configure cephfs

The following example shows how to configure persistent storage for Kubernetes
using `cephfs`. You can adapt these steps for your environment.

1. Create a `StorageClass`, the specifics of which depend on the storage
   backend you are using. The following example illustrates how to create a
   StorageClass class with a CephFS backend and Ceph CSI:

    ```yaml
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: cephfs
      annotations:
       storageclass.kubernetes.io/is-default-class: "true"
    provisioner: cephfs.csi.ceph.com
    parameters:
      clusterID: <cluster-id>
    ```

2. Run `kubectl apply` to apply the StorageClass configuration to the
   cluster, in the appropriate namespace.

3. Create the PVC:

    ```yaml
 
       apiVersion: v1
       kind: PersistentVolumeClaim
       metadata:
         name: shared-pvc
       spec:
         accessModes:
           - ReadWriteMany
         resources:
           requests:
             storage: 10Gi
         storageClassName: cephfs
    ```
    !!! note

        The `.spec.storageClassName` references the name of the
        `StorageClass` you created above.

4. Run `kubectl apply` to apply PVC to the cluster, in the appropriate
   namespace.

## Configure NFS

The following example shows how to configure persistent storage for Kubernetes
using NFS. You can adapt these steps for your environment.

1. Add the Helm repository for the NFS subdirectory external provisioner.

    ```bash
    helm repo add nfs-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
    helm repo update
    ```

2. Install the NFS client provisioner. Replace the placeholders with values for
   your environment.

    ```bash
    helm install nfs-client-provisioner nfs-provisioner/nfs-subdir-external-provisioner \
      --set nfs.server=<NFS-SERVER-IP> \
      --set nfs.path=</DIRECTORY/YOU/WANT/TO/USE> \
      --set storageClass.name=nfs-storage \
      --set storageClass.defaultClass=true
    ```
