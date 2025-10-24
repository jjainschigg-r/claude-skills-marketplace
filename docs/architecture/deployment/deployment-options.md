# Deployment Options

MSR 4 offers two primary deployment options, each with the flexibility to
accommodate various modifications. For instance, in the all-in-one deployment,
local storage can be replaced with shared storage, and databases or key-value
stores can be made remote. This adaptability allows MSR 4 to support various
configurations and deployment scenarios.

However, to establish a standardized approach, we propose two primary
deployment options tailored for specific use cases:

* **All-in-One on a Single Node** – Ideal for testing and development
* **Multi-Node HA Deployment** – Designed for production environments

Since MSR 4 operates as a Kubernetes workload, all of its core services
run as Kubernetes pods. As a result, we consider a worker node as the minimum
footprint for an all-in-one MSR 4 deployment, and three workers as the minimum
footprint for an HA deployment. Master nodes, however, are not included in
this count, giving you the flexibility to design and deploy the underlying
Kubernetes cluster according to your needs.