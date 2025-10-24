# Redis Helm Chart

For a **Highly Available (HA)** deployment, a dedicated **Redis Helm chart**
can be used to deploy a Redis instance, ensuring distribution across nodes for
replication and enhanced reliability.

## NetworkPolicy

| Name | Namespace | Description |
|------|------------|--------------|
| **redis** | default | A NetworkPolicy for Redis declares an ingress port for exposure. |

## PodDisruptionBudget

| Name | Namespace | Description |
|------|------------|--------------|
| **redis-master** | default | Helps maintain the availability of applications during voluntary disruptions like node drains or rolling updates. It specifies the minimum number or percentage of pods that must remain available during a disruption for redis-master pods. |
| **redis-replicas** | default | It's the same for replica pods. |

## ServiceAccount

| Name | Namespace | Description |
|------|------------|--------------|
| **redis-master** | default | Service account configuration for redis-master. |
| **redis-replicas** | default | Service account configuration for redis-replicas. |

## Secrets

| Name | Namespace | Description |
|------|------------|--------------|
| **redis** | default | It contains a Redis password. |

## ConfigMaps

| Name | Namespace | Description |
|------|------------|--------------|
| **redis-configuration** | default | Master.conf, redis.conf, replica.conf. |
| **redis-health** | default | Multiple .sh files with health checks. |
| **redis-scripts** | default | start-master.sh and start-replica.sh. |

## Services

| Name | Namespace | Description |
|------|------------|--------------|
| **redis-headless** | default | Service for redis-headless. |
| **redis-master** | default | Service for redis-master. |
| **redis-replicas** | default | Service for redis-replica. |

## StatefulSet

| Name | Namespace | Description |
|------|------------|--------------|
| **redis-master** | default | StatefulSet configuration for redis-master. |
| **redis-replicas** | default | StatefulSet configuration for redis-replica. |
