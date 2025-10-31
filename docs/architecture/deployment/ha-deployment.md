# High Availability Deployment


The **Highly Available (HA) Deployment** of MSR 4 is distributed across three
or more worker nodes, ensuring resilience and reliability through multiple
service instances. For installation guidance, refer to
the [installation-with-high-availability](../../installation/installation-with-high-availability/index).

A key aspect of this deployment is that **Job Service** and **Registry**
utilize a shared volume, which should be backed by a non-local, shared file
system or external storage cluster, such as **Ceph (CephFS)**. Additionally,
**Redis** and **PostgreSQL** run in a replicated mode within this example,
co-hosted on the same worker nodes as MSR 4’s core services. However, it is
also possible to integrate existing corporate Redis and PostgreSQL instances
outside of these nodes, leveraging an enterprise-grade key-value store and
database infrastructure.

The following diagram illustrates the service placement in an HA deployment.
Dashed boxes indicate potential additional replicas for certain services. As a
reference, we recommend deploying at least **two instances** of **Portal, Core,
Job Service, Registry, and Trivy**—though this number can be adjusted based on
specific requirements, workload, and use cases. These services are not
quorum-based.

While the number of replicas for these services can scale as needed,
**Redis and PostgreSQL must always have a minimum of three replicas** to ensure
proper replication and fault tolerance. This requirement should be carefully
considered when planning a production deployment. Redis and PostgreSQL are
quorum-based services, so the number of replicas should always be odd,
specifically 1, 3, 5, and so on.

The reference HA deployment of an MSR 4 is presented in the following diagram.

![HA Deployment](../../_diagrams/ha-deployment.svg)
