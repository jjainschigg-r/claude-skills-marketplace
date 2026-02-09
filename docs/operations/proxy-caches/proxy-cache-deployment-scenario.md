# Proxy Cache Deployment Scenario

MSR caches running in different geographic locations can provide your users
with greater efficiency and shorten the amount of time that is needed to pull images
from MSR.

Consider a scenario in which you are running an MSR instance that is installed
in the United States, with a user base that includes developers located in the
United States, Asia, and Europe. The US-based developers can pull their images
from MSR quickly; however, the developers working in Asia and Europe have to contend with
unacceptably long wait times to pull the same images. You can address this
issue by deploying MSR caches in Asia and Europe, thus reducing the wait time
for the developers located in those areas.

The described MSR cache scenario requires three datacenters:

1. A US-based datacenter, running an MSR instance that is preferably configured for [high availability](../../installation/installation-with-high-availability/index.md).
2. An Asia-based datacenter running an MSR cache that is configured to fetch
   images from MSR.
3. A Europe-based datacenter running an MSR cache that is configured to fetch
    images from MSR.

For information on datacenter configuration, refer to
[Proxy cache prerequisites](proxy-cache-prerequisites.md).
