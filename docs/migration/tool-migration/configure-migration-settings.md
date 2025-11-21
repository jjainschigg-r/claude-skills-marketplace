# Configure Migration Settings

The following guide explains how to configure the environment and migration
settings to ensure a smooth transition between MSR versions.

## Configure Environment

To configure your target environment:

1. Create a directory named `config` in your current working directory.

2. Inside the `config` directory, create a file named `config.env`.

3. Add the required variables with the appropriate values according to your
   deployment.

    Ensure the following configuration is present:

    ```bash
    HARBOR_API_BASE_URL=<HARBOR-API-ENDPOINT-FQDN>
    HARBOR_API_USER=admin
    HARBOR_API_PASSWORD=<REDACTED>
    HARBOR_API_TLS_VERIFICATION=False
    HARBOR_DB_HOST=localhost
    HARBOR_DB_USER=msr
    HARBOR_DB_PASSWORD=<HARBOR-DB-PASSWORD>
    HARBOR_SECRET_KEY=<MSR4-SECRETKEY-VALUE> #Obtain from MSR4 values secretKey
    MIGRATION_SOURCE_REGISTRY_URL=<SOURCE-MSR-REGISTRY>
    MIGRATION_SOURCE_REGISTRY_ADMIN_USERNAME=admin
    MIGRATION_SOURCE_REGISTRY_ADMIN_PASSWORD=<ADMIN-PASSWORD>
    MIGRATION_SOURCE_REGISTRY_WITH_TLS_VERIFICATION=False
    ```

    !!! note

        The secret key in Harbor is required for replicating container images.

4. Configure the replication schedule in the `config/config.env` file. If you
   are running the migration immediately, update the default cron value to
   match your intended schedule.

    ```bash
    REUSE_ALREADY_FETCHED_DATA=True
    REPLICATION_TRIGGER_CRON="0 0 1 * * *"
    ```

    Refer to the [Configuration Reference](migration-tool-reference/configuration-reference.md) 
    for more details.

5. If you are migrating from an MSR 3 registry (as opposed to MSR 2),
   uncomment the following line:

    ```bash
    ENZI_RETHINKDB_MKE_DB_NAME=enzi
    ```

## Configure Migration Mode

By default, the migration tool migrates projects, repositories, and team
permissions in a granular mode, in which MSR 2 `organization/repository` with
team permissions are moved to MSR 4 project–team–repository path.

If the MSR 2 administrator assigns repository permissions only at the
organization level and not the team level, the migration will preserve
organization-level permissions. In such a case, MSR 2
`organization/repository` will map directly to MSR 4 `project/repository`.

### Determine Migration Mode

To identify which migration mode to use, run the following command from the
MSR 2 worker node:

```bash
export REPLICA_ID=$(docker ps -lf name='^/dtr-rethinkdb-.{12}$' --format '{{.Names}}' | cut -d- -f3)
docker run -it --rm --net dtr-ol -v dtr-ca-$REPLICA_ID:/ca mirantis/rethinkcli:v2.3.0 $REPLICA_ID

r.db('dtr2').table('repository_team_access')
```

If `repository_team_access` is empty, you can use 1-to-1 migration mode, but
if it contains entries, you should use granular migration mode.

### Configure Default Role

The MSR 4 Migration Tool migrates project permissions from MSR 2 and MSR 3.
If permissions are not set in the source MSR version, the default role is
applied. For that reason, you must configure the default group role in the
`config/config.env` file.

Valid values are:

- `read-only` (Limited Guest)
- `read-write` (Maintainer)
- `admin`

```bash
HARBOR_DEFAULT_GROUP_ROLE=read-only
```

For 1-to-1 migration mode, ensure the following settings are configured in
the `config/config.env` file:

```bash
IS_ENZI_TEAM_NAME_UNIQUE=True
IS_MAPPING_ORGANIZATION_1_TO_1=True
HARBOR_DEFAULT_GROUP_ROLE=read-only # or read-write, or admin
```

### Configure Replication Rules

By default, in 1-to-1 migration mode repositories and tags are migrated using
one migration replication rule per organization or project. In some cases,
administrators might prefer one migration replication rule per repository. To
enable this capability, set:

```bash
MIGRATION_REPLICATION_RULE_PER_REPO=True
```

When you migrate projects with this setting enabled, the replication rules are
created per `project/repository`.
