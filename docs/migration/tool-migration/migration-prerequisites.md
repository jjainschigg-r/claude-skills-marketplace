# Migration Prerequisites

Before you begin the migration process, complete the following steps to ensure
a smooth and secure transition:

**Administrative access**  

Confirm that you have administrative access to both source (MSR 2.9 and MSR
3.1) and target (MSR 4.x) environments to read all source data and configure
the destination from your migration workstation.

**Backup**  

Perform a full backup of existing data to prevent any data loss in case of a
misstep:

- [MSR 2.9 backup](https://docs.mirantis.com/msr/2.9/ops/disaster-recovery/create-a-backup.html)
- [MSR 3.1 backup](https://docs.mirantis.com/msr/3.1/ops/disaster-recovery/create-a-backup.html)

**MSR 4 installation** 

Complete the following tasks to prepare the target environment for migration:

- Verify that the system meets all prerequisites.  
  See [Prerequisites](../../installation/msr-system-reqs.md).
- Install MSR 4 using the steps in the [High availability installation](../../installation/installation-with-high-availability/index.md)  
- Configure authentication as described in the [Authentication Configuration](../../operations/authentication-configuration/authentication-configuration.md).

**Storage**  

Ensure that the target system has sufficient storage capacity to accommodate
all migrated artifacts. The storage must be separate from MSR 2.9 or MSR 3.1.

- The PostgreSQL database must have enough space for the following:
    - Current Enzi RethinkDB
    - Current MSR RethinkDB
    - Plus 25% overhead
- The BLOB storage must have enough space for the following:
    - Current used storage
    - Extra space for new images, based on your requirements
    - Plus at least 5% overhead for working space

**Migration workstation** 

Set up a dedicated migration workstation to manage the migration process.  
This workstation must have:

- Linux operating system.
- Installed the following tools:
    - A container runtime, either:
        - [Docker Desktop](https://docs.docker.com/desktop/)
        - [Mirantis Container Runtime (MCR)](https://docs.mirantis.com/mcr/current/install.html)
        - [Docker CE](https://docs.docker.com/engine/install/)
    - [RethinkDB](https://rethinkdb.com/docs/install/) version 2.4.4
- Access to the following databases:
    - PostgreSQL — configured as part of the MSR 4 deployment.
    - Enzi — included in MSR 2.9 (through MKE) or directly in MSR 3.1.
    - RethinkDB — used in both MSR 2.9 and MSR 3.1 deployments.

