# Snapshot Backups with Velero

This method leverages Velero’s integration with Container
Storage Interface (CSI) drivers to create volume snapshots,
providing efficient and consistent backups for cloud-native
environments.

## Prerequisites

* **Velero Installation with CSI Support**  
    Ensure Velero is installed with CSI snapshot support
    enabled. This requires the `EnableCSI` flag during
    installation. For detailed instructions, refer to the
    official Velero documentation:  
    [Container Storage Interface Snapshot Support in Velero](https://velero.io/docs/main/csi/)

* **CSI Driver Installation**  
    Confirm that a compatible CSI driver is installed and
    configured in your Kubernetes cluster. The CSI driver
    should support snapshot operations for your storage
    provider.

## Backup process using Velero with CSI Snapshots

1. Set MSR 4 to Read-Only Mode.

    Before initiating the backup, set MSR 4 to Read-Only
    mode to prevent new data from being written during the
    process, minimizing inconsistencies.

    1. Log in to MSR 4 as an administrator.  
    2. Navigate to **Administration** -> **Configuration**.  
    3. Under **System Settings**, enable the
       **Repository Read-Only** option.  
    4. Click **Save** to apply the changes.

2. Optional: Label Redis-Related Resources for Exclusion.

    To avoid backing up ephemeral data, exclude Redis-related
    resources from the backup.

    1. Label the Redis Pod:

        ```bash
        kubectl -n <MSR4-NAMESPACE> label pod <REDIS-POD-NAME> velero.io/exclude-from-backup=true
        ```

    2. Repeat the labeling process for the Redis
       PersistentVolumeClaim (PVC) and PersistentVolume (PV):

        ```bash
        kubectl -n <MSR4-NAMESPACE> label pvc <REDIS-PVC-NAME> velero.io/exclude-from-backup=true
        kubectl -n <MSR4-NAMESPACE> label pv <REDIS-PV-NAME> velero.io/exclude-from-backup=true
        ```

3. Create a backup.

    * **Create a Full Snapshot Backup (Recommended for initial backup)**

        Full Snapshot Backup is recommended for an initial
        backup.

        Use the following command to back up the entire MSR 4
        namespace, capturing snapshots of all
        PersistentVolumes:

        ```bash
        velero backup create msr4-full-backup --include-namespaces <MSR4-namespace> --snapshot-volumes --wait
        ```

    * **Create an Incremental Snapshot Backup**

        After the full backup, incremental backups happen
        automatically. They capture only the changes since the
        last backup if the CSI Storage driver supports this
        capability. Please check with the manufacturer of your
        CSI driver.

        When running **incremental backups**, use the
        `--from-backup` flag:

        ```bash
        velero backup create msr4-full-backup --include-namespaces <MSR4-NAMESPACE> --snapshot-volumes --wait
        ```

        !!! note
   
            Replace `<TIMESTAMP>` with the current date and time
            to uniquely identify each backup.  
            This command can be scheduled to run periodically.

## Restore process

To restore MSR 4 from a snapshot backup, follow these steps:

* **Restore a Full Backup**

    1. Set MSR 4 to Read-Only Mode.

        1. Log in to MSR 4 as an administrator.  
        2. Navigate to **Administration** -> **Configuration**.  
        3. Under **System Settings**, enable the
           **Repository Read-Only** option.  
        4. Click **Save** to apply the changes.

    2. Run the restore command.

        Restore from the most recent backup:

        ```bash
        velero restore create msr4-restore --from-backup msr4-full-backup --wait
        ```

* **Restore an Incremental Backup**

    1. Set MSR 4 to Read-Only Mode.

        1. Log in to MSR 4 as an administrator.  
        2. Navigate to **Administration** -> **Configuration**.  
        3. Under **System Settings**, enable the
           **Repository Read-Only** option.  
        4. Click **Save** to apply the changes.

    2. Run the restore command.

        Restore from the most recent backup:

        ```bash
        velero restore create msr4-restore-incremental --from-backup msr4-incremental-backup --wait
        ```

## Complete backup by unsetting Read-Only mode

After the backup is complete, revert MSR 4 to its normal operational state:

1. Navigate to **Administration** -> **Configuration**.  
2. Under **System Settings**, disable the
   **Repository Read-Only** option by unchecking it.  
3. Click **Save** to apply the changes.

