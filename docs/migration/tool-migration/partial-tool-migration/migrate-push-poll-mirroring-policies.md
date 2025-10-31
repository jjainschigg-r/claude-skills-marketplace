# Migrate Push and Poll Mirroring Policies

Follow the steps below to migrate push and poll mirroring policies. Each set
of policies can be exported, triggered, and optionally reconfigured to use
manual scheduling.

## Migrate push mirroring policies

1. Run the migration tool to export push mirroring policies from MSR:

   ```bash
   docker run --rm \
      -v ./sql:/app/data/sql \
      -v ./csv:/app/data/csv \
      -v ./config:/app/config \
      --network host \
      registry.mirantis.com/msrh/migrate:latest \
      poetry run migration --push-mirroring
   ```

2. Verify the imported policies in **Administration > Replications**. All
   push mirroring policies will have the prefix `push-`. Each policy is migrated
   with its associated registry.

3. Trigger the push mirroring policies:

   ```bash
   docker run --rm \
      -v ./sql:/app/data/sql \
      -v ./csv:/app/data/csv \
      -v ./config:/app/config \
      --network host \
      registry.mirantis.com/msrh/migrate:latest \
      poetry run migration --trigger-push-replication-rules
   ```

   This command applies a cron schedule defined in the
   `REPLICATION_TRIGGER_CRON` environment variable.

4. Optional. Remove scheduled triggers from all push mirroring policies and
   switch them to manual triggering:

   ```bash
   docker run --rm \
      -v ./sql:/app/data/sql \
      -v ./csv:/app/data/csv \
      -v ./config:/app/config \
      --network host \
      registry.mirantis.com/msrh/migrate:latest \
      poetry run migration --remove-push-replication-rules-trigger
   ```

## Migrate poll mirroring policies

1. Run the migration tool to export poll mirroring policies from MSR:

   ```bash
   docker run --rm \
      -v ./sql:/app/data/sql \
      -v ./csv:/app/data/csv \
      -v ./config:/app/config \
      --network host \
      registry.mirantis.com/msrh/migrate:latest \
      poetry run migration --poll-mirroring
   ```

2. Verify the imported policies in **Administration > Replications**. All
   poll mirroring policies will have the prefix `pull-`. Each policy is migrated
   with its associated registry.

3. Trigger the poll mirroring policies:

   ```bash
   docker run --rm \
      -v ./sql:/app/data/sql \
      -v ./csv:/app/data/csv \
      -v ./config:/app/config \
      --network host \
      registry.mirantis.com/msrh/migrate:latest \
      poetry run migration --trigger-pull-replication-rules
   ```

   This command applies a cron schedule defined in the
   `REPLICATION_TRIGGER_CRON` environment variable.

4. Optional. Remove scheduled triggers from all poll mirroring policies and
   switch them to manual triggering:

   ```bash
   docker run --rm \
      -v ./sql:/app/data/sql \
      -v ./csv:/app/data/csv \
      -v ./config:/app/config \
      --network host \
      registry.mirantis.com/msrh/migrate:latest \
      poetry run migration --remove-pull-replication-rules-trigger
   ```
