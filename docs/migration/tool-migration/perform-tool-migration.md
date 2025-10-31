# Perform Migration

To migrate images, repositories, and tags from an MSR 2.9 or MSR 3.1 environment
to MSR 4.x, you can either run the migration as a single comprehensive
operation, which is the recommended path, or break it into specific steps if
needed. The migration tool supports both full and partial migrations, with
detailed options described in the `--help` flag and active configuration in
the `--config` flag.

To migrate all data in one step, run:

```bash
docker run --rm \
  -v ./sql:/app/data/sql \
  -v ./csv:/app/data/csv \
  -v ./config:/app/config \
  --network host \
  registry.mirantis.com/msrh/migrate:latest poetry run migration --all
```

To perform the migration in individual steps:

- [Migrate Projects](partial-tool-migration/migrate-projects.md)
- [Migrate Permissions](partial-tool-migration/migrate-permissions.md)
- [Migrate Push and Poll Mirroring Policies](partial-tool-migration/migrate-push-poll-mirroring-policies.md)

To view all available options for partial migrations, use the `--help` flag
with the migration tool.


