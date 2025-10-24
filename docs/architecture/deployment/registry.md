# Registry

The **Harbor Registry** is deployed as a **ReplicaSet**, running as a single
instance in **All-in-One** deployments and supporting multiple replicas in
**HA** mode. These replicas are not quorum-based, meaning there are no limits
on the number of replicas. The instance count should be determined by your
specific use case and load requirements. To ensure high availability, it is
recommended to have at least two replicas. Like the Job Service, it utilizes
a **PVC** to store registry data, using either local or shared backend storage.
For more details on storage options, please refer to the **Storage** section.
The Registry workload relies on a **ConfigMap** to store the **config.yaml**
and uses **Secrets** to manage sensitive parameters, such as keys and
passwords.

![Registry Deployment](../../_diagrams/depl-registry.svg)
