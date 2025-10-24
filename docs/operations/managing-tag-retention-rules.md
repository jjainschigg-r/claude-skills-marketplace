# Managing Tag Retention Rules

## Introduction to Tag Retention in MSR

Tag retention rules are essential for maintaining an efficient and organized registry.  
They define policies that determine which image tags to retain and which to remove.  
This helps prevent the accumulation of outdated images, optimize storage, and
align with organizational image lifecycle policies.

**Key Concepts:**

- **Tag Retention Rules:** Policies that specify criteria for keeping or
  deleting image tags.  
- **Policy Filters:** Parameters such as tags, repositories, or labels used to
  control rule application.  
- **Priority:** The order in which rules execute, providing granular control
  over retention or removal.

## Understanding Tag Retention Rules

Tag retention rules are evaluated against repositories within a project to
determine which tags to keep or remove.  
Administrators can use filters such as tag patterns or image age to
fine-tune retention policies.

**Example Use Cases:**

- **Development Projects:** Retain only the latest five tags of a repository.  
- **Production Repositories:** Retain tags with labels like `stable` or `release`.  
- **Cleanup Operations:** Remove all tags older than 30 days.

## Configuring Tag Retention Rules in MSR

1. **Access the Tag Retention Panel**

    a. Log in to the MSR web interface.  
    b. Go to **Projects** and select the desired project.  
    c. Click **Policy**.  
    d. Select **Tag Retention** under project settings.

2. **Define a New Rule**

    a. Click **+ New Rule** to begin configuration.

3. **Select Matching or Excluding Rule**

    a. In the **Repositories** dropdown, select *matching* or *excluding*.  
    b. Specify repositories in the **Repositories** field using one of the following:

      - A specific repository name, e.g., `my_repo_1`.  
      - A comma-separated list, e.g., `my_repo_1,my_repo_2,your_repo_3`.  
      - A partial repository name with wildcards (*):  
        - `my_*` matches repositories starting with `my_`.  
        - `*_3` matches repositories ending with `_3`.  
        - `*_repo_*` matches repositories containing `repo`.  
      - `**` applies the rule to **all repositories** in the project.

4. **Select Retention Criteria**

   Choose **by artifact count or number of days** to define tag retention duration or quantity.

   | Option | Description |
   | ------- | ----------- |
   | retain the most recently pushed # artifacts | Retain a set number of most recently pushed artifacts. |
   | retain the most recently pulled # artifacts | Retain a set number of most recently pulled artifacts. |
   | retain the artifacts pushed within the last # days | Retain artifacts pushed within a specified time range. |
   | retain the artifacts pulled within the last # days | Retain artifacts pulled within a specified time range. |
   | retain always | Always retain the artifacts identified by this rule. |

5. **Specify Tags for Rule Application**

   Use the **Tags** field to define which tags the rule targets:

    a. A single tag, e.g., `my_tag_1`.  
    b. A comma-separated list, e.g., `my_tag_1,my_tag_2,your_tag_3`.  
    c. A partial tag with wildcards (*):  
       - `my_*` matches tags starting with `my_`.  
       - `*_3` matches tags ending with `_3`.  
       - `*_tag_*` matches tags containing `tag`.  
    d. `**` applies to all tags in the project.

    - If you select *matching*, the rule applies only to specified tags.  
    - If you select *excluding*, it applies to all tags except those listed.

6. **Save and Activate the Rule**

   Click **Save** once all fields are complete.  
   The rule will appear in the **Tag Retention Rules** table.

## Managing and Executing Retention Policies

### Viewing and Managing Rules

1. Open the **Policy** page under your selected **Project**.  
2. To edit a rule, go to **Retention Rules**, click **ACTION → Edit**, and
   adjust the scope or filters.  
3. To delete a rule, select **ACTION → Delete**.

## Executing Retention Rules

### Scheduled Execution

1. Under **Projects**, open your project.  
2. Go to **Policy** and ensure a retention policy is configured.  
3. Under **Schedule**, select **Hourly**, **Daily**, **Weekly**, or **Custom**.  
   - Choosing **Custom** allows you to define a cron schedule.

### Manual Execution

1. Under **Projects**, open your project.  
2. Go to **Policy** and verify that a retention rule exists.  
3. Select **DRY RUN** to simulate execution safely, or **RUN NOW** to apply it
   immediately.

### Reviewing Execution Logs

- After execution, view logs to confirm success or troubleshoot issues.  
- Logs show retained and deleted tags as well as any errors.  
- Navigate to **Policy → Retention Runs**, select a job, and click **>** to
  expand details.  
- Click **Log** beside each repository to view its specific log entries.

## Interaction Between Tag Retention Rules and Project Quotas

The MSR administrator can configure project quotas to limit both the number of
tags and the total storage used.  
See **Configure Project Quotas** for more information.

When a quota is applied, it serves as a strict cap — retention rules cannot
override it.  
If retention rules attempt to retain more tags than allowed,
the **quota takes precedence**.
