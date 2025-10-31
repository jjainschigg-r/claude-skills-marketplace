## Manual Migration Prerequisites

Before you begin the migration process, complete the following
steps to ensure a smooth and secure transition:

**Administrative access**

Confirm that you have administrative access to both source
(MSR 2.9 and MSR 3.1) and target (MSR 4.x) environments to read all source
data and configure the destination from your migration workstation.

**Backup**

 Perform a full backup of existing data to prevent any data loss in case of a
 misstep:

* [MSR 2.x backup](https://docs.mirantis.com/msr/2.9/ops/disaster-recovery/create-a-backup.html)  
* [MSR 3.x backup](https://docs.mirantis.com/msr/3.1/ops/disaster-recovery/create-a-backup.html)

**MSR 4 installation**

Complete the following tasks to prepare the target environment for
migration:

- Verify that the system meets all prerequisites.
  See [Prerequisites](../../msr-system-reqs.md).
- Install MSR 4 using the steps in the
  [Install MSR with High Availability](../../installation-with-high-availability/index.md).
- Configure authentication as described in the
  [Authentication Configuration](../../../operations/authentication-configuration/authentication-configuration.md).

**Storage**

Ensure that the target system has sufficient storage capacity to accommodate
all migrated artifact. The storage must be separate from MSR 2.9 or MSR 3.1.

* The PostgreSQL database must have enough space for the following:

  * Current MSR RethinkDB
  * Plus 25% overhead

* The BLOB storage must have enough space for the following:

  * Current used storage
  * Extra space for new images, based on your requirements
  * Plus at least 5% overhead for working space





