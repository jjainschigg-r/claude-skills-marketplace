# Installation Guide

Mirantis Secure Registry (MSR) supports two installation scenarios designed to
meet most customer needs:

- [High availability installation](installation-with-high-availability/index)  
- [Single host installation](msr-docker-install/index)

The following comparison highlights key differences to help you choose the most
appropriate option for your environment.


| **Installation Scenario** | **Detail** |
|----------------------------|-------------|
| **High Availability** | Deployment of MSR in a high availability configuration on Kubernetes using Helm charts. <br><br> **Benefits** <br> - Provides the highest resiliency and uptime. <br> - Leverages Kubernetes orchestration with three or more nodes running in an active-active configuration. <br> - Includes guidance for installing PostgreSQL and Redis in a high availability configuration. <br><br> **Use case** <br> Production environments of medium to large enterprises, where uptime is critical. |
| **Single host using Docker Compose** | High availability is not supported. Thus, if the MSR instance becomes unavailable, there is no orchestrator to provide redundancy. <br><br> **Benefits** <br> - Does not require Kubernetes or Helm/OCI Charts. <br><br> **Use case** <br> Non-production environments, or smaller enterprises or office sites. Also suitable for non-Kubernetes environments. |

Some organizations may have unique infrastructure requirements or prefer
custom deployment strategies that extend beyond the scope outlined here.  
While Mirantis supports a wide range of use cases, official support is limited
to the configurations described above.

Contact [Mirantis Professional Services](https://www.mirantis.com/company/services-descriptions/)  
for assistance with specialized installations or custom deployments.

!!! note

    The full set of installation options for MSR follows
    [the Harbor upstream documentation](https://goharbor.io/docs/2.10.0/install-config/).

### Installation Topics

- [System Requirements](msr-system-reqs)
- [Prepare MKE for MSR Installation](prepare-mke-for-msr-install)
- [Installation with High Availability](installation-with-high-availability/index)
- [Single Host Installation](msr-docker-install/index)




