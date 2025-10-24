# Filesystem-Level Backups with Velero

## Create a backup

1. Set MSR4 to Read-Only Mode.

    Before initiating the backup, set MSR4 to Read-Only mode
    to prevent new data from being written during the
    process, minimizing inconsistencies.

    1. Log in to MSR4 as an administrator.  
    2. Navigate to **Administration**
       -> **Configuration**.  
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

    **Create a Full Backup**

    Run the following command to create a full backup:

    ```bash
    velero backup create msr4-full-backup --include-namespaces harbor --default-volumes-to-fs-backup --wait
    ```

    **Create an Incremental Backup**

    After the full backup, incremental backups happen
    automatically. They capture only the changes since the
    last backup:

    ```bash
    velero backup create msr4-incremental-backup --include-namespaces harbor --default-volumes-to-fs-backup --wait
    ```

4. Complete backup by unsetting Read-Only mode.

    Once the backup is complete, revert MSR4 to its normal
    operational state:

    1. Navigate to **Administration**
       -> **Configuration**.  
    2. Under **System Settings**, disable the
       **Repository Read-Only** option by unchecking
       it.  
    3. Click **Save** to apply the changes.

## Restore process

**Restore a Full Backup**

To restore from a Full Backup, use the following command:

```bash
velero restore create msr4-restore --from-backup msr4-full-backup
```

**Restore an Incremental Backup**

To restore from an Incremental Backup, use the following
command:

```bash
velero restore create msr4-incremental-restore --from-backup msr4-incremental-backup
```


