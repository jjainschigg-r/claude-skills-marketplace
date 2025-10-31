# Perform Migration

!!! warning "Manual Helm Chart Migration Required"

    When migrating from MSR 2.x or MSR 3.x to MSR 4.x, Helm charts do not
    automatically migrate.
    You must manually migrate any existing Helm charts to the new environment.

To migrate images, repositories, and tags from an MSR 2.x or MSR 3.x
environment to an MSR 4.x environment, follow these steps:

1. Access the MSR Web UI.

2. Navigate to **Administration** → **Registries**.

3. Select **New Endpoint** to add a new registry connection.

4. Fill in the pop-up with the following details:

    * **Provider**: ``DTR``
    * **Name**: ``<your-identifier>``
    * **Endpoint URL**: ``<root-of-the-registry>``
    * **Access ID**: ``<admin-username>``
    * **Access Secret**: ``<admin-password>``

    !!! note

        Avoid specifying a user or repository namespace, as this will restrict
        access. Using the root enables full crawling of the host.

    ![Edit New Endpoint](../../../_images/edit-new-endpoint.png)

5. Navigate to **Administration** → **Replications**.

6. Select **New Replication Rule** to create a replication rule.

7. In the pop-up window, review and confirm the following settings:

    * **Replication mode**: Ensure it is set to **Pull-based**.
    * **Source registry**: Verify that the MSR 2 and MSR 3 hosts added in
      previous steps are listed.
    * **Source resource filter**: Ensure the **Name** field is set to ``**``,
      with all other fields left blank.
    * **Destination**: Make sure flattening is set to ``Flatten 1 Level``.
      If your environment uses an organization namespace in MSR 2 or MSR 3,
      you may choose an alternative flattening option.

    <details>
      <summary>Click to learn more about flattening options</summary>
    
      You can choose to flatten or retain the original structure of any
      organization or namespace.
      Enabling the flattening option will merge all content into a single
      namespace (`ns`). If your organization uses a more flexible
      namespace or organizational structure, review the following guidelines
      to understand how flattening may affect your setup:
    
      * Flatten All Levels: `a/b/c/d/img` → `ns/img`
      * No Flattening: `a/b/c/d/img` → `ns/a/b/c/d/img`
      * Flatten 1 Level: `a/b/c/d/img` → `ns/b/c/d/img`
      * Flatten 2 Levels: `a/b/c/d/img` → `ns/c/d/img`
      * Flatten 3 Levels: `a/b/c/d/img` → `ns/d/img`
    
      The term `Levels` refers to the directory depth of the source
      path (`a/b/c/d/img`).
    
     </details>

    ![Edit Replication Rule](../../../_images/edit-replication-rule.png)

8. Select the rule created in the previous step and click
   **Replicate**. Be aware that pulling down the entire host may take
   some time to complete.

    ![Replications](../../../_images/replications.png)

9. To check the status of the replication process, click the job ID.

    ![Check Status](../../../_images/check-status.png)
