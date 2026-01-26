# Storage

Storage is a critical component of the MSR 4 deployment, serving multiple
purposes, such as temporary job-related data and image storage. It can be
configured as local storage on the worker nodes or as shared storage,
utilizing a remote standalone storage cluster like **Ceph**, or by attaching a
dedicated storage application license.

Kubernetes cluster can provide storage for MSR 4 using a Container Storage
Interface (CSI), which supports static or dynamic volume provisioning:

- [Container Storage Interface (CSI) for Kubernetes GA](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)

- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

CSI drivers support different access modes. The most relevant access modes for
MSR 4 are:

- `ReadWriteMany`, which allows multiple Pods on different nodes to read from
  and write to the same shared volume. This mode is required for high
  availability (HA) configurations.

- `ReadWriteOnce`, which allows a single Pod on one node to read from and write
  to a volume. This mode is suitable for an all-in-one configuration.

To install MSR 4 in an HA configuration, the CSI must support `ReadWriteMany`.
MSR 4 can also be installed by using Helm in an all-in-one configuration by
following [Install MSR on a Single-Host using Helm](https://docs.mirantis.com/msr/4.13/installation/msr-helm-install/)
and setting one replica for each component.

## Local

Local storage is used for non-critical data that can be safely discarded
during development, testing, or when service instances are reinitialized.
This setup is primarily applicable in **All-in-One** deployments or when
storage redundancy is provided through hardware solutions, such as **RAID**
arrays on the worker nodes.

## Shared

The shared storage option offloads storage management to a separate device,
cluster, or appliance, such as a **Ceph cluster**. In the following PVC
example, **CephFS** is used to store the created volume. This approach ensures
that data is stored in a secure, robust, and reliable environment, making it an
ideal solution for **multi-node deployments and production environments**.

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

## Volumes

Refer to the
[Volume access type](../installation/installation-with-high-availability/ha-create-pvc-across-kubernetes-workers.md)
outlined in the installation section. While volumes used in
**All-in-One** deployments can utilize
the ``WriteToOne`` access mode, volumes that leverage shared storage may be
configured with the ``ReadWriteMany`` access mode. This allows the same volume
to be accessed by multiple replicas of services, such as **Job Service** or
**Registry**.

## External

Note that MSR 4 also offers the capability to integrate with
external object storage solutions, allowing data to be stored directly on
these platforms without the need for configuring Volumes and Persistent Volume
Claims (PVCs). This integration remains optional.
