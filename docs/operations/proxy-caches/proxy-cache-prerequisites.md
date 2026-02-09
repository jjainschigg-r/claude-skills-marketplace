# Proxy Cache Prerequisites

Before deploying an MSR proxy cache in a datacenter:

- Set up a new MSR instance on a supported platform:
    * [Kubernetes](../../installation/installation-with-high-availability/index.md)
    * [Docker Compose](../../installation/msr-docker-install/index.md)
- Obtain access to the cluster that is running the MSR registry in your data center.
- Either join the nodes into a cluster or deploy a standalone proxy cache.
- Dedicate one or more nodes for running the MSR proxy cache.
- Configure your firewall rules to ensure that your users have access to the proxy cache.
