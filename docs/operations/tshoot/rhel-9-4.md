# MSR installation may fail on RHEL 9.4 and later

When deploying MSR in High Availability mode using Helm on Red Hat Enterprise
Linux (RHEL) 9.4 or later, installation may fail due to a
[segmentation fault in the bg_mon module](https://github.com/zalando/spilo/issues/1039).  
This issue occurs when PostgreSQL is deployed using the `zalando/spilo` image.

## Symptoms

The failure manifests with the following error messages:

In the `harbor-core` pod:

```ini
2025-06-24T07:58:01Z [INFO] [/common/dao/pgsql.go:135]: Upgrading schema for pgsql ...
2025-06-24T07:58:01Z [ERROR] [/common/dao/pgsql.go:140]: Failed to upgrade schema, error: "Dirty database version 11. Fix and force version."
2025-06-24T07:58:01Z [FATAL] [/core/main.go:204]: failed to migrate the database, error: Dirty database version 11. Fix and force version.
```

On the node hosting the `msr-postgres` pod:

```ini
Jun 24 07:55:19 ip-172-31-0-252.eu-central-1.compute.internal systemd[1]: Created slice Slice /system/systemd-coredump.
Jun 24 07:55:19 ip-172-31-0-252.eu-central-1.compute.internal systemd[1]: Started Process Core Dump (PID 34335/UID 0).
Jun 24 07:55:19 ip-172-31-0-252.eu-central-1.compute.internal systemd-coredump[34336]: [🡕] Process 27789 (postgres) of user 101 dumped core.
```

## Workaround

Exclude the `bg_mon` module from the PostgreSQL configuration:

```yaml
apiVersion: "acid.zalan.do/v1"
kind: postgresql
metadata:
  name: msr-postgres
spec:
  teamId: "msr"
  volume:
    size: 1Gi
  numberOfInstances: 3
  users:
    msr:
      - superuser
      - createdb
  databases:
    registry: msr
  postgresql:
    version: "17"
    parameters:
      shared_preload_libraries: "pg_stat_statements,pgextwlist,pg_auth_mon,set_user,timescaledb,pg_cron,pg_stat_kcache"
```
