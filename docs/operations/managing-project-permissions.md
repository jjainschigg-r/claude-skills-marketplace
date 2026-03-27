# Managing Project Permissions

**Purpose**: Permissions allow controlled access to projects, ensuring only
authorized users can modify and interact with registry content.

- **Key Terms**:

   - **Project**: A logical container in goharbor.io where users can store,
     manage, and share images.
   - **User Roles**: Project Admin, Maintainer, Developer, Guest—each with
     specific permission levels.

- **Key Concepts**

   - Security Best Practices

     - **Least-Privilege Principle**: Regularly audit and apply the minimum
        required permissions.
     - **Review and Audit**: Routinely check project member lists, adjust roles
        as needed, and remove users who no longer need access.

   - There are two **System-Level Roles** in MSR

     - **Harbor System Administrator**: The *Harbor System Administrator* role
       holds the highest level of privileges within the system. In addition to
       the standard user permissions, a system administrator can:

       - View and manage all projects, including private and public projects.
       - Assign administrative privileges to regular users.
       - Delete user accounts.
       - Configure vulnerability scanning policies for all images.
       - Manage the default public project, “**library**”, which is owned by
         the system administrator.

     - **Anonymous User**. A user not logged into the system is
       classified as an *Anonymous User*. Anonymous users:

       - Have **read-only access** to public projects.
       - Cannot view or access private projects.


## Overview of User and Group Permissions

- **ProjectAdmin**: When creating a new project, you will be assigned the
  “ProjectAdmin” role to the project. Besides read-write privileges, the
  “ProjectAdmin” also has some management privileges, such as adding and
  removing members, starting a vulnerability scan.
- **Developer**: Developer has read and write privileges for a project.
- **Maintainer**: Maintainer has elevated permissions beyond those of
  ‘Developer’ including the ability to scan images, view replication jobs, and
  delete images and helm charts.
- **Guest**: Guest has read-only privilege for a specified project. They can
  pull and retag images, but cannot push.
- **Limited Guest**: A Limited Guest does not have full read privileges for a
  project. They can pull images but cannot push, and they cannot see logs or
  the other members of a project. For example, you can create limited guests
  for users from different organizations who share access to a project.

## Instructions for Setting Up Project Permissions

1. Log in to the MSR 4 web interface using your admin credentials.
2. Navigate to **Projects** from the main menu.
3. Click **+ New Project**.

    - **Project Name**: Enter a unique name for your project.
    - **Access Level**: Choose between **Private** (restricted access) or
      **Public** (accessible to all authenticated users).

        !!! warning
   
            To prevent unauthorized access to internal or sensitive workloads,
            use **Private** projects.
            In internet-facing registries, **Public** projects are visible to all users,
            thus, anyone can pull images or view metadata without authentication.

    - Select **Project quota limits** to enable any quota as desired by MiB,
      GiB, and TiB sizes.
    - Select **Proxy Cache** to enable this to allow this project to act as
      a pull-through cache for a particular target registry instance.

      - MSR 4 can only act a proxy for DockerHub, Docker Registry, Harbor,
        Aws ECR, Azure ACR, Alibaba Cloud ACR, Quay, Google GCR, Github GHCR,
        and JFrog Artifactory registries.

4. Click **OK** to create the project.

## Adding Users and Groups to a Project

To add **groups** to a project, you must first have OIDC authentication
enabled.

1. Go to **Projects** and select the project where you want to add users.
2. In the project menu, select **Members**.
3. Click **+ Add Member** or **+ Group**.

    - **Member Name**: Enter the exact username or group name as registered in
      Harbor.
    - **Role**: Select the role (for example, Developer, Guest) based on the required
      access level.

4. Click **Save** to assign the member with the specified role.

## Changing Permissions to Project Members

1. Access the Members tab within the chosen project.
2. Select the checkbox next to the member or group.
3. Select **ACTION** then select the role (for example, Developer, Guest) based on the
   required access level.

## Editing or Removing Members

1. Access the Members tab within the chosen project.
2. Select the checkbox next to the member or group.
3. Select **ACTION** then select **Remove**

## Automation Using the Harbor API

1. Install Harbor CLI (if applicable).
2. Use commands like add-user, assign-role, and create-project to automate
   user setup.
3. Example:

    ```bash
    harbor-cli project create example-project --public
    harbor-cli project member add example-project --user john_doe --role developer
    ```

