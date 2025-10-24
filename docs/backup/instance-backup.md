# Single Instance Backup

This section provides a comprehensive guide for single
instance backup for Docker Compose MSR installation.

## Prerequisites

**Stop Write Operations (optional but recommended)**

Set MSR to read-only mode to
prevent data inconsistencies.

**Enable Read-Only Mode in MSR**:

1. Log in as an administrator.  
2. Go to **Administration**
   → **Configuration**.  
3. Under **System Settings**, enable
   **Repository Read-Only** mode.  
4. Click **Save**.

## Backup Components

A complete backup includes:

* **Registry Storage (Images and Artifacts)**
* **MSR Databases (PostgreSQL and Redis)**
* **Configuration Files**

## Backup Registry Storage (Default: `/data`)

If using **filesystem storage**, copy the image storage
directory:

```bash
tar -czvf harbor-registry-backup.tar.gz /data
```

If using an **S3-compatible backend**, ensure retention
policies exist on the object storage.

## Backup Databases (PostgreSQL and Redis)

MSR 4 uses PostgreSQL and Redis. Back them up
separately.

**Backup PostgreSQL:**

```bash
docker exec -t harbor-db pg_dumpall -U harbor > harbor-db-backup.sql
```

**Backup Redis (if needed - used for caching/session
storage):**

```bash
docker exec -t harbor-redis redis-cli save
cp /var/lib/redis/dump.rdb harbor-redis-backup.rdb
```


**Backup Configuration Files**

Back up the configuration and TLS certs from the install
directory (typically ``/etc/harbor/``):

```bash
tar -czvf harbor-config-backup.tar.gz /etc/harbor/
```

## Restore Process

If disaster recovery is needed, follow these steps:

1. **Stop Running Containers:**

    ```bash
    docker compose down
    ```

2. **Restore Registry Storage:**

    ```bash
    tar -xzvf harbor-registry-backup.tar.gz -C /
    ```

3. **Restore PostgreSQL Database:**

    ```bash
    cat harbor-db-backup.sql | docker exec -i harbor-db psql -U postgres -d registry
    ```

    Use ``-d registry`` to restore into the correct
    database.

4. **Restore Redis (if needed):**

    ```bash
    cp harbor-redis-backup.rdb /var/lib/redis/dump.rdb
    ```

5. **Restore Configuration Files:**

    ```bash
    tar -xzvf harbor-config-backup.tar.gz -C /
    ```

6. **Restart MSR:**

    ```bash
    docker compose up -d
    ```

7. **Automate and Schedule Backups**

    For regular automated backups, use cron jobs.

8. **Edit the crontab**

    ```bash
    crontab -e
    ```
   
9. Add a scheduled task to run nightly at 2 AM:

    ```bash
    0 2 * * * /bin/bash -c "tar -czvf /backup/harbor-registry-$(date +\%F).tar.gz /data && docker exec -t harbor-db pg_dumpall -U harbor > /backup/harbor-db-$(date +\%F).sql"
    ```

## How Long Will This Take?

| Component | Estimated Time |
|------------|----------------|
| Configuration Files (`/etc/harbor/`) | **<1 minute** |
| PostgreSQL DB Backup | **1-5 minutes** (depends on size) |
| Redis Backup | **<1 minute** |
| Registry Storage (`/data/`) | **Varies** (Minutes to Hours for TBs) |
