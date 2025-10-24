# Signing Artifacts with Cosign

Artifact signing and signature verification are essential security measures
that ensure the integrity and authenticity of artifacts.  
MSR facilitates content trust through integrations with [Cosign](https://github.com/sigstore/cosign).  
This guide explains how to use Cosign to sign artifacts within MSR.

!!! note

    Project administrators can enforce content trust, requiring all artifacts
    to be signed before they can be pulled from an MSR registry.

## Using Cosign to Sign Artifacts

MSR integrates with **Cosign**, an OCI artifact signing and verification
solution that is part of the [Sigstore project](https://sigstore.dev/).  
Cosign signs OCI artifacts and uploads the generated signature to MSR, where
it is stored as an **artifact accessory** alongside the signed artifact.  
MSR maintains the link between the artifact and its Cosign signature, ensuring
consistent management, including tag retention and immutability rules.

### Key Features of Cosign Integration in MSR

- **Signature Management:** MSR treats Cosign signatures as artifact
  accessories, enabling consistent management alongside signed artifacts.  
- **Replication Support:** MSR replication includes both artifacts and their
  Cosign signatures.

  **Limitations:**
   - Vulnerability scans of Cosign signatures are **not supported**.  
   - Only **manual** and **scheduled** replication modes are supported; **event-based** replication is currently unsupported.

## Prerequisites

1. **Install Cosign:**  
   Ensure Cosign is installed on your local machine.  
   Refer to the [Cosign documentation](https://github.com/sigstore/cosign) for installation instructions.

2. **Generate a Private Key:**  
   Create a private key for signing artifacts.

## Signing and Uploading Artifacts with Cosign

1. **Log in to MSR:**  
   Authenticate with your MSR instance using Docker:

   `docker login <MSR-instance>`

   Replace `<MSR-instance>` with the URL of your MSR registry.

2. **Tag the Image:**  
   Tag your local image to match the MSR repository format:

   `docker tag <local-image> <MSR-instance>/<project>/<repository>:<tag>`

   Replace `<local-image>`, `<project>`, `<repository>`, and `<tag>` with your specific details.

3. **Push the Image to MSR:**  

   `docker push <MSR-instance>/<project>/<repository>:<tag>`

4. **Sign the Image with Cosign:**  

   `cosign sign --key cosign.key <MSR-instance>/<project>/<repository>:<tag>`

   You will be prompted to enter the password for your Cosign private key.

## Viewing Cosign Signatures in MSR

1. **Access the MSR Interface:** Log in to the MSR web interface.  
2. **Navigate to the Project:** Select the project containing the signed artifact.  
3. **Locate the Artifact:** Find the artifact in the repository list.  
4. **Expand Accessories:** Click the **>** icon next to the artifact to view
   the **Accessories** table, which lists all associated Cosign signatures.

## Deleting Cosign Signatures

**Individual Deletion:**

1. In the MSR interface, navigate to the project and locate the artifact.  
2. Expand the **Accessories** table.  
3. Click the **⋮** (three dots) next to the signature and select **Delete**.

