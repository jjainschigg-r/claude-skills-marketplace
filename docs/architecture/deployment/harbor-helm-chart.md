# Harbor Helm Chart

Note that the type and number of resources may vary based on the
deployment configuration and the inclusion of additional services.

## Secret

| Name | Namespace | Description |
|------|------------|--------------|
| **msr-4-harbor-core** | default | Stores data needed for integration with other fundamental and data storage services and API-related keys, certificates, and passwords for DB integration. |
| **msr-4-harbor-database** | default | Contains a DB password. |
| **msr-4-harbor-jobservice** | default | Contains a job service secret and a registry credential password. |
| **msr-4-harbor-nginx** | default | Contains TLS certs for API proxy. |
| **msr-4-harbor-registry** | default | Contains a registry secret and Redis password. |
| **msr-4-harbor-registry-htpasswd** | default | Contains the registry password. |
| **msr-4-harbor-registryctl** | default | Contains registry-controller sensitive configuration. |
| **msr-4-harbor-trivy** | default | Contains Trivy reference to Redis K-V storage. |

## ConfigMap

| Name | Namespace | Description |
|------|------------|--------------|
| **msr-4-harbor-core** | default | Stores configuration for core services, defining integrations, databases, URLs, ports, and other non-sensitive settings (excluding passwords, keys, and certs). |
| **msr-4-harbor-jobservice-env** | default | Job service configuration parameters such as URLs, ports, users, proxy configuration, etc. |
| **msr-4-harbor-jobservice** | default | A job service config.yaml. |
| **msr-4-harbor-nginx** | default | Nginx.config. |
| **msr-4-harbor-portal** | default | Portal virtual host HTTP config. |
| **msr-4-harbor-registry** | default | Registry config.yaml. |
| **msr-4-harbor-registryctl** | default | Register controller configuration. |

## PersistentVolumeClaim

| Name | Namespace | Description |
|------|------------|--------------|
| **msr-4-harbor-jobservice** | default | PVC for job service. |
| **msr-4-harbor-registry** | default | PVC for registry. |

## Service

| Name | Namespace | Description |
|------|------------|--------------|
| **msr-4-harbor-core** | default | Service for Core. |
| **msr-4-harbor-database** | default | Service for DB. |
| **msr-4-harbor-jobservice** | default | Service for Job Service. |
| **harbor** | default | Service for Harbor. |
| **msr-4-harbor-portal** | default | Service for Portal. |
| **msr-4-harbor-redis** | default | Service for k-v Redis. |
| **msr-4-harbor-registry** | default | Service for Registry. |
| **msr-4-harbor-trivy** | default | Service for Trivy. |

## Deployment

| Name | Namespace | Description |
|------|------------|--------------|
| **msr-4-harbor-core** | default | A Deployment configuration for Core. |
| **msr-4-harbor-jobservice** | default | A Deployment configuration for Job Service. |
| **msr-4-harbor-nginx** | default | A Deployment configuration for Proxy. |
| **msr-4-harbor-portal** | default | A Deployment configuration for Portal. |
| **msr-4-harbor-registry** | default | A Deployment configuration for Registry. |

## ReplicaSet

| Name | Namespace | Description |
|------|------------|--------------|
| **msr-4-harbor-core** | default | A ReplicaSet configuration for Core. |
| **msr-4-harbor-jobservice** | default | A ReplicaSet configuration for Job Service. |
| **msr-4-harbor-nginx** | default | A ReplicaSet configuration for Proxy. |
| **msr-4-harbor-portal** | default | A ReplicaSet configuration for Portal. |
| **msr-4-harbor-registry** | default | A ReplicaSet configuration for Registry. |

## StatefulSet

| Name | Namespace | Description |
|------|------------|--------------|
| **msr-4-harbor-database** | default | A StatefulSet configuration for DB. |
| **msr-4-harbor-redis** | default | A StatefulSet configuration for k-v. |
| **msr-4-harbor-trivy** | default | A StatefulSet configuration for Trivy. |

