# Disaster Recovery

!!! warning

    The procedures herein are validated Disaster Recovery approaches for MSR
    4, leveraging Velero, MinIO, and an NFS CSI backend.

    To accommodate diverse customer environments, Velero supports multiple
    backup and recovery options, including integration with various cloud and
    on-premises storage providers. Thus, Mirantis strongly recommends that you
    consult [the official Velero documentation](https://velero.io/docs/latest/)
    for an overview of all supported providers and advanced features.

    To ensure the DR solution aligns with your infrastructure, security,
    and performance requirements, contact Mirantis for assistance.
    The team will evaluate your environment and design a custom backup
    and disaster recovery strategy for your specific MSR 4 deployment.

The following section provides detailed guidance for implementing a Disaster
Recovery (DR) strategy for Mirantis Secure Registry 4 (MSR 4). This solution
focuses on the backup and restoration of an MSR 4 instance that is deployed on
a Kubernetes cluster using Helm, with NFS CSI providing persistent storage.

The DR implementation is based on the following key components:

| Component                      | Description                                                                                                                     |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **MSR 4 (deployed with Helm)** | The target application whose data and Kubernetes resources are protected through the backup and restore process.                |
| **NFS CSI Driver**             | The provider of Persistent Volumes (PVs) for Harbor's stateful components to ensure data persistence across cluster operations. |
| **Velero**                     | The primary tool used for backing up and restoring Kubernetes cluster resources and persistent volumes.                         |
| **MinIO**                      | An S3-compatible object storage server that acts as the Backup Storage Location (BSL) for Velero to store the backup archives.  |

The Disaster Recovery documentation provides detailed instructions for
implementing a DR strategy for MSR 4.
This solution focuses on the backup and restoration of an MSR 4 instance
deployed on a Kubernetes cluster using Helm, with NFS CSI providing persistent
storage.

