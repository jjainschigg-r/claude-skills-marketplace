# Schedule backups and restores

Automate and schedule MSR backups and restores with Velero.

## Verify Velero installation

Ensure that Velero is already installed and configured in your Kubernetes
cluster. Check that:

* Velero is installed.
* Backup storage is configured (e.g., AWS S3, MinIO, Azure Blob).
* Snapshots are enabled if using incremental snapshot backup.


Run the following command to test if Velero is working:

```bash
velero backup create test-backup --include-namespaces=harbor
```

Verify the backup status:

```bash
velero backup describe test-backup
```

## Create a backup schedule with Velero

Velero provides a built-in **schedule** command for automating backups.

**Create a daily schedule**

Run the following command to create a backup schedule that runs daily at
a specific time:

```bash
velero schedule create daily-harbor-backup \
  --schedule="0 2 * * *" \
  --include-namespaces=harbor \
  --ttl=168h
```

* ``--schedule="0 2 * * *"`` - Schedules the backup to run daily at 2 AM (UTC).
  Modify this cron expression as needed.
* ``--include-namespaces=harbor`` - Ensures only the harbor namespace is backed
  up. Adjust if you need to include other namespaces.
* ``--ttl=168h`` - Sets the backup retention time to 7 days. Adjust based on
  your storage needs.
