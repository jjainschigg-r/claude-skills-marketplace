# Best backup practices

* **Schedule Incremental Backups**

    Automate backups using Kubernetes CronJobs:

    ```bash
    velero backup create daily-harbor-backup-$(date +\%Y\%m\%d\%H\%M\%S) --include-namespaces=<MSR4 namespace> --snapshot-volume
    ```

    !!! note

        This cron job is scheduled to run daily at 2 AM.  
        The `$(date +\%Y\%m\%d\%H\%M\%S)` command appends a timestamp to each
        backup name to ensure uniqueness.

* **Retention Policy**

    Configure Velero to **prune old backups**:

    ```bash
    velero backup delete msr4-full-backup --confirm
    ```

    **OR** set a **time-to-live (TTL)** when creating backups:

    ```bash
    velero backup create msr4-backup-<timestamp> --include-namespaces <MSR4-namespace> --snapshot-volumes --ttl 168h --wait
    ```

    The example above retains the backup for 7 days.

* **Store Backups in Multiple Locations**

    For disaster recovery, store a copy of backups in an
    external object storage system (e.g., AWS S3, Azure
    Blob, GCS):

    ```bash
    velero backup describe msr4-backup-<timestamp>
    velero restore create --from-backup msr4-backup-<timestamp>
    ```


