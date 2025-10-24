# LDAP Authentication

## Prerequisites

* Ensure you have access to your organization's LDAP server.
* Obtain the LDAP Base DN, Bind DN, Bind Password, and server URL.

## Configure LDAP in MSR

1. **Access MSR Administration Interface**  
    * Log in as an administrator and navigate to the  
      **Administration > Configuration** section.

2. **Set Auth Mode to LDAP**  
    * Under the **Authentication** tab, select **LDAP** from the  
      **Auth Mode** dropdown.

3. **Provide LDAP Server Details**  
    * **Auth Mode** will say **LDAP**.  
    * **LDAP URL**: Enter the server URL (e.g.,  
     `ldap://example.com` or `ldaps://example.com` for secure connections).  
    * **LDAP Search DN** and **LDAP Search Password**: When a user logs in to  
      Harbor with their LDAP username and password, Harbor uses these values to  
      bind to the LDAP/AD server. For example, `cn=admin,dc=example.com`.  
    * **LDAP Base DN**: Harbor looks up the user under the LDAP Base DN entry,  
      including the subtree. For example, `dc=example.com`.  
    * **LDAP Filter**: The filter to search for LDAP/AD users. For example,  
     `objectclass=user`.  
    * **LDAP UID**: An attribute, for example `uid` or `cn`, that is used to  
      match a user with the username. If a match is found, the user's password is  
      verified by a bind request to the LDAP/AD server.  
    * **LDAP Scope**: The scope to search for LDAP/AD users. Select from  
      **Subtree**, **Base**, and **OneLevel**.

4. **(Optional) Manage LDAP Groups**  
    * **LDAP Group Base DN**: Base DN for group lookup. Required when LDAP group  
      feature is enabled.  
    * **LDAP Group Filter**: Search filter for LDAP/AD groups. Required when  
      LDAP group feature is enabled. Available options:  
        * OpenLDAP: `objectclass=groupOfNames`  
        * Active Directory: `objectclass=group`  
    * **LDAP Group GID**: Attribute naming an LDAP/AD group. Required when LDAP  
      group feature is enabled.  
    * **LDAP Group Admin DN**: Group DN for users with Harbor admin access.  
    * **LDAP Group Admin Filter**: Grants Harbor system administrator privileges  
      to all users in groups that match the specified filter.  
    * **LDAP Group Membership**: User attribute for group membership.  
      Default: `memberof`.  
    * **LDAP Scope**: Scope for group search: Subtree, Base, or OneLevel.  
    * **LDAP Group Attached in Parallel**: Attaches groups in parallel to  
     prevent login timeouts.

5. **Uncheck LDAP Verify Cert**  
    * If the LDAP/AD server uses a self-signed or untrusted certificate.

6. **Test LDAP Connection**  
    * Use the **Test LDAP Server** button to validate the connection.  
      Troubleshoot any errors before proceeding.

7. **Save Configuration**  
    * Click **Save** to apply changes.

## Manage LDAP Users in MSR

* After configuring LDAP, MSR automatically authenticates users based on their  
  LDAP credentials.  
* To assign user roles, navigate to **Projects** and assign LDAP-based user  
  accounts to project roles.

Use the table below to identify and apply the correct roles based on the new structure:

| **MSR 2.9 / MSR 3.1 Roles** | **MSR 4 Roles** | **Description** | **Permissions** | **Limitations** |
|------------------------------|-----------------|-----------------|-----------------|-----------------|
| IRE, Cloudview, CIE | Administrator | Full control over the MSR 4 instance. | Manage system settings, users, and projects. Manage registries and replication rules. View and delete audit logs. Manage garbage collection. | Cannot perform operations restricted by external access policies, for example, LDAP-integrated roles. |
|  | Project Admin | Full control within a specific project. | Manage project settings, members, and quotas. Push and pull images. Delete repositories and artifacts. | Cannot modify settings outside their assigned project. Cannot manage global configurations or other projects. |
| DEV, QA, OPS, ReleaseManager, and such | Maintainer | Responsible for managing and maintaining project content. | Push and pull images. Add tags to images. Manage replication rules for their project. | Cannot manage project members. Cannot delete the project or modify project settings. |
| DEV, QA, OPS, ReleaseManager, and such | Developer | Focused on pushing and managing images within the project. | Push images and tags. Pull images from the project. | Cannot delete images or repositories. Cannot manage project members or settings. |
|  | Guest | Has read-only access to project resources. | Pull images from the project. View repository and artifact metadata. | Cannot push images. Cannot delete, modify, or manage anything in the project. |
|  | Limited Guest | Restricted read-only access to specific projects. | View some project resources based on permissions. | Cannot pull images unless explicitly granted permission. Cannot push, delete, or manage project resources. |
