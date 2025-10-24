# Monitoring backup and restore status

Use these commands to check the status of backups and restores:

**To list all backups:**

```bash
velero backup get
```

**To list all restores:**

```bash
velero restore get
```

**To check details of a specific backup:**

```bash
velero backup describe msr4-full-backup --details
```

**To check details of a specific restore:**

```bash
velero restore describe msr4-restore --details
``` 
