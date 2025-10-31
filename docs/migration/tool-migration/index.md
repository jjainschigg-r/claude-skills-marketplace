.. _tool-migration:

==============
Tool Migration
==============

This guide offers comprehensive, step-by-step instructions for migrating
artifacts from Mirantis Secure Registry (MSR) versions 2.9 and 3.1 to MSR 4
using the official migration tool.

The migration process is designed as an A/B operation. Your existing MSR
deployment remains active and unaffected while data is copied to a new MSR 4.x
instance. The migration tool runs independently on a separate host with
network access to both source and destination environments. This design
ensures operational continuity and limits risk to the current deployment.

**Key characteristics of the migration:**

- Migration is non-disruptive to your existing MSR system until the final
  cutover.
- Metadata are transferred using offline copies for consistency.
- The database backend changes from RethinkDB to PostgreSQL.
- Team names and repository paths may change. You will need to update pipelines
  accordingly.
- Image data migration can take significant amount of time dependent on
  attributes of the customer environment such as image and layer count and
  size, as well as network and storage capabilities. It may be scheduled
  to manage network and storage usage or run immediately.
- To minimize downtime during the final cutover, image migration can be
  repeated to reduce the size of the remaining delta before the last sync.

Before proceeding, review the following topics:

- :ref:`whats-new` for changes in MSR 4 behavior.
- :ref:`removed-features` and :ref:`what-to-expect-when-transitioning`
  especially if you use Swarm, custom image signing, or repository permissions.

If you have any questions, contact support for further guidance.

Tool Migration Contents
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Step
     - Description
   * - [What to Expect During the Migration](what-to-expect-when-transitioning.md)
     - Summarizes major behavioral and architectural changes between MSR
       versions. Review before planning your migration timeline.
   * - [Migration Prerequisites](migration-prerequisites.md)
     - Lists the technical requirements needed to run the migration tool
       successfully.
   * - [Install Migration Tool](install-migration-tool.md)
     - Explains how to download, verify, and install the migration tool on
       your migration host.
   * - [Database Access Configuration](db-configuration.md)
     - Describes how to configure and access the source and destination
       database environments.
   * - [Configure Migration Settings](configure-migration-settings.md)
     - Explains how to configure your target environment.
   * - [Perform Migration](perform-tool-migration.md)
     - Outlines how to run the migration tool to export data from the source
       MSR and import it into the MSR 4 deployment.
   * - [Migrate Projects](partial-tool-migration/migrate-projects.md)
     - Describes how to migrate projects.
   * - [Migrate Permissions](partial-tool-migration/migrate-permissions.md)
     - Describes how to migrate permissions.
   * - [Migrate Push and Poll Mirroring Policies](partial-tool-migration/migrate-push-poll-mirroring-policies.md)
     - Describes how to migrate push and poll mirroring policies.
   * - [Validate Migration Data](validate-migration-data.md)
     - Details optional steps to confirm that repositories, metadata, and user
       configurations were migrated correctly.
   * - [Post-Migration Configuration](tool-configure-migration.md)
     - Provides guidance on updating pipelines, credentials, and access
       controls for the new MSR system.
   * - [Post-Migration Cleanup](clean-up-after-migration.md)
     - Lists cleanup tasks, including retiring the old MSR deployment and
       releasing temporary resources.
   * - [Migration Tool Reference](reference-migration-tool/index.md)
     - Contains command-line options and configuration
       parameters for the migration tool.
   * - [Migration Tool Release Notes](migration-tool-release-notes/index.md)
     - Contains migration tool release notes.
