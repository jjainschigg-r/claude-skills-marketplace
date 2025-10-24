# Configuring Webhooks

As a project administrator, you can connect your Harbor projects to external  
webhook endpoints. This enables Harbor to notify those endpoints of events  
occurring within your projects, supporting integration with other tools and  
enhancing continuous integration and development workflows.

## Supported Events

Harbor supports two types of webhook endpoints: **HTTP** and **Slack**.  
You can configure multiple webhook endpoints per project. Notifications are  
sent in **JSON** format via HTTP or HTTPS POST requests to the specified  
endpoint URL or Slack address.

Harbor supports two JSON payload formats:

- **Default:** The traditional format used in earlier versions.  
- **CloudEvents:** A format compliant with the CloudEvents specification.

The following table lists the events that trigger notifications and the  
contents of each message.

| Event | Webhook Event Type | Contents of Notification |
|-------|--------------------|---------------------------|
| **Push artifact to registry** | `PUSH_ARTIFACT` | Repository namespace name, repository name, resource URL, tags, manifest digest, artifact name, push time, and username of the user who pushed the artifact. |
| **Pull artifact from registry** | `PULL_ARTIFACT` | Repository namespace name, repository name, manifest digest, artifact name, pull time, and username of the user who pulled the artifact. |
| **Delete artifact from registry** | `DELETE_ARTIFACT` | Repository namespace name, repository name, manifest digest, artifact name, artifact size, delete time, and username of the user who deleted the image. |
| **Artifact scan completed** | `SCANNING_COMPLETED` | Repository namespace name, repository name, tag scanned, artifact name, number of critical, major, and minor issues, last scan status, completion time, and username of the user who performed the scan. |
| **Artifact scan stopped** | `SCANNING_STOPPED` | Repository namespace name, repository name, tag scanned, artifact name, and scan status. |
| **Artifact scan failed** | `SCANNING_FAILED` | Repository namespace name, repository name, tag scanned, artifact name, error details, and username of the user who performed the scan. |
| **Project quota exceeded** | `QUOTA_EXCEED` | Repository namespace name, repository name, tags, manifest digest, artifact name, push time, and username of the user who pushed the artifact. |
| **Project quota near threshold** | `QUOTA_WARNING` | Repository namespace name, repository name, tags, manifest digest, artifact name, push time, and username of the user who pushed the artifact. |
| **Artifact replication status changed** | `REPLICATION` | Repository namespace name, repository name, tags, manifest digest, artifact name, push time, and username of the user who triggered replication. |
| **Artifact tag retention finished** | `TAG_RETENTION` | Repository namespace name, repository name, tags, manifest digest, and artifact name. |

# Configuring Webhook Notifications

1. **Access the Harbor Interface**  

    - Log in to the Harbor web portal.  
    - Navigate to the project where you want to configure webhooks.  

2. **Navigate to Webhooks Settings**  

    - Within the project, click on the **Webhooks** tab.  

3. **Add a New Webhook**  

    - Click the **NEW WEBHOOK** button.  
    - In the form that appears, provide the following details:  
      - **Name:** A descriptive name for the webhook.  
      - **Description:** *(Optional)* Add information about the webhook’s  
        purpose.  
      - **Notify Type:** Choose between **HTTP** or **SLACK**, depending on your  
        endpoint.  
      - **Payload Format:** Select either **Default** or **CloudEvents**.  
      - **Event Type:** Check the boxes for events that should trigger  
        notifications.  
      - **Endpoint URL:** Enter the URL where webhook payloads should be sent.  
      - **Auth Header:** *(Optional)* Provide authentication credentials if  
        required by the endpoint.  
      - **Verify Remote Certificate:** Enable this to verify the SSL certificate  
        of the endpoint.  

4. **Save the Webhook**  

     - After completing all required fields, click **ADD** to create the webhook.

## Manage Existing Webhooks

- **Access the Harbor Interface** 

   - Log in to the Harbor web portal.  
   - Navigate to the project where the webhooks are configured.  

- **Navigate to Webhooks Settings**  

   - Within the project, click the **Webhooks** tab.  
   - Select the existing webhook under **Webhooks**.  
   - Click **ACTION** → **EDIT** to update or modify webhook details.  

## Webhook Payload Examples

