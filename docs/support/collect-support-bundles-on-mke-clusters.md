# Collect Support Bundles on MKE Clusters

If your MSR4 instance runs on MKE, you can use any of the following methods to
obtain a support bundle.

## Obtain a full-cluster support bundle using the MKE web UI

1. Log in to the MKE web UI as an administrator.

2. In the left-side navigation panel, navigate to **<user name>** and click
   **Support Bundle**. The support bundle download will require several minutes
   to complete.

!!! note 

    The default name for the generated support bundle file is  
    `docker-support-<cluster-id>-YYYYmmdd-hh_mm_ss.zip`.  
    Mirantis suggests that you not alter the file name before submitting it to
    the customer portal. However, if necessary, you can add a custom string
    between `docker-support` and `<cluster-id>`, as in:  
    `docker-support-MyProductionCluster-<cluster-id>-YYYYmmdd-hh_mm_ss.zip`.

3. Submit the support bundle to Mirantis Customer Support by clicking
   **Share support bundle** on the success prompt that displays once the
   support bundle has finished downloading.

4. Fill in the Jira feedback dialog, and click **Submit**.

## Obtain a full-cluster support bundle using the MKE API

1. Create an environment variable with the user security token:

    ```bash
    export AUTHTOKEN=$(curl -sk -d \
    '{"username":"<username>","password":"<password>"}' \
    https://<mke-ip>/auth/login | jq -r .auth_token)
    ```

2. Obtain a cluster-wide support bundle:

    ```bash
    curl -k -X POST -H "Authorization: Bearer $AUTHTOKEN" \
    -H "accept: application/zip" https://<mke-ip>/support \
    -o docker-support-$(date +%Y%m%d-%H_%M_%S).zip
    ```

## Obtain a single-node support bundle using the CLI

Use SSH to log into a node and run:

```bash
MKE_VERSION=$((docker container inspect ucp-proxy \
--format '{{index .Config.Labels "com.docker.ucp.version"}}' \
2>/dev/null || echo -n {{{ latest_mke_tag }}})|tr -d [[:space:]])

docker container run --rm \
    --name ucp \
    -v /var/run/docker.sock:/var/run/docker.sock \
    --log-driver none \
    mirantis/ucp:${MKE_VERSION} \
    support > \
    docker-support-${HOSTNAME}-$(date +%Y%m%d-%H_%M_%S).tgz
```

!!! tip

    If SELinux is enabled, include the `--security-opt label=disable` flag.

!!! note

    The CLI-derived support bundle only contains logs for the node on which
    you are running the command. If you are running a
    [high availability](https://docs.mirantis.com/mke/current/ops/administer-cluster/join-nodes/set-up-high-availability.html>)
    MKE cluster, collect support bundles from all manager nodes.

## Obtain a support bundle using the MKE CLI with PowerShell:

Run the following command on Windows worker nodes to collect the support
information and have it placed automatically into a `.zip` file:

```bash
$MKE_SUPPORT_DIR = Join-Path -Path (Get-Location) -ChildPath 'dsinfo'
$MKE_SUPPORT_ARCHIVE = Join-Path -Path (Get-Location) -ChildPath $('docker-support-' + (hostname) + '-' + (Get-Date -UFormat "%Y%m%d-%H_%M_%S") + '.zip')
$MKE_PROXY_CONTAINER = & docker container ls --filter "name=ucp-proxy" --format "{{.Image}}"
$MKE_REPO = if ($MKE_PROXY_CONTAINER) { ($MKE_PROXY_CONTAINER -split '/')[0] } else { 'mirantis' }
$MKE_VERSION = if ($MKE_PROXY_CONTAINER) { ($MKE_PROXY_CONTAINER -split ':')[1] } else { '3.6.0' }
docker container run --name windowssupport `
-e UTILITY_CONTAINER="$MKE_REPO/ucp-containerd-shim-process-win:$MKE_VERSION" `
-v \\.\pipe\docker_engine:\\.\pipe\docker_engine `
-v \\.\pipe\containerd-containerd:\\.\pipe\containerd-containerd `
-v 'C:\Windows\system32\winevt\logs:C:\eventlogs:ro' `
-v 'C:\Windows\Temp:C:\wintemp:ro' $MKE_REPO/ucp-dsinfo-win:$MKE_VERSION
docker cp windowssupport:'C:\dsinfo' .
docker rm -f windowssupport
Compress-Archive -Path $MKE_SUPPORT_DIR -DestinationPath $MKE_SUPPORT_ARCHIVE
```
