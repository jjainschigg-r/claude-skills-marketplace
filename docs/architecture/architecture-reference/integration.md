# Integration

Functional services can be integrated with various auxiliary services,
including publicly available providers and locally hosted corporate services.

## Identity providers

**Identity providers** are centralized Identity and Access Management
solutions, such as **AD/LDAP** or **OIDC**, that can be seamlessly integrated
with MSR 4.

## Metrics Observability

MSR 4 can be integrated with **Prometheus** to centralize the collection and
management of metrics.

## Scan providers

MSR 4 supports integration with multiple scanning providers. As mentioned in
the core services, Trivy is used by default.

## Registry providers

**Multiple providers** can support image storage in MSR 4. By default,
MSR 4 uses an internal registry that stores data on **Data Storage**, as
outlined in the Data Access Layer. Alternatively, various registry providers
can be enabled, including:

* Distribution (Docker Registry)
* Docker Hub
* Huawei SWR
* Amazon ECR
* Google GCR
* Azure ACR
* Ali ACR
* Helm Hub
* Quay
* Artifactory
* GitLab Registry

Once a provider is attached, MSR 4 will use it as a backend registry
replication, pushing and pulling images. For more information regarding
the replication and Backend Registry configuration, refer to
the [Configuring Replication](../../operations/configuring-replication.md).