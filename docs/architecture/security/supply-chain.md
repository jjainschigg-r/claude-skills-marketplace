# Supply Chain

Mirantis hosts and controls all sources of MSR 4 that are delivered to the
environment, ensuring a secure supply chain. This controlled process is
essential for preventing any malware injections or unauthorized modifications
to the system infrastructure. By maintaining tight control over the software
delivery pipeline, Mirantis helps safeguard the integrity and security of the
environment from the outset.

## Platform Sources

Helm charts and images used for building MSR 4 are hosted and maintained by
Mirantis. These resources are regularly scanned and updated according to
Mirantis' corporate schedule, ensuring that they remain secure and up-to-date.

To ensure the security of the environment, the customer must establish a secure
communication channel between their infrastructure and Mirantis' repositories
and registries. This can be achieved through specific proxy configurations,
which ensure a direct and controlled connection, minimizing the risk of
unauthorized access or data breaches.

## Patch Management

Regularly applying security patches to all components—such as Harbor, Redis,
PostgreSQL, and Kubernetes—is essential to mitigate vulnerabilities promptly
and maintain a secure environment. Keeping components up-to-date with the
latest security patches helps protect the system from known threats and
exploits.

It is also important to monitor security bulletins and advisories for updates
and fixes relevant to your stack. Staying informed about new vulnerabilities
and their corresponding patches allows for quick action when necessary.

While Mirantis handles the security of sources delivered from its repositories
and registries, third-party integrations require additional security measures.
These must be secured with proper scanning and a regular patching schedule to
ensure they meet the same security standards as internal components, reducing
the risk of introducing vulnerabilities into the environment.

## Compliance Standards

Implementing audit trails is essential for tracking and monitoring system
activity, enabling you to detect and respond to potential security incidents.
Audit logs should capture all critical events, such as access attempts,
configuration changes, and data modifications, ensuring accountability and
traceability.

Additionally, sensitive data must be encrypted both at rest and in transit.
Encryption at rest protects stored data from unauthorized access, while
encryption in transit ensures that data exchanged between systems remains
secure during transmission. This dual-layer approach helps safeguard sensitive
information from potential breaches and attacks.

Mirantis actively checks the sources for Common Vulnerabilities and Exposures
(CVEs) and malware injections. This proactive approach ensures that the
software and components delivered from Mirantis repositories are thoroughly
vetted for security risks, helping to prevent vulnerabilities and malicious
code from being introduced into the environment. By conducting these checks,
Mirantis maintains a secure supply chain for MSR 4 deployments.

Ensure that the environment adheres to relevant compliance standards such as
GDPR, HIPAA, or PCI-DSS, depending on your use case.
