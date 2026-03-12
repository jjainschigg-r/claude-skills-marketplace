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
   push mirroring policies will have the prefix `push-`. Each policy is
   migrated with its associated registry and by default has **Manual**
   Replication Trigger.

3. Configure the trigger for push replication policies in `config/config.env`:

    1. To enable an event-based replication, set:
   
        ```
        EVENT_BASED_PUSH_MIRRORING_REPLICATION_TRIGGER=True
        ```
   
        When new image tags are pushed, the replication policy schedules tasks to
        replicate the new tags to the destination registry.

    2. To enable scheduled replication using a cron expression, set:
   
        ```
        REPLICATION_TRIGGER_CRON=True
        ```

4. Trigger the push mirroring policies:

    ```bash
    docker run --rm \
       -v ./sql:/app/data/sql \
       -v ./csv:/app/data/csv \
       -v ./config:/app/config \
       --network host \
       registry.mirantis.com/msrh/migrate:latest \
       poetry run migration --trigger-push-replication-rules
    ```

    This command applies the trigger mode, either cron-based or event-based 
    defined in the `config/config.env`.

5. Remove scheduled triggers from all push mirroring policies and
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

    If push mirroring trigger needs to change from manual to cron-based or
    event-based, follow steps 3 and 4.

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
   poll mirroring policies will have the prefix `pull-`. Each policy is
   migrated with its associated registry and by default has **Manual**
   Replication Trigger.

3. Configure the trigger for poll replication policies in `config/config.env`:

    1. To enable an event-based replication, set:
   
        ```
        EVENT_BASED_PUSH_MIRRORING_REPLICATION_TRIGGER=True
        ```
   
        When new image tags are polled, the replication policy schedules tasks to
        replicate the new tags to the destination registry.
 
    2. To enable scheduled replication using a cron expression, set:
   
        ```
        REPLICATION_TRIGGER_CRON=True
        ```

4. Trigger the poll mirroring policies:

    ```bash
    docker run --rm \
       -v ./sql:/app/data/sql \
       -v ./csv:/app/data/csv \
       -v ./config:/app/config \
       --network host \
       registry.mirantis.com/msrh/migrate:latest \
       poetry run migration --trigger-pull-replication-rules
    ```

    This command applies the trigger mode, either cron-based or event-based 
    defined in the `config/config.env`.

5. Remove scheduled triggers from all poll mirroring policies and
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

    If poll mirroring trigger needs to change from manual to cron-based or
    event-based, follow steps 3 and 4.
