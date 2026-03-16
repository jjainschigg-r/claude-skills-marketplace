# Velero Installation

Install Velero on an MSR instance to enable the backup and restore of Kubernetes
cluster resources. For more information, refer to the official
[Velero documentation](https://velero.io/).

!!! note "MKE 4k installations"

    If you are running MKE 4k, note that Velero was included through version 4.1.1.
    Starting with version 4.1.2, however, it is no longer bundled
    and must be installed separately. Velero remains a fully supported backup
    solution for all MSR 4 on MKE 4k deployments.

## Prerequisites

Ensure the following requirements are met before installing Velero:

**Kubernetes cluster**

  - Install Kubernetes version 1.16 or later with DNS and container networking enabled.

**Local tools**

  - Install and configure `kubectl` locally.

**Storage providers**

  - An object storage provider is required for backups and artifacts.
  - A block storage provider is optional and used for volume snapshots.
  - Select your storage and volume providers from the
    [Velero supported providers](https://velero.io/docs/v1.18/supported-providers/).
    Velero supports both Cloud and on-premises environments.

**Storage plugins**

  - Refer to the [Velero installation customization guide](https://velero.io/docs/v1.18/customize-installation/)
    to determine the required plugins and installation flags for your selected storage providers.

## Install the Velero CLI

To install the Velero CLI on both the source (primary) and target
(recovery) Kubernetes clusters, refer to the
[Velero CLI installation guide](https://velero.io/docs/v1.8/basic-install/).

## Install Velero

Install Velero on both the source (primary) and target (recovery)
Kubernetes clusters.

Because Velero integrates with the underlying infrastructure, the
installation commands may vary depending on your environment and storage
configuration.

1. Create the `credentials-velero` file:

    ```bash
    cat credentials-velero
    [default]
    aws_access_key_id=<access key from mino-tenant>
    aws_secret_access_key=<secret access key from mino-tenant>
    ```

2. Install Velero:

    * For the snapshot backup:

        ```bash
        velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.13.0 --bucket msr4-backup --secret-file ./credentials-velero --backup-location-config s3Url=https://<minio-tenant API URL>:<minio-tenant API Port>,s3ForcePathStyle=true,insecureSkipTLSVerify=true --use-volume-snapshots=true --use-node-agent --features=EnableCSI --snapshot-location-config region=default
        ```

    * For the file system backup:

        ```bash
        velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.13.0 --bucket <Minio bucket name> --secret-file ./credentials-velero --backup-location-config s3Url=https://<minio-tenant API URL>:<minio-tenant API Port>,s3ForcePathStyle=true,insecureSkipTLSVerify=true --use-volume-snapshots=false --use-node-agent
        ```

        !!! note
            The source and target clusters must both have Velero
            configured to point to the same MinIO Tenant URL and Backup
            Storage Location (BSL) bucket.

3. Verify backup location on both the source (primary) and target
   (recovery) Kubernetes clusters:

    * For the snapshot backup:

        ```bash
        kubectl -n velero describe VolumeSnapshotLocation
        ```

    * For the file system backup:

        ```bash
        kubectl -n velero describe backupstoragelocations
        ```
