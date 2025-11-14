# Post-Migration Cleanup

!!! caution

    Before deprecating MSR 2.9 or MSR 3.1, run the migration one last time to
    ensure all data has been transferred.

When you no longer plan to push data to your MSR 2.9 or MSR 3.1 instances,
you can remove the replication schedules:

1. Remove the trigger of replication rules:

    ```bash
    docker run --rm \
        -v ./sql:/app/data/sql \
        -v ./csv:/app/data/csv \
        -v ./config:/app/config \
        --network host \
        registry.mirantis.com/msrh/migrate:latest poetry run migration --remove-replication-rules-trigger
    ```

2. Check your **Replications** service dashboard to verify if they were
   switched to manual.

3. Delete all replication rules created for the migration, use the
   `--delete-migration-rules` option. This removes all rules prefixed with
   `migration-rule-`.

    ```bash
    docker run --rm \
        -v ./sql:/app/data/sql \
        -v ./csv:/app/data/csv \
        -v ./config:/app/config \
        --network host \
        registry.mirantis.com/msrh/migrate:latest poetry run migration --delete-migration-rules
    ```

!!! note "Additional considerations"

    Re-running the script with `--trigger-replication-rules` re-enables
    scheduled execution for all migration-rule replication rules. The schedule
    is defined by the `REPLICATION_TRIGGER_CRON` environment variable.

    Use the appropriate command-line flags based on the replication policy type:

    - `--trigger-push-replication-rules` and
      `--remove-push-replication-rules-trigger` for push policies

    - `--trigger-pull-replication-rules` and
      `--remove-pull-replication-rules-trigger` for pull policies

    Before performing any deprecating operations, use
    `--export-all-replication-rules` to back up all replication rules from
    the `replication_policy` table in MSR 4.

## Delete Custom Replication Rules

You can delete all pull or push replication rules or filter them by the source
or destination registry domains.

- **To delete all pull replication rules:**

    ```bash
    docker run --rm \
        -v ./sql:/app/data/sql \
        -v ./csv:/app/data/csv \
        -v ./config:/app/config \
        --network host \
        registry.mirantis.com/msrh/migrate:latest poetry run migration --delete-pull-replication-rules
    ```

- **To delete pull replication rules that match a specific source registry
  domain, for example index.docker.io:**

    ```bash
    docker run --rm \
        -v ./sql:/app/data/sql \
        -v ./csv:/app/data/csv \
        -v ./config:/app/config \
        --network host \
        registry.mirantis.com/msrh/migrate:latest poetry run migration --delete-pull-replication-rules --replication-rule-remote-registry index.docker.io
    ```

- **To delete all push replication rules:**

    ```bash
    docker run --rm \
        -v ./sql:/app/data/sql \
        -v ./csv:/app/data/csv \
        -v ./config:/app/config \
        --network host \
        registry.mirantis.com/msrh/migrate:latest poetry run migration --delete-push-replication-rules
    ```

- **To delete push replication rules that match a specific source registry
  domain, for example index.docker.io:**

    ```bash
    docker run --rm \
        -v ./sql:/app/data/sql \
        -v ./csv:/app/data/csv \
        -v ./config:/app/config \
        --network host \
        registry.mirantis.com/msrh/migrate:latest poetry run migration --delete-push-replication-rules --replication-rule-remote-registry index.docker.io
    ```

