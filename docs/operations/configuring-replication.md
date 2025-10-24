# Configuring Replication

## Introduction to Replication

**Purpose of Replication:**  

Replication allows synchronization of container images across multiple registry
instances. It is commonly used for:

- **Disaster Recovery:** Creating replicas in different locations for
  redundancy and availability.  
- **Load Balancing:** Distributing image pull requests across registries to
  enhance performance and reduce latency.  
- **Collaborative Environments:** Enabling global teams to access synchronized
  repositories.

**Key Concepts:**

- **Replication Endpoint:** Defines the registry MSR will replicate images to
  or from.  
- **Replication Rule:** Specifies which images to replicate, using filters such
  as namespace, tags, or patterns.  
- **Triggers:** Control when replication occurs — manually, immediately, or on
  a schedule.

## Configuring Replication Endpoints

Create a replication endpoint in the MSR 4 UI.

1. **Log in to the MSR 4 Web Interface**

   Use your admin credentials to access MSR 4.

2. **Navigate to Registries**

    - From the main menu, go to **Administration → Registries**.  
    - Manage all endpoints your MSR 4 instance connects to for replication.

3. **Create a New Endpoint**

    - Click **+ New Endpoint** to begin setup.  
    - **Select Provider Type:** Choose **MSR**, **Docker Registry**, **Harbor**, or **AWS ECR**.  
    - **Endpoint Name:** Enter a descriptive name (e.g., *US-West Registry*, *Production Backup*).  
    - **Endpoint URL:** Provide the full URL of the target registry (e.g., `https://example-registry.com`).  
    - **Access ID:** Enter the username for the remote registry.  
    - **Access Secret:** Enter the password for the account.  
    - **Verify Connection:** Click **Test Connection** to confirm that MSR 4
      can reach the endpoint successfully. A success message indicates valid
      credentials and connectivity.

4. **Save Endpoint Configuration**

   Click **Save** after successful testing to finalize configuration.

**Considerations:**  

Ensure registry URLs and credentials are up to date. Expired tokens or
incorrect URLs can interrupt replication jobs and require troubleshooting.


## Creating Replication Rules

Replication rules define the replication scope to synchronize only the 
necessary images, conserving bandwidth and storage.

**Setting Up a New Replication Rule in MSR 4**

1. **Access the Replication Rules Panel**

    - In the MSR 4 interface, go to **Administration → Replications**.  
    - The **Replications** page displays existing rules and lets you add or
      modify rules.

2. **Define a New Rule**

    - Click **+ New Replication Rule**.  
    - **Name:** Give the rule a clear name (for example, *Sync to Europe Backup*).  
    - **Replication Mode:** Choose *Push* to send data to the remote registry, 
      or *Pull* to copy data from it.  
    - **Source Resource Filter:** Filter which images to include based on:
      - **Namespace:** Sync only images from specific namespaces.  
      - **Tag Patterns:** Limit replication to specific tags (for example, `*latest`).  
      - **Label:** Replicate only images with certain labels.  
      - Set name to `**` to download **all images**.  
    - **Destination Registry:** Select a previously configured endpoint.  
    - **Namespace & Flattening:** Optionally flatten namespaces during mirroring.  
    - **Configure Trigger Mode:** Define when replication occurs:
      - **Manual:** Triggered by an admin.  
      - **Immediate:** Starts when an image is pushed to the source.  
      - **Scheduled:** Set a CRON-based schedule (e.g., *daily at midnight*).  
    - **Save and Activate the Rule:** Click **Create** to save and activate.



## Managing and Monitoring Replications

Efficient monitoring ensures seamless synchronization and quick issue resolution.

### Monitoring Replication Jobs

1. **Access Replication Jobs**

    - Go to **Administration → Replications** in MSR 4.  
    - Select a replication rule, then **Actions → Edit** to modify its configuration.

2. **Run a Replication Job Manually**

    - From **Administration → Replications**, select a rule and click
      **Replicate** to start it immediately, regardless of the schedule.

3. **View Job Details**

    - Navigate to **Administration → Replications**.  
    - Select a rule to see current and historical job data.  
    - Click a job **entry ID** to view logs, errors, and detailed replication 
      statistics for troubleshooting and verification.

4. **Re-run Failed Jobs**

    - For failed jobs, select **Replicate** again.  
    - Confirm that the endpoint connection and credentials are valid before re-running.
