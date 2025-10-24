# Harbor Security

Harbor serves as the container registry in MSR 4, making its security
crucial for safeguarding both container images and their associated
metadata. Ensuring proper security measures are in place helps protect
against unauthorized access, image tampering, and potential vulnerabilities
within the registry.

## Authentication and Authorization

It is essential to enable Harbor's authentication mechanisms, such as
OpenID Connect (OIDC), LDAP, or local accounts, to manage access to
repositories and projects effectively.

For testing and development purposes, using local accounts may suffice, as
seen in deployment examples, since the solution is not intended for
production. However, for production environments, integrating corporate
OAuth or Active Directory (AD)/LDAP with MSR 4 is necessary to enable
Single Sign-On (SSO) capabilities, enhancing security and user management.

Additionally, leveraging Role-Based Access Control (RBAC) within Harbor
allows for the assignment of specific roles to users, restricting access to
sensitive resources and ensuring that only authorized individuals can
interact with critical data and operations.

## Image Signing and Scanning

Cosign is used to sign images stored in Harbor, ensuring their authenticity
and providing a layer of trust.

In addition, vulnerability scanning via Trivy is enabled by default for all
images pushed to Harbor. This helps identify potential security flaws
before the images are deployed, ensuring that only secure and trusted
images are used in production environments.

## Secure Communication

It is crucial to configure Harbor to use HTTPS with strong SSL/TLS
certificates to secure client-server communications.

For production environments, corporate-signed certificates should be used
rather than self-signed ones. Self-signed certificates are acceptable only
for testing purposes and should not be used in production, as they do not
provide the same level of trust and security as certificates issued by a
trusted certificate authority.

## Registry Hardening

For added security, it is important to assess your specific use case and
disable any unused features in Harbor, such as unnecessary APIs, to reduce
the attack surface. Regularly reviewing and disabling non-essential
functionalities can help minimize potential vulnerabilities.

Additionally, credentials used to access Harbor—such as API tokens and
system secrets—should be rotated regularly to enhance security.

Since these credentials are not managed by the internal MSR 4 mechanism, it
is recommended to use third-party CI tools or scripts to automate and
manage the credential rotation process, ensuring that sensitive resources
are updated and protected consistently.
