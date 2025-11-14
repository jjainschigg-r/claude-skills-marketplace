# NFS Full Restore

The procedure herein details the steps that are required to perform a full
cross-cluster Disaster Recovery restore of an MSR 4 instance, leveraging Velero
and MinIO to perform a complete end-to-end backup. This method is intended for
scenarios wherein both the Kubernetes configuration and all registry data
(blobs) must be migrated to a separate cluster, regardless of whether the
underlying storage is shared.

Mirantis recommends using this approach only for small MSR 4 instances,
as it requires that you copy all registry data (image blobs) into and out
of the MinIO backup storage, which is time-consuming and resource-intensive.
Full backup and restore is recommended only for MSR 4 instances that have a
small total size of image and artifact data. For production environments with
large registries, use the [NFS Metadata Restore](../nfs-metadata-restore/index.md)
to a different cluster method.

## Prerequisites

Verify that your Kubernetes cluster is configured with a compatible CSI driver.
For Snapshot backup, the CSI driver must support snapshot operations for your
storage provider.

## Procedure

* [Install MinIO and Velero](full-install-minio-and-velero.md)
* [Backup and Restore](full-restore-backup.md)


