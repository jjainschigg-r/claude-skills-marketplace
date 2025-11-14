# Migrate Projects

During migration, source organizations and repositories are recreated as
projects. You can configure replication behavior both during and after
migration using the options provided by the migration tool.

To migrate repositories as projects:

1. Run the migration tool with the `--projects` flag to prepare the MSR 2.9
   or 3.1 repositories for migration:

    ```bash
    docker run --rm \
      -v ./sql:/app/data/sql \
      -v ./csv:/app/data/csv \
      -v ./config:/app/config \
      --network host \
      registry.mirantis.com/msrh/migrate:latest poetry run migration --projects
    ```

    The migration tool first exports data from MSR and Enzi. It then processes
    this data to import all repositories into MSR 4. Exported data is stored in
    the `csv` directory, while data prepared for import resides in the `sql`
    directory.

2. Optional. Verify if data has been exported:

     * Verify the `./csv` directory for exported data:

       ```bash
       ls -l csv
       ```

       Within the `csv` directory, all exported files are prefixed with either
       `msr_` or `enzi_`, indicating their source. Files prefixed with
       `harbor_` represent data migrated to MSR 4, exported for verification
       purposes.

     * Verify the `./sql` directory for SQL files that contain data to be
       imported into MSR 4:

       ```bash
       ls -l sql
       ```

    The migration recreates source organizations and repositories as projects.

3. Open the MSR web UI and verify if the projects are visible.

## Export data and migrate projects

**To run the migration replication process with Cron-Based trigger:**

1. Configure the replication schedule in the `config/config.env` file:

    ```bash
    REUSE_ALREADY_FETCHED_DATA=True
    REPLICATION_TRIGGER_CRON="0 0 1 * * *"
    ```

    See the [Configuration Reference](../reference-migration-tool/configuration-reference.md)
    for complete configuration reference.

2. Start an interactive partial migration:

    ```bash
    docker run --rm \
      -v ./data/sql:/app/data/sql \
      -v ./data/csv:/app/data/csv \
      -v ./config:/app/config \
      --network host \
      registry.mirantis.com/msrh/migrate:latest poetry run migration \
      --trigger-replication-rules
    ```

    !!! note

        The migration process may take a significant amount of time, depending
        on factors such as storage and network speed, and the volume of data in
        your project.

**To trigger the migration replication process manually:**

1. In the MSR 4 web UI, navigate to **Replication rules** page and check how
   many pages of `migration-rule` replication rules have been created.

2. Set the `PAGE` parameter in the command to match the number of pages.

    !!! note

        The `PAGE_SIZE` parameter corresponds to the page size setting in the
        MSR 4 web UI. For example, if the page size is set to `15`, use
        `--PAGE_SIZE=15`.

    ```bash
    docker run \
      -v ./sql:/app/data/sql \
      -v ./csv:/app/data/csv \
      -v ./config:/app/config \
      --network host \
      registry.mirantis.com/msrh/migrate:latest \
      utils/run-migration-replication-rules.sh --PAGE=1 --PAGE_SIZE=<NUMBER-OF-PAGES>
    ```

## Verify the migration replication status

To verify that all replication tasks have completed, run the following
command with your environment-specific values:

```bash
docker run registry.mirantis.com/msrh/migrate:latest utils/migration_replication_status.sh \
   --url=msr4.[MY-DOMAIN].com \
   --user=admin \
   --pwd=[ADMIN-PASSWORD]
```

Example output:

```text
Fetching policies with prefix 'migration-rule-'...

=== Replication Summary ===
Total executions:   191
Succeeded       :   188 (98.4%)
In Progress     :     0 ( 0.0%)
Failed          :     3 ( 1.6%)
Stopped         :     0 ( 0.0%)
Others          :     0 ( 0.0%)
```

!!! note

    To view command options and usage instructions, run:

    ```bash
    docker run registry.mirantis.com/msrh/migrate:latest utils/migration_replication_status.sh --help
    ```

## Limit the number of migration replication requests

Optional. To reduce the load on the source system, administrators can limit
the number of migration replication requests that MSR 4 sends to MSR 2.9.

To reconfigure `maxJobWorkers` and limit how many tags are being concurrently
migrated by MSR 4:

1. Set MSR4 to Read-Only Mode:

    1. Log in to MSR 4 as an administrator.
    2. Navigate to **Administration > Configuration**.
    3. Under **System Settings**, enable the **Repository Read-Only** option.
    4. Click **Save** to apply the changes.

2. In the `msr-values.yaml` file, change the `maxJobWorkers` parameter
   from `10` to `4`.

3. Apply the Helm chart.

4. Disable read-only mode:

    1. Log in to MSR 4 as an administrator.
    2. Navigate to **Administration > Configuration**.
    3. Under **System Settings**, disable the **Repository Read-Only** option.
    4. Click **Save** to apply the changes.
