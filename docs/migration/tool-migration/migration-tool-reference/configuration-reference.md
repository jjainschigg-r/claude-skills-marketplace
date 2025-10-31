# Configuration Reference

| Parameter | Description | Default |
|------------|--------------|----------|
| INSERT_HARBOR_PROJECTS_SQL | File including SQL statements to create projects. | ``harbor_projects.sql`` |
| INSERT_HARBOR_PROJECTS_USER_GROUPS_SQL | File including SQL statements to create user groups. Maps `<team-name>` on Enzi to `<organization>-<team-name>`. | ``harbor_projects_user_groups.sql`` |
| INSERT_HARBOR_ORGANIZATIONS_USER_GROUPS_SQL | File including SQL statements to create user groups. Maps `<team-name>` on Enzi to `<team-name>`. | ``harbor_organizations_user_groups.sql`` |
| INSERT_HARBOR_MSR_REPO_TEAM_TO_PROJECTS_MEMBERS_SQL | File with SQL statements to grant user permissions to projects. Maps ``repository_team_access`` | ``harbor_msr_team_to_project_member.sql`` |
| INSERT_HARBOR_MSR_ORG_TEAM_TO_PROJECTS_MEMBERS_SQL | File with SQL statements to grant user permissions to projects. Maps ``namespace_team_access``. | ``harbor_msr_org_to_project_member.sql`` |
| INSERT_HARBOR_PROJECT_METADATA_SQL | File with SQL to attach project metadata, including visibility and ``scanOnPush`` settings. | ``harbor_project_metadata.sql`` |
| INSERT_HARBOR_PROJECT_QUOTA_SQL | File including SQL statements to configure project quotas. Default is unlimited storage per project. | ``harbor_project_quota.sql`` |
| INSERT_HARBOR_IMMUTABLE_TAG_RULE_SQL | File including SQL to add immutability tag rules to projects. | ``harbor_immutable_tag_rule.sql`` |
| INSERT_HARBOR_RETENTION_POLICY_SQL | File including SQL to create retention rules. Maps part of the pruning policies. | ``harbor_retention_policy.sql`` |
| INSERT_HARBOR_PUSH_MIRRORING_POLICIES_SQL | File including SQL to define push replication policies. | ``harbor_push_mirroring_policies.sql`` |
| INSERT_HARBOR_POLL_MIRRORING_POLICIES_SQL | File including SQL to define pull replication policies. | ``harbor_poll_mirroring_policies.sql`` |
| HARBOR_API_BASE_URL | Hostname or IP for connecting to the API. | ``localhost`` |
| HARBOR_API_USER | Username for connecting to the API. | ``admin`` |
| HARBOR_API_PASSWORD | Password for connecting to the API. | ``MSR12345`` |
| HARBOR_API_TLS_VERIFICATION | Defines whether to verify SSL certificates. Should be ``true`` for production. | None |
| HARBOR_API_BATCH_SIZE | Defines the chunk size of data handled per API request. | None |
| HARBOR_DB_PASSWORD | Password used to connect to the MSR 4 PostgreSQL database. | ``root123`` |
| HARBOR_DB_HOST | Hostname or IP address for the MSR 4 PostgreSQL database. | ``localhost`` |
| HARBOR_DB_PORT | Port for the MSR 4 PostgreSQL database connection. | ``5432`` |
| HARBOR_DB_USER | Username to connect to the MSR 4 PostgreSQL database. | ``postgres`` |
| HARBOR_DB_NAME | Database name for the MSR 4 PostgreSQL database. | ``registry`` |
| HARBOR_DEFAULT_SYSTEM_ADMIN_ID | Owner ID for all projects created during migration. Default is the MSR 4 system admin ID. | ``1`` |
| HARBOR_DEFAULT_REGISTRY_ID | Registry ID where all projects and replication policies are created. | ``0`` |
| HARBOR_SECRET_KEY | Secret key used to encrypt passwords for registries. | ``secret`` |
| ENZI_RETHINKDB_HOST | Hostname or IP for the Enzi RethinkDB database. | ``localhost`` |
| ENZI_RETHINKDB_PORT | Port for the Enzi RethinkDB database. | ``28015`` |
| ENZI_RETHINKDB_DB_NAME | Database name for Enzi RethinkDB. | ``enzi`` |
| ENZI_ACCOUNTS_CSV | CSV file containing all Enzi accounts. | ``enzi_accounts.csv`` |
| ENZI_TEAMS_CSV | CSV file containing all Enzi teams. | ``enzi_teams.csv`` |
| MSR_RETHINKDB_HOST | Hostname or IP for the MSR 2.9 or MSR 3.1 RethinkDB database. | ``localhost`` |
| MSR_RETHINKDB_PORT | Port for the MSR 2.9 or MSR 3.1 RethinkDB database. | ``28016`` |
| MSR_RETHINKDB_DB_NAME | Database name for the MSR 2.9 or MSR 3.1 RethinkDB. | ``dtr2`` |
| MSR_REPO_CSV | CSV file with all MSR 2.9 or MSR 3.1 repositories. | ``msr_repositories.csv`` |
| MSR_REPO_WITH_TEAM_ID_CSV | CSV with MSR 2.9 or MSR 3.1 repositories and their team IDs from ``repository_team_access``. | ``msr_repositories_with_team_id.csv`` |
| MSR_ORGANIZATIONS_WITH_TEAM_ID_CSV | CSV with MSR 2.9 or MSR 3.1 organization and team ID mappings from ``namespace_team_access``. | ``msr_organizations_with_team_id.csv`` |
| MSR_REPO_WITH_ENZI_TEAM_CSV | CSV with MSR 2.9 or MSR 3.1 repository and team mappings, used to import MSR 4 permissions. | ``msr_repositories_with_enzi_team.csv`` |
| MSR_ORGANIZATIONS_WITH_ENZI_TEAM_CSV | CSV with MSR 2.9 or MSR 3.1 organization and team mappings, used to import MSR 4 permissions. | ``msr_organizations_with_enzi_team.csv`` |
| MSR_ORGANIZATIONS_AND_REPO_WITH_ENZI_TEAM_CSV | CSV with MSR 2.9 or MSR 3.1 organisation or repository and team data used to map permissions to MSR 4 projects. | ``msr_organizations_and_repo_with_enzi_team.csv`` |
| MSR_PRUNING_POLICIES_CSV | CSV with all MSR 2.9 or MSR 3.1 pruning policies, imported as MSR 4 retention policies. | ``msr_pruning_policies.csv`` |
| MSR_POLL_MIRRORING_POLICIES_CSV | CSV with MSR 2.9 or MSR 3.1 pull mirroring policies imported to MSR 4. | ``msr_poll_mirroring_policies.csv`` |
| MSR_PUSH_MIRRORING_POLICIES_CSV | CSV with MSR 2.9 or MSR 3.1 push mirroring policies imported to MSR 4. | ``msr_push_mirroring_policies.csv`` |
| MSR_RETHINKDB_FETCH_PAGING_SIZE | Page size used when exporting MSR 2.9 or MSR 3.1 data to CSV. Helps limit memory usage. | ``1000`` |
| CSV_READER_CHUNK_SIZE | Chunk size used to read data from CSV files. Helps limit memory usage. | ``1000`` |
| HARBOR_PROJECTS_CSV | CSV containing all MSR 4 projects created. | ``harbor_projects.csv`` |
| HARBOR_GROUPS_CSV | CSV containing all MSR 4 user groups created. | ``harbor_groups.csv`` |
| HARBOR_PROJECT_MEMBER_CSV | CSV with MSR 4 group permissions attached to projects. | ``harbor_project_membebr.csv`` |
| HARBOR_RETENTION_POLICIES_CSV | CSV with MSR 4 retention policies attached to projects. | ``harbor_retention_policies.csv`` |
| HARBOR_IMMUTABLE_TAG_RULES_CSV | CSV containing all MSR 4 tag immutability rules set per project. | ``harbor_immutable_tag_rules.csv`` |
| HARBOR_POLL_MIRRORING_POLICIES_CSV | CSV containing MSR 4 pull replication policies migrated from the previous MSR version. | ``harbor_poll_mirroring_policies.csv`` |
| HARBOR_PUSH_MIRRORING_POLICIES_CSV | CSV containing MSR 4 push replication policies migrated from the previous MSR version. | ``harbor_push_mirroring_policies.csv`` |
| REUSE_ALREADY_FETCHED_DATA | Reuse previously fetched MSR 2.9 or MSR 3.1 and Enzi data, or download it again. | ``false`` |
| DRY_RUN | Simulates project creation by generating SQL statements without applying them. | ``false`` |
| CSV_DATA_DIR | Directory where CSV data is saved. | ``localhost`` |
| SQL_DATA_DIR | Directory where SQL files are generated. | ``./data/sql`` |
| EXTERNAL_SCRIPT_DIR | Directory for external scripts, including a background PostgreSQL keep-alive. | ``external`` |
| ENZI_TEAM_NAME_PREFIX_OR_SUFFIX | Specifies if organization name is added as a prefix (default) or suffix to teams. | ``prefix`` |
| IS_ENZI_TEAM_NAME_UNIQUE | Whether Enzi team names are unique. Set to ``true`` to avoid prefixing with organisation name. | ``false`` |
| HARBOR_DEFAULT_GROUP_ROLE | Sets default group role for projects' members in 1-to-1 migration mode. Valid values are: ``read-only``, ``read-write``, ``admin``. | None |
| HARBOR_DEFAULT_VISIBILITY | **DEPRECATED** Default visibility setting if MSR 2.9 or MSR 3.1 data is unavailable. | ``false`` |
| HARBOR_DEFAULT_TAG_IMMUTABILITY | **DEPRECATED** Default tag immutability setting if MSR 2.9 or MSR 3.1 data is unavailable. | ``false`` |
| HARBOR_DEFAULT_SCAN_ON_PUSH | **DEPRECATED** Default ``scanOnPush`` setting if MSR 2.9 or MSR 3.1 data is unavailable. | ``false`` |
| IS_MAPPING_ORGANIZATION_1_TO_1 | Maps MSR 2.9 and 3.1 ``organizations/repositories`` to MSR 4 ``projects/repositories`` 1-to-1. | ``false`` |
| MIGRATION_REPLICATION_RULE_PER_REPO | Creates migration replications rules per repository instead of per project in 1-to-1 migration mode. | ``false`` |
| MIGRATION_SOURCE_REGISTRY_URL | URL of the MSR 2.9 or MSR 3.1 source registry used for image migration. | None |
| MIGRATION_SOURCE_REGISTRY_NAME | Name saved on MSR 4 for the source registry used in migration. | None |
| MIGRATION_SOURCE_REGISTRY_ADMIN_USERNAME | Username to access the source MSR registry. | None |
| MIGRATION_SOURCE_REGISTRY_ADMIN_PASSWORD | Password or token for accessing the source MSR registry. | None |
| MIGRATION_SOURCE_REGISTRY_WITH_TLS_VERIFICATION | Defines whether to verify SSL certificates when connecting to the source registry. | None |
| MIGRATION_SOURCE_REGISTRY_REPLICATION_RULE_PREFIX | Prefix used for naming replication rules for easier management. | ``migration-rule-`` |
| MIGRATION_SOURCE_REGISTRY_TYPE | Registry type. Defaults to DTR unless the connection is broken. | ``DTR`` |
| REPLICATION_RULE_FLATTENING | Flattening level for all migrated images. | ``-1`` |
| REPLICATION_TRIGGER_CRON | Cron job schedule for triggering replication rules. Format: ``second minute hour day_of_month month day_of_week``. | ``0 0 1 * * *`` |

