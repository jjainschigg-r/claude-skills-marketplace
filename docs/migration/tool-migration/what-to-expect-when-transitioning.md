# What to Expect During the Migration

Mirantis Secure Registry (MSR) 4 represents a significant evolution in managing
container images and associated metadata. The transition introduces a new
architecture centered around projects, improved security models,
and streamlined policy-based configuration.

The transition may take a significant amount of time, depending on
your system and data volume. However, your current MSR instance may remain
fully operational throughout the migration, allowing you to continue work
without interruption.

Most core data will be transferred automatically, but some settings and
features require manual reconfiguration after migration. Understanding what is
and is not migrated will help you plan the migration effectively.

## What is migrated

During migration, MSR automatically transfers key content and configurations,
preserving the core of your container registry environment:

![Table to table migration](../../_diagrams/table-to-table-migration.drawio.svg)

- **Repositories**

  Repositories from MSR 2.9 and MSR 3.1 are migrated as projects in MSR 4.

- **Images**

  All image data, including associated metadata and tags.

- **Permissions**

  Permissions are mapped into the MSR 4 project-based access control system as
  shown in the diagram below:

  ![Permissions migration](../../_diagrams/permissions-migration.drawio.svg)

- **Push and Poll Mirroring Policies**

  Mirroring policies are exported and can be manually triggered or rescheduled.

- **Roles**

  LDAP-based user accounts assigned to project roles are migrated.

- **Helm Charts**

  Chart packages stored in the registry are preserved.

## What is not migrated

The following items must be recreated or reconfigured after the migration:

- **Audit Logs**

  Set up new logging and compliance monitoring mechanisms.

- **API Updates**

  Some endpoints have changed; update as needed to maintain
  automation and tooling compatibility.

- **Authentication**

  SAML support is removed. Use LDAP or OIDC instead.

- **Certificate Management**

  Define retention and cleanup rules in the new system.

- **Garbage Collection Settings**

  Manually reconfigure garbage collection policies in MSR 4.

- **Image Tag Retention**

  Reconfigure rules to manage image lifecycle in MSR 4.

- **Labels**

  Update image and repository labels.

- **Local Groups and Users**

  Manually recreate any local groups and users that are defined only in Enzi
  and not managed by an external identity provider.

- **Project Permissions**

  Depending on your permission settings you may need
  to recreate user and team access rules using MSR 4's project-level model.

- **Project Visibility**

  Set project visibility manually for each project.
  MSR 4 does not support mixed visibility within a single organization
  as shown in the diagram below:

  ![MSR visibility scanning settings](../../_diagrams/msr-visibility-scanning-settings.drawio.svg)

- **Pruning Policies**

  Configure pruning policies manually.
  These settings cannot be imported directly, as MSR 4 uses reversed logic
  when evaluating pruning rules.

- **Scanning Settings**

  Enable and configure Trivy to support image vulnerability scanning in MSR 4.

- **Signed Images**

  Existing image signatures are not preserved. They need to be re-signed using
  Cosign.

- **Tag Immutability**

  Tag immutability is configured at the project level, and must be set up
  manually for each relevant project.
  However, if a repository had tag immutability previously set to ``false``,
  there is no need to apply a new tag immutability rule after the migration.

- **Tokens**

  Tokens from previous versions are not preserved. Generate new
  tokens in MSR 4

- **Webhooks**

  Recreate and redirect webhooks to MSR 4 endpoints.

## Removed features

The following features are not supported in MSR 4:

- **Swarm Support**

  While MSR 4 no longer supports Swarm HA clusters,
  single-instance deployments remain viable for Swarm users, though not
  recommended for production use.
  For more information, visit
  [Install MSR on a Single Host using Docker Compose](../../installation/msr-docker-install/index.md).

- **Promotion Policies**

  Automate promotion workflows through updated CI/CD pipelines.
