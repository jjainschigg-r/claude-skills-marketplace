# Manual Migration

This guide provides instructions for performing a **manual migration** from
MSR 2.9 or 3.1 to MSR 4. Manual migration is recommended for small
environments or limited migration scopes because it transfers repository data
only. Permissions and policies are not included.
Manual migration is easy to implement and does not require additional tools.

Use this guide if you need to preserve your existing registry content and
organizational layout while maintaining full control over each migration
step.

Before proceeding, review the following topics:

- [What's New](../../../whats-new/index.md) for changes in MSR 4 behavior.
- [Removed Features](../../../whats-new/removed-features.md) 
  especially if you use Swarm, custom image signing, or repository permissions.

## Manual Migration Contents

| Step | Description |
|------|-------------|
| [Migration prerequisites](manual-migration-prerequisites) | Lists the technical requirements needed to run the manual migration successfully. |
| [Perform migration](migrate-msr) | Outlines how to run the manual migration to export repository data from the source MSR and import it into the MSR 4 deployment. |
| [Post-migration configuration](manual-configure-migration) | Provides guidance on updating pipelines, credentials, and access controls for the new MSR system. |

