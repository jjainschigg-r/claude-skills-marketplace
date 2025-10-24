# Fundamental Services Layer

These are the core functional services of MSR 4, including Proxy, Core, and Job
services, all built on Harbor. This layer can also accommodate third-party
services installed and integrated to enhance functionality, such as improved
replication, advanced logging capabilities, and additional integration drivers.

![Fundamental Services Layer](../../_diagrams/fundamental-services.svg)

## Core

Harbor's core service, which provides the following functions, is illustrated
in the diagram below:

![Core Architecture](../../_diagrams/architecture-core.svg)

| Function | Description |
|-----------|--------------|
| **API Server** | An HTTP server that accepts REST API requests and responds by utilizing its submodules, including **Authentication and Authorization**, **Middleware**, and **API Handlers**, to process and manage the requests effectively. |
| **Authentication and Authorization** | The authentication service can secure requests, which can be powered by a local database, **AD/LDAP**, or **OIDC**. The **RBAC (Role-Based Access Control)** mechanism authorizes actions such as pulling or pushing images. The **Token service** issues tokens for each **Docker push/pull** command based on the user's role within a project. If a request from a Docker client lacks a token, the **Registry** redirects the request to the **Token service** for token issuance. |
| **Middleware** | This component preprocesses incoming requests to determine whether they meet the required criteria before passing them to backend services for further processing. Various functions, including **quota management**, **signature verification**, **vulnerability severity checks**, and **robot account parsing**, are implemented as middleware. MSR4 supports Cosign for image signing and verification. Cosign is part of the Sigstore project. Cosign allows signing without relying on a separate, heavyweight service like Notary and supports keyless signing with OIDC identities. Harbor integrates this natively, providing better interoperability with Kubernetes-native tools and workflows. |
| **API Handlers** | These handle the corresponding REST API requests, primarily parsing and validating request parameters. They execute the business logic associated with the relevant API controller and generate a response, which is then written back to the client. |
| **API Controller** | The API controller plays a critical role in orchestrating the processing of REST API requests. It's a key component within the system's architecture that manages the interaction between the user's requests and the backend services. |
| **Configuration Manager** | Manages all system configurations, including settings for authentication types, email configurations, certificates, and other essential parameters. |
| **Project Management** | Oversees the core data and associated metadata of projects, which are created to isolate and manage the artifacts effectively. |
| **Quota Manager** | Manages project quota settings and validates quotas whenever new pushes are made, ensuring that usage limits are followed. |
| **Chart Controller** | Acts as a proxy for chart-related requests to the OCI-compatible registry backend and provides various extensions to enhance the chart management experience. |
| **Retention Manager** | Manages tag retention policies and oversees the execution and monitoring of tag retention processes, ensuring efficient storage management. |
| **Content Trust** | Enhances the trust capabilities provided by the backend **Cosign**, facilitating a seamless content trust process for secure and verified operations. |
| **Replication Controller** | Manages replication policies and registry adapters while also triggering and monitoring concurrent replication processes to ensure consistency and reliability across systems. |
| **Scan Manager** | Oversees multiple configured scanners from different providers and generates scan summaries and reports for specified artifacts, ensuring comprehensive security and vulnerability assessments. |
| **Label Manager** | The Label Manager is responsible for the creation and management of labels that can be applied to projects and resources within the registry. |
| **P2P Manager** | This component is crucial for enhancing the efficiency of image distribution across different instances using peer-to-peer (P2P) technology. Its role involves setting up and managing P2P preheat provider instances. These instances allow specified images to be preheated into a P2P network, facilitating faster access and distribution across various nodes. |
| **Notification Manager (Webhook)** | A mechanism configured in Harbor that sends artifact status changes to designated webhook endpoints. Interested parties can trigger follow-up actions by listening to related webhook events, such as HTTP POST requests or Slack notifications. |
| **OCI Artifact Manager** | The core component manages the entire lifecycle of OCI artifacts across the Harbor registry, ensuring efficient storage, retrieval, and management. |
| **Registry Driver** | Implemented as a registry client SDK, it facilitates communication with the underlying registry (currently **Docker Distribution**), enabling seamless interaction and data management. |
| **Robot Manager** | The Robot Manager manages robot accounts, which are used to automate operations through APIs without requiring interactive user login. These accounts facilitate automated workflows such as CI/CD pipelines, allowing tasks like pushing or pulling images and Helm charts, among other operations, through command-line interfaces (CLI) like Docker and Helm. |
| **Log Collector** | Responsible for aggregating logs from various modules into a centralized location, ensuring streamlined access and management of log data. |
| **GC Controller** | Manages the online garbage collection (GC) schedule, initiating and tracking the progress of GC tasks to ensure efficient resource utilization and cleanup. |
| **Traffic Proxy** | The Traffic Proxy in Harbor primarily functions through its Proxy Cache feature, which allows Harbor to act as a middleman between users and external Docker registries. |

## Job Service

The MSR 4 Job Service is a general job execution queue service to let other
components/services submit requests of running asynchronous tasks concurrently
with simple restful APIs.

## Trivy

**Trivy** is a powerful and versatile security scanner with tools to detect
security vulnerabilities across various targets, ensuring comprehensive scans
for potential issues. However, if customers prefer to use a different scanner,
MSR 4 allows such customization in the configuration.
