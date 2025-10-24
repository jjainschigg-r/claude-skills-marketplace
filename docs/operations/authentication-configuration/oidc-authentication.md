# OIDC Authentication

Configuring OpenID Connect (OIDC) provides a secure and scalable method for
integrating authentication with identity providers.

## Prerequisites

- Register MSR as a client in your OIDC provider (e.g., Okta, Keycloak, Azure
  AD).
- Obtain the client ID, client secret, and OIDC endpoint.

## Configure OIDC in MSR

1. **Access the MSR Administration Interface**  
    - Log in and navigate to **Administration** → **Configuration** → **Authentication**.

2. **Set Authentication Mode to OIDC**  
    - Select **OIDC** as the authentication mode.

3. **Enter OIDC Provider Details**  
    - **OIDC Provider Name**: The name of the OIDC provider.  
    - **OIDC Provider Endpoint**: The URL of the endpoint of the OIDC provider, which must start with `https`.  
    - **OIDC Client ID**: The client ID with which Harbor is registered with the OIDC provider.  
    - **OIDC Client Secret**: The secret with which Harbor is registered with the OIDC provider.  
    - **Group Claim Name**: The name of a custom group claim that you have configured in your OIDC provider, 
      that includes the groups to add to Harbor.  
    - **OIDC Admin Group**: The name of the admin group. If the ID token of the user shows that they are a 
      member of this group, the user will have admin privilege in Harbor.  
      **Note**: You can only set one Admin Group. Please also make sure the value in this field matches the 
      value of group item in the ID token.  
    - **OIDC Scope**: A comma-separated string listing the scopes to be used during authentication.  
        - The OIDC scope must contain `openid` and usually also contains `profile` and `email`.  
        - To obtain refresh tokens it should also contain `offline_access`.  
        - If you are using OIDC groups, a scope must identify the group claim. Check with your OIDC provider
          administrator for precise details of how to identify the group claim scope, as this differs from
          vendor to vendor.  
    - Uncheck **Verify Certificate** if the OIDC Provider uses a self-signed or untrusted certificate.  
    - Check **Automatic onboarding** if you do not want the user to set their username in Harbor during their first login.  
        - When this option is checked, the attribute **Username Claim** must be set.  
        - Harbor will read the value of this claim from the ID token and use it as the username for onboarding
          the user.  
        - Therefore, you must make sure the value you set in **Username Claim** is included in the ID token
          returned by the OIDC provider you set, otherwise there will be a system error when Harbor tries to
          onboard the user.  
    - Verify that the Redirect URI that you configured in your OIDC provider is the same as the one displayed 
      at the bottom of the page on the Mirantis Harbor configuration page.

4. **Test OIDC Server Connection**  
    - Use the **Test OIDC Server** button to verify the configuration.

5. **Save Configuration**  
    - After a successful test, click **Save**.

## Authenticate users with OIDC

- Users authenticate with the OIDC provider's login page.  
- OIDC tokens are used for API and CLI access.
