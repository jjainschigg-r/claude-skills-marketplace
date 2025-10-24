# Architecture

The Mirantis Secure Registry (MSR) Reference Architecture provides
comprehensive technical information on MSR, including component particulars,
infrastructure specifications, and networking and volumes detail.

- [Reference Architecture](architecture-reference.md)
    - [Consumers Layer](architecture-reference/consumers-layer.md)
    - [Fundamental Services Layer](architecture-reference/fundamental-services-layer.md)
    - [Data Access Layer](architecture-reference/data-access-layer.md)
    - [Integration](architecture-reference/integration.md)
- [Deployment](deployment/deployment.md)
    - [Deployment Options](deployment/deployment-options.md)
        - [All-in-one Deployment](deployment/all-in-one-deployment.md)
        - [High Availability Deployment](deployment/ha-deployment.md)
    - [Components Deployment](deployment/components-deployment.md)
        - [Web Portal](deployment/web-portal.md)
        - [Proxy (API Routing)](deployment/proxy.md)
        - [Core](deployment/core.md)
        - [Job Service](deployment/job-service.md)
        - [Registry](deployment/registry.md)
        - [Trivy](deployment/trivy.md)
        - [K-V Storage](deployment/k-v-storage.md)
        - [SQL Database](deployment/sql-database.md)
    - [Deployment Resources](deployment/deployment-resources.md)
        - [Harbor Helm Chart](deployment/harbor-helm-chart.md)
        - [Redis Helm Chart](deployment/redis-helm-chart.md)
        - [PostgreSQL Helm Chart](deployment/postgresql-helm-chart.md)
- [System Requirements](system-reqs.md)
- [Storage](storage.md)
- [Networking](networking.md)
- [Security](security/security.md)
    - [Kubernetes Security](security/kubernetes-security.md)
    - [Harbor Security](security/harbor-security.md)
    - [K-V Storage (Redis) Security](security/kv-storage-redis-security.md)
    - [DB Service (PostgreSQL) Security](security/db-service-security.md)
    - [Logging and Monitoring](security/logging-and-monitoring.md)
    - [Supply Chain](security/supply-chain.md)

