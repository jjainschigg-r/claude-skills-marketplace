# Command Reference

This table provides the most frequently used commands in the
Mirantis Secure Registry (MSR) migration tool,
along with their equivalent entities in both source MSR and target MSR 4.

| Command           | MSR 2.9 / MSR 3.1                   | MSR 4                                  |
|-------------------|-------------------------------------|----------------------------------------|
| -a, --all         | All options below                   | All options below                      |
| -p, --projects    | repositories                        | project, project_metadata, quota, quota_usage |
| -m, --members     | repository_team_access               | project_member                         |
| -g, --groups      | teams                               | user_group                             |
| -l, --poll-mirroring | poll_mirroring_policies          | replication_policy, registry           |
| -s, --push-mirroring | push_mirroring_policies          | replication_policy, registry           |


## Command details

This section provides a detailed breakdown of each command used in the MSR
migration tool, including behavior, transformations, and the database tables
affected.

### -c/--config

Displays the active configuration and then exits.

### -p/--project

Exports repositories and namespaces. A `namespace` name is prefixed to
`repository` name to avoid issues with `accessLevel` permissions. The
`project_metadata` table on MSR 4 is populated with information such as
`auto_scan` (from `scanOnPush` on MSR) or `public` (from `visibility`
on MSR).

Additionally, `quota` and `quota_usage` tables on MSR 4 are populated
during project migration. These tables reference the `project_id`.
During migration, the tool initializes:

- `quota` to infinity (`-1`)
- `quota_usage` to `0`

### -m/--members

Exports team permissions. In MSR 4, project membership is per project, not
per repository. Therefore, a team on MSR 2.9 or MSR 3.1 is migrated as
a project member on MSR 4.

The `repository_team_access` table, which contains `teamId` and
`repositoryId` mappings, is used to populate the `project_member`
table by referencing a `project_id`. Therefore, projects must be created
before this step; otherwise, an error will occur. Each team is assigned an
`entity_type` of group, and roles are mapped as shown in the table below.

**Team role mapping:**

| MSR 2.9 / MSR 3.1 Role | MSR 2.9 / MSR 3.1 Permissions                       | MSR 4 Role    | MSR 4 Permissions                                                    | MSR 4 DB Role Type |
|------------------------|-----------------------------------------------------|---------------|----------------------------------------------------------------------|--------------------|
| admin                  | All permissions on given repository                 | Project Admin | All permissions on given repository                                  | 1                  |
| read-write             | Same as read-only + Push + Start Scan + Delete Tags | Maintainer    | Same as Limited Guest + Push + Start Scan + Create/Delete Tags + etc | 4                  |
| read-only              | View/Browse + Pull                                  |               |                                                                      |                    |

### -g/--groups

Exports LDAP groups. Because group names must be unique in MSR 4, each group is
prefixed with its organization name in the format
`<organization>-<group name>`. This naming convention helps prevent name
collisions. The LDAP group distinguished name (DN) in MSR 4 is set using the
`groupDN` field from Enzi.

Exporting LDAP groups only migrates the group definitions, it does not include
memberships or permissions. To migrate those, use the `--members` command.

### -l/--poll-mirroring

Exports all poll mirroring policies.

- Stored in the `replication_policies` table.
- Requires external `registry` entries, repositories to pull from.
- Data is saved in a project, hence projects must be created beforehand.
- Policies are prefixed with `pull-`.
- Trigger is set to **manual** by default (no cron job is set).

### -s/--push-mirroring

Exports all push mirroring policies.

- Stored in the `replication_policies` table.
- Requires external `registry` entries, repositories to pull from.
- Data is saved in a project, hence projects must be created beforehand.
- Policies are prefixed with `push-`.
- Trigger is set to **manual** by default (no cron job is set).

### -i/--trigger-replication-rules

Triggers all replication rules starting with `migration-rule-` using the cron
schedule set in `REPLICATION_TRIGGER_CRON`.

### -j/--remove-replication-rules-trigger

Removes cron trigger from all `migration-rule-` replication rules by setting
them to manual.

### -k/--delete-migration-rules

Deletes all replication rules starting with `migration-rule-`.
Data is recoverable with the `-p` option.

### -w/--trigger-push-replication-rules

Adds a cron job trigger to all **push** mirroring policies using the
`REPLICATION_TRIGGER_CRON` value.

### -x/--remove-push-replication-rules-trigger

Removes all cron schedules from push replication rules. Sets them to
**manual**.

### -y/--trigger-pull-replication-rules

Adds a cron job trigger to all **poll** mirroring policies using
`REPLICATION_TRIGGER_CRON`.

### -z/--remove-pull-replication-rules-trigger

Removes all cron schedules from pull replication rules. Sets them to
**manual**.

### -e/--export-all-replication-rules

Exports all rows contained in the `replication_policy` table from MSR 4
database.



