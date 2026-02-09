# Proxy Caches

The time needed to pull and push images is directly influenced by the geographic distance
between your users and that of your MSR deployment. This is
because the files need to traverse the physical space and cross multiple networks.
You can, however, deploy MSR caches at different geographic locations to add greater
efficiency and shorten user wait time. You can also use the proxy cache feature to
mitigate any issues that can rise due to the [Docker Hub’s rate limit policy](https://www.docker.com/blog/november-2024-updated-plans-announcement/).

You can use MSR proxy caches to:

- Accelerate image pulls for users in a variety of geographical regions.
- Manage user permissions from a central location.
- Avoid the Docker Hub rate limit.

MSR system administrators can set up a proxy cache project in another instance of MSR that links
to an MSR registry through a predefined registry endpoint. This special project
functions much like a standard Harbor project, with the key difference being
that you can only pull images from it, not push images to it.
To take advantage of the MSR proxy cache, update your pull commands, container
manifests, and CI/CD workloads to retrieve images from the proxy cache project
rather than directly from the original registry.

!!! note

    Avoid using caches if your users need to push images faster or if you want
    to implement region-based RBAC policies. Instead, deploy multiple MSR
    clusters and apply mirroring policies between them. For further details,
    refer to [Configure Replication](../configuring-replication.md).
