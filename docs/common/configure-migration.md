# Post-Migration Configuration

After upgrading MSR, several settings will not carry over automatically.  
Below are key aspects to consider after a successful migration:

| Configuration area | Required actions |
|--------------------|------------------|
| **Project Visibility** | Project visibility (public/private) must be configured manually. In MSR 3.x, private and public image repositories could coexist under a single organization. In MSR 4, visibility is set only at the project level. Mixed public/private repositories under one organization in MSR 3.x must be manually adjusted. |
| **Project Permissions** | MSR 4 organizes repositories within projects. Ensure that project-level permissions are properly recreated. See: <a href="/operations/managing-project-permissions/">Managing Project Permissions</a>. |
| **Registry Replication** | Re-establish any replication or mirroring rules and schedules in MSR 4. See: <a href="/operations/configuring-replication/">Configuring replication</a>. |
| **Image Tag Retention** | Manually configure existing retention policies for images in MSR 4 to ensure appropriate lifecycle management. See: <a href="/operations/managing-tag-retention-rules/">Managing Tag Retention</a>. |
| **Scanning Settings** | Configure or re-enable Trivy image scanning policies. See: <a href="/operations/vulnerability-scanning/">Vulnerability Scanning</a>. |
| **Audit Logs** | Set up logging mechanisms in MSR 4 for compliance. See: <a href="/operations/log-rotation/">Log Rotation in Mirantis Secure Registry</a>. |
| **Webhooks** | Recreate and configure webhooks to point to MSR 4. See: <a href="/operations/configuring-webhooks/">Configuring Webhooks</a>. |
| **CI/CD Pipelines** | Update custom CI/CD pipelines to reference MSR 4. |
| **Signed Images** | Reconfigure image signing using Cosign. See: <a href="/operations/signing-artifacts-with-cosign/">Signing Artifacts with Cosign</a>. |
| **Garbage Collection Settings** | Manually reconfigure garbage collection policies in MSR 4. See: <a href="/operations/managing-garbage-collection/">Managing Garbage Collection</a>. |
| **Certificate Management** | Re-establish custom certificate configurations in MSR 4. |
| **API Updates** | Update API endpoints and account for changes in MSR 4's API. |


## Pruning Policies

Pruning behavior in MSR 4 differs fundamentally from earlier versions.  
While previous releases used pruning policies to remove images that matched defined criteria,  
MSR 4 introduces retention policies, which are based on preserving images that meet certain tag patterns.

Use the mapping guide below to manually translate existing pruning rules into MSR 4 retention policies.

### Operator Mapping Table

| Operator Name | MSR 2.9 / MSR 3.1 Pruning Operator | Regex Equivalent | MSR 2.9 / MSR 3.1 → MSR 4 Translation (Prune = Not Retain) | MSR 4 Time Frame (`template` field) | MSR 4 Conversion to "doublestar" kind |
|----------------|------------------------------------|------------------|-------------------------------------------------------------|--------------------------------------|---------------------------------------|
| equals | eq | matching + exact value | P if equal value = NOT R if equal value = exclude x if equal value | always | use exact value |
| starts with | sw | matching + "^" + value + "*" | exclude x if starts with value | always | `value*` |
| ends with | ew | matching + "*" + value + "$" | exclude x if ends with value | always | `*value` |
| contains | c | matching + "" + value + "" | exclude x if contains value | always | `\value\` |
| one of | oo | matching + `\b(word1\|word2\|word3)\b` | exclude x if one of value | always | Use exact value multiple times |
| not one of | noo | excluding + `\b(word1\|word2\|word3)\b` | match x if one of value | always | Use exact value multiple times |
| matches regex | matches | matching + regex value | exclude x if match value | always | None |

### Supported MSR 2.9 and MSR 3.1 Rule Types in MSR 4

| MSR 2.9 / MSR 3.1 Rule Type | MSR 4 Mapping |
|------------------------------|---------------|
| Tag Name | Tags field |
| Component Name | For repositories |
| All CVSS 3 vulnerabilities | None |
| Critical CVSS 3 vulnerabilities | None |
| High CVSS 3 vulnerabilities | None |
| Medium CVSS 3 vulnerabilities | None |
| Low CVSS 3 vulnerabilities | None |
| License name | None |
| Last updated at | None |

## Configure Environment

The following infrastructure components require manual updates to align with the new MSR setup:

| Infrastructure Component | Required Actions |
|----------------------------|------------------|
| **CI/CD Pipelines** | Update custom CICD pipelines to leverage the new environments. |
| **DNS** | Update DNS CNAMEs to point to the new hosts after migration. |