When an artifact is pushed to the registry, and you’ve configured a webhook
for the PUSH_ARTIFACT event, Harbor sends a JSON payload to the specified
endpoint. Below is an example of such a payload in the **Default** format:

```json
{
  "type": "PUSH_ARTIFACT",
  "occur_at": 1680501893,
  "operator": "harbor-jobservice",
  "event_data": {
    "resources": [
      {
        "digest": "sha256:954b378c375d852eb3c63ab88978f640b4348b01c1b3e0e1e4e4e4e4e4e4e4e4",
        "tag": "latest",
        "resource_url": "harbor.example.com/project/repository:latest"
      }
    ],
    "repository": {
      "name": "repository",
      "namespace": "project",
      "repo_full_name": "project/repository",
      "repo_type": "private"
    }
  }
}
```

In the **CloudEvents** format, the payload would be structured differently,
adhering to the CloudEvents specification.

**Recommendations for Webhook Endpoints**

- **HTTP Endpoints**: Ensure that the endpoint has a listener capable of
  interpreting the JSON payload and acting upon the information,
  such as executing a script or triggering a build process.
- **Slack Endpoints**: Follow Slack’s guidelines for incoming webhooks to
  integrate Harbor notifications into Slack channels.

By configuring webhook notifications, you can automate responses to various
events within your Harbor projects, thereby enhancing your continuous
integration and deployment pipelines.

## Differences Between MSR 3 Webhooks and MSR 4 Webhooks (Harbor-Based)

When migrating from Mirantis Secure Registry (MSR) 3 to MSR 4 (based on
Harbor), several key differences in webhook functionality should be noted.
These changes reflect the enhanced architecture and expanded event support in
Harbor, offering greater flexibility and compatibility while addressing certain
legacy limitations.

1. **Event Coverage**

    - In **MSR 3**, webhook notifications were primarily focused on
      repository-level events, such as image push and deletion. However,
      **MSR 4** expands the event coverage significantly, including
      notifications for:

      - Artifact scans (completed, stopped, or failed).
      - Project quota thresholds (exceeded or nearing limits).
      - Replication and tag retention processes.

    - This expanded event set allows for more granular monitoring and
      automation opportunities.

2. **Payload Format Options**

    - **MSR 3** supported a single JSON payload format for webhook events,
      designed to integrate with basic CI/CD pipelines. In contrast, **MSR 4**
      introduces dual payload format options:

      - **Default Format**: Maintains backward compatibility for simple
        integrations.
      - **CloudEvents Format**: Complies with the CloudEvents specification,
        enabling integration with modern cloud-native tools and ecosystems.

3. **Webhook Management Interface**

    - In **MSR 3**, managing webhooks required navigating a simpler interface
      with limited options for customization. In **MSR 4**, the management UI is
      more sophisticated, allowing users to configure multiple endpoints, select
      specific event types, and apply authentication or SSL verification for
      secure communication.

4. **Slack Integration**

    - MSR 3 did not natively support direct Slack notifications. With MSR 4, you
      can configure webhook notifications to integrate directly with Slack
      channels, streamlining team collaboration, and real-time monitoring.

5. **Authentication and Security Enhancements**

    - MSR 4 enhances webhook security by supporting authentication headers and
      remote certificate verification for HTTPS endpoints, which were limited or
      unavailable in MSR 3.

6. **Ease of Configuration**

    - The MSR 4 webhook interface provides a user-friendly experience for
      creating, testing, and managing webhooks, compared to the more rudimentary
      configuration options in MSR 3.

### Features No Longer Present in MSR 4 Webhooks

While MSR 4 webhooks offer enhanced functionality, a few MSR 3-specific
behaviors are no longer present:

1. **Tight Coupling with Legacy Components**

    - MSR 3 webhooks were tightly integrated with certain Mirantis-specific
      features and configurations. MSR 4’s Harbor-based webhooks embrace open
      standards, which may mean that legacy integrations require adjustments.

2. **Simplistic Event Payloads**

    - For users relying on MSR 3’s minimalistic payloads, the more detailed JSON
      structures in MSR 4 may require updates to existing automation scripts or
      parsers.

By understanding these differences and new capabilities, organizations can
better adapt their workflows and take full advantage of the modernized webhook
architecture in MSR 4.
