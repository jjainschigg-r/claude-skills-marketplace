# PostgreSQL Helm Chart

**PostgreSQL helm chart** `#postgresql-helm-chart`

For a **Highly Available (HA)** deployment, a dedicated
**PostgreSQL Helm chart** can be used to deploy a PostgreSQL instance, ensuring
distribution across nodes for replication and enhanced reliability.

## NetworkPolicy

| Name | Namespace | Description |
|------|------------|--------------|
| **postgresql-ha-pgpool** | default | A NetworkPolicy for PostgreSQL pgpool declares an ingress port for exposure. |
| **postgresql-ha-postgresql** | default | A NetworkPolicy for PostgreSQL declares an ingress port for exposure. |

## PodDisruptionBudget

| Name | Namespace | Description |
|------|------------|--------------|
| **postgresql-ha-pgpool** | default | Helps maintain the availability of applications during voluntary disruptions like node drains or rolling updates. It specifies the minimum number or percentage of pods that must remain available during a disruption for postgres-pgpool pods. |
| **postgresql-ha-postgresql** | default | It's the same for PostgreSQL replicas. |
| **postgresql-ha-postgresql-witness** | default | It's the same for PostgreSQL witness. |

## ServiceAccount

| Name | Namespace | Description |
|------|------------|--------------|
| **postgresql-ha** | default | A Service Account configuration for PostgreSQL. |

## Secrets

| Name | Namespace | Description |
|------|------------|--------------|
| **postgresql-ha-pgpool** | default | A Service Account configuration for PostgreSQL pgpool. |
| **postgresql-ha-postgresql** | default | A Service Account configuration for PostgreSQL replicas. |

## ConfigMaps

| Name | Namespace | Description |
|------|------------|--------------|
| **postgresql-ha-postgresql-hooks-scripts** | default | pre-stop.sh and readiness-probe.sh. |

## Services

| Name | Namespace | Description |
|------|------------|--------------|
| **postgresql-ha-pgpool** | default | A Service configuration for PostgreSQL pgpool. |
| **postgresql-ha-postgresql-headless** | default | A Service configuration for PostgreSQL headless. |
| **postgresql-ha-postgresql** | default | A Service configuration for PostgreSQL replicas. |

## Deployments

| Name | Namespace | Description |
|------|------------|--------------|
| **postgresql-ha-pgpool** | default | A Deployment configuration for PostgreSQL pgpool. |

## StatefulSet

| Name | Namespace | Description |
|------|------------|--------------|
| **postgresql-ha-postgresql** | default | A StatefulSet configuration for PostgreSQL replicas. |
