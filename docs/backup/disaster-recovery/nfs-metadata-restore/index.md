# NFS Metadata Restore

The procedure herein details the steps required to perform a cross-cluster
disaster recovery restore of an MSR 4 instance. This method is intended for
environments wherein both the source and target Kubernetes clusters use the
same underlying NFS storage backend along with MinIO backup storage.

Shared persistent storage significantly accelerates the recovery process by
circumventing the movement of large registry data files.

## Prerequisites

Verify that a compatible CSI driver is installed and configured in your
Kubernetes cluster. For Snapshot backup, the CSI driver must support snapshot
operations for your storage provider.

## Procedure

* [Install MinIO and Velero](metadata-install-minio-and-velero.md)
* [Backup and Restore](metadata-restore-backup.md)
