# All-in-one Deployment

The **All-in-One Deployment** consolidates all services onto a single worker
node, making it the most straightforward way to deploy MSR 4\. In this setup,
all services run as single-instance components without a high availability (HA)
or replication. Such an approach is not applicable for production usage but is
useful for testing or Proof of Concept. Refer to the installation
guidance in the MSR 4 documentation
[using a docker compose](../../installation/msr-docker-install/msr-docker-install.md)
or you can use a helm chart approach (that is mentioned in
[HA deployment variant](../../installation/installation-with-high-availability/installation-with-high-availability.md)
instead, but scaling replicas to 1 in variables configuration.

While this deployment effectively showcases MSR 4's capabilities and
functionality, it is not intended for production use due to its lack of
redundancy. Instead, it is a lightweight option suitable for demonstrations,
training, testing, and development.

The following diagram illustrates a single worker node running all
MSR 4-related services.

![Worker Node](../../_diagrams/single-node.svg)

There are two methods for installing the all-in-one MSR 4:

1. Using Kubernetes Helm
2. [Using Docker Compose](../../installation/msr-docker-install/msr-docker-install.md)

Each approach has its own advantages. The Kubernetes method is similar to
High Availability (HA) mode and allows for easy scaling from a single-node
to a multi-node deployment. On the other hand, Docker Compose is ideal for
those not using Kubernetes in their infrastructure, enabling them to
leverage MSR 4's capabilities by running all services in containers.