# Authentication Configuration

Authentication in MSR ensures secure access by validating user credentials
against an external provider or internal database. Supported methods include:

* [**LDAP Authentication**](ldap-authentication.md): Leverages existing LDAP directories to authenticate
  users.
* [**OpenID Connect (OIDC)**](oidc-authentication.md): A federated identity standard for single sign-on
  (SSO) and secure authentication.
* [**Database Authentication**](database-authentication.md): Built-in method that manages user credentials
  locally within MSR. This is the default authentication option.

Each authentication method offers unique advantages depending on your
organization's requirements. Database Authentication offers the option for
smaller organizations or for sandbox and testing environments that don't need
or have access to an external provider to get started. For larger organizations
and production environments, the protocols LDAP or OIDC can be used for bulk
user onboarding and group management.