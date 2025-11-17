# Differences between MSR versions

Mirantis Secure Registry (MSR) 4 is now based on CNCF Harbor, bringing
increased stability, an expanded feature set, and a broader ecosystem of
integrations. This document outlines key changes and considerations between
MSR versions.

For more information, refer to the full documentation or contact Mirantis.

## API

API and webhook behavior has been updated to reflect Harbor’s implementation.
These changes support better compatibility with ecosystem tools and simplify
DevOps automation.

## Architecture

MSR 4 introduces a Kubernetes-native architecture that is more scalable and
easier to operate than the legacy Swarm-based design. Legacy components such
as RethinkDB and embedded services have been removed or refactored, improving
performance and simplifying upgrades.

## Artifact Management and CI/CD Pipelines

**Helm Support**

Helm chart support in MSR 4 is now OCI-compliant. Charts are stored and
managed as OCI artifacts rather than through a dedicated Helm repository. Use
OCI commands:

``` bash
helm push oci:///
helm pull oci:///
```

The `helm search repo` command is no longer supported. Instead, use the
Harbor UI or the forthcoming Harbor CLI.

This change improves compatibility with OCI tooling but may require minor
adjustments to traditional Helm workflows.

**Promotion Policies**

Promotion policies are not supported in MSR 4. You must adapt CI/CD pipelines
to reflect this change.

## Authentication and Access Control

**OpenID Connect (OIDC) Authentication**

MSR 4 replaces legacy SAML support with OpenID Connect (OIDC). OIDC is more
suitable for modern applications due to its lightweight protocol, better
mobile and microservices compatibility, and broader support across enterprise
Identity Providers (IdPs) such as Azure AD, Okta, Google Identity Platform,
Amazon Cognito, Ping Identity, IBM Security Verify, OneLogin, and VMware
Workspace ONE.

Customers using SAML must configure an IdP that supports SAML-to-OIDC bridging
(for example, Okta, Keycloak, Azure AD).

**Role-Based Access Control (RBAC)**

MSR 4 removes the legacy Teams and Enzi components. You must now add users
manually to projects to configure access. Group-based access is supported only
through AD Groups, which requires integration with LDAP/AD and OIDC.

For more information, refer to [Authentication Configuration](../operations/authentication-configuration/authentication-configuration.md).

## Database

MSR 4 replaces the legacy RethinkDB backend with PostgreSQL, an
industry-standard relational database known for stability and scalability.
This transition improves data consistency, query performance, and operational
resilience in high-demand environments. PostgreSQL also simplifies
administrative tasks and aligns MSR 4 with enterprise database best practices.

## Deployment and Infrastructure Support

**Swarm Support and HA**

Upstream Harbor does not support Swarm. You can deploy MSR 4 as a single-node
instance using Docker Compose. High availability (HA) requires Kubernetes.
Most customers with HA needs already have Kubernetes and can use it for
production deployments.

**Backup and Disaster Recovery**

MSR 2 and MSR 3 included built-in backup capabilities. MSR 4 requires
external backup management using **Velero**, an open-source tool widely used
in enterprise Kubernetes environments, including Azure.

Velero supports backup and restore, but it requires a Kubernetes-based
deployment. Unlike earlier versions, MSR 4 does not provide native backup
functionality.

For more information, refer to [Backup Guide](../backup/index.md).

## Upgrades

All MSR 4 upgrades are supported as in-place operations. You no longer need to
use disruptive blue-green or backup-restore strategies. Administrators can
apply version updates with less downtime and lower operational complexity.

For more information, refer to [Upgrade Guide](../operations/upgrade.md).

## Job Runner for Background Task Execution

The MSR 4 job runner, inherited from Harbor’s job service, provides a
modernized mechanism for executing background tasks such as garbage
collection, replication, scanning, and retention.

Compared to MSR 2, the new job runner supports distributed execution,
automatic retry policies, improved error reporting, and detailed job history.
These features improve observability and reliability for registry operations.

## Long Repository Names (256 Characters)

MSR 4 supports repository path lengths up to 256 characters, aligning with
OCI registry specifications. This support enables deeper project namespaces
and more descriptive naming, which are common in enterprise CI/CD pipelines.

## Migration

CNCF MSR 4 supports mirroring-based migration from MSR 2 and MSR 3. The
following elements transfer automatically:

* Repositories
* Images
* Permissions
* Push and Pull Mirroring Policies
* Roles
* Helm Charts

This migration method uses **mirroring**, which reduces the need for extended
downtime or manual migration tools like MMT. MSR 2 or 3 can remain active
alongside MSR 4, allowing teams to update pipelines while maintaining system
availability.

For more information, refer to [Migration Guide](../migration/index.md).

## Summary

Migrating to MSR 4 improves performance, simplifies upgrades, and expands
feature capabilities. However, functional changes may require you to adjust
authentication, promotion workflows, and backup strategies.

Review the changes outlined in this document and plan your migration
accordingly.
