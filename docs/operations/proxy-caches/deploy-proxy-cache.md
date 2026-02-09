# Deploy a Proxy Cache

1. Log in to the MSR web interface as an administrator.
2. From the left-side navigation panel, select **Administration** > **Registries**.
3. Click **+ New Endpoint**, and configure the following settings:
    
    | Parameter             | Required action                                                                                                  |
    |-------------------|------------------------------------------------------------------------------------------------------------------|
    | **Provider Type** | Select **Harbor**.                                                                                               |
    | **Endpoint Name** | Enter a descriptive name that identifies the endpoint purpose, such as *US-West Registry* or *Production Cache*. |
    | **Description**   | Optional: Provide additional context for the endpoint.                                                           |
    | **Endpoint URL**  | Enter the full URL of the target registry, for example: `https://example-registry.com`.                          |
    | **Access ID**     | Enter the username used to authenticate with the remote registry.                                                |
    | **Access Secret** | Enter the password associated with the account used to access the remote registry.                               |

4. Click **Test Connection** to verify network connectivity and credentials. 
   A success message confirms that MSR can reach the endpoint.
5. Click **Save** to create the registry endpoint. 
6. Go to **Projects**, click **New Project**, and enter a name for the project. 
7. Enable **Proxy Cache**, and select the registry endpoint from the list that displays.
8. Click **OK** to create the project.
9. Update image pull commands to use the proxy cache path.

    - Pull an image directly from the registry:

        ```bash
        docker pull <Registry URL>/ubuntu/ubuntu:latest
        ```

    - Pull the same image through the proxy cache:

        ```bash
        docker pull <Registry URL>/proxy_cache/ubuntu/ubuntu:latest
        ```
 