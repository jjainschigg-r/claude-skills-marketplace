# Migrate Permissions

In MSR 4, repositories and organizations are migrated as projects. As a
result, permissions are added at the organization project level, and do not
follow the same inheritance structure as in earlier MSR versions. See
[What to Expect During the Migration](../what-to-expect-when-transitioning.md)
for detailed description.

!!! warning
    If the permissions target paths are business-critical, you should migrate
    them manually to ensure accuracy and avoid disruptions.

To migrate permissions to MSR 4, you must transfer:

- Team access at the repository level.
- Team access at the organization (namespace) level.

## Migration steps

1. Ensure that the MSR 4 authorization is properly configured to enable
   **Groups** section in the main menu. Refer to the
   [Authentication Configuration](../../../operations/authentication-configuration/authentication-configuration.md)
   for setup instructions.

2. Optional. Configure permission migration in the `config/config.env` file:

    1. Specify whether the organization name is added as a prefix (default) or
       suffix to team names by setting the value to `prefix` or `suffix` in
       the configuration.

       ```bash
       ENZI_TEAM_NAME_PREFIX_OR_SUFFIX=<SET-PREFIX-OR-SUFFIX>
       ```

    2. If all group names are already unique across the environment, you can
       prevent MSR from appending the organization name during import by
       setting:

       ```bash
       IS_ENZI_TEAM_NAME_UNIQUE=True
       ```

    !!! warning
        Do not modify these environment variables after the migration begins.
        Changing them mid-process may cause duplicate groups or inconsistent
        team references.

3. Export groups data from MSR and Enzi, and import it into MSR 4:

    ```bash
    docker run --rm \
        -v ./sql:/app/data/sql \
        -v ./csv:/app/data/csv \
        -v ./config:/app/config \
        --network host \
        registry.mirantis.com/msrh/migrate:latest \
        poetry run migration --groups
    ```

4. Confirm that group data appears under **Groups** in the MSR web UI.

    !!! note
        If the **Groups** section is missing from the main menu, LDAP
        may not be configured. See [LDAP Authentication](../../../operations/authentication-configuration/ldap-authentication.md)
        for instructions on how to set up user authentication.

5. Migrate team permissions for namespaces and repositories:

    ```bash
    docker run --rm \
        -v ./sql:/app/data/sql \
        -v ./csv:/app/data/csv \
        -v ./config:/app/config \
        --network host \
        registry.mirantis.com/msrh/migrate:latest \
        poetry run migration --members
    ```

6. In the MSR web UI, navigate to **Projects**, select a project,
   and click the **Members** tab to verify that team permissions have
   been correctly applied.
