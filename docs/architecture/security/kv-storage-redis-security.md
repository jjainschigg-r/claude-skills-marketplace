# K-V Storage (Redis) Security

Redis is an in-memory data store, and securing its configuration and
access is critical to maintaining the integrity of cached data. While Redis
is often part of MSR 4 installations, it’s important to note that in some
cases, a corporate key-value (K-V) storage solution may be used instead. In
such scenarios, the responsibility for securing the K-V storage is transferred
to the corresponding corporate service team, which must ensure the storage is
appropriately configured and protected against unauthorized access or data
breaches.

## Authentication

To secure Redis, it is essential to enable authentication by setting a strong
password using the `requirepass` directive in the Redis configuration. This
ensures that only authorized clients can access the Redis instance.

Additionally, TLS/SSL encryption should be enabled to secure communication
between Redis clients and the Redis server. This helps protect sensitive data
in transit, preventing unauthorized interception or tampering of the
information being exchanged.

## Network Security

Since the placement of the K-V Storage service may vary—whether cohosted on
the same cluster, accessed from another cluster, or deployed entirely
separately—it is crucial to bind Redis to a private network to prevent
unauthorized external access. Redis should only be accessible from trusted
sources, and access should be restricted to the minimum necessary.

To achieve this, Kubernetes Network Policies should be used to enforce strict
controls on which pods can communicate with the Redis service. This ensures
that only authorized pods within the cluster can access Redis, further
minimizing the attack surface and enhancing security.

## Redis Configuration

To enhance security, the `CONFIG` command should be disabled in Redis to
prevent unauthorized users from making changes to the Redis configuration.
This reduces the risk of malicious users altering critical settings.

Additionally, for Redis instances that should not be exposed to the internet,
consider enabling Redis' protected mode. This mode ensures that Redis only
accepts connections from trusted sources, blocking any unauthorized access
attempts from external networks.
