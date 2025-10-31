# Migration Guide

This guide provides instructions for performing migration from MSR 2.9 and 3.1
to MSR 4. MSR supports two migration paths:

* [Manual migration](manual-migration/index.md)
* [Tool-based migration](tool-migration/index.md)

The following comparison highlights the key differences to help you choose
the most appropriate option for your environment.

| Migration | Description|
|------------|---|
| **Manual migration** | Transfers repository data only. <br><br> **Benefits** <br> * Simple and fast to implement with minimal dependencies. <br> - Suitable for small environments or limited migration scope. <br><br> **Considerations** <br> - Does not migrate repository-level permissions. <br> - Does not migrate push and poll mirroring policies. <br> - Manually recreating access controls can be time-consuming. <br> - Prone to human error in large deployments.                                            |
| **Tool-based migration** | Transfers repositories, associated permissions, and push and poll mirroring policies using Mirantis-provided automation tools. <br><br> **Benefits** <br> - Automates migration, reducing manual overhead. <br> - Improves consistency in complex or large-scale deployments. <br> - Transfers metadata using offline copies for consistency. <br><br> **Considerations** <br> - Requires setup and configuration of a migration tool. <br> - Best suited for complex or large-scale environments. |
