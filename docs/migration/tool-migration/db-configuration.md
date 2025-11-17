# Database Access Configuration

This guide assumes you are working on a dedicated migration workstation, a
machine with access to both the source and destination environments, used
for managing the migration.

## Configure PostgreSQL access

To enable access to the MSR 4.x PostgreSQL instance:

1. Update any required inbound firewall rules to allow PostgreSQL traffic.

    !!! note

        Before running `kubectl` commands, source the client bundle by
        exporting the `kubeconfig` file that provides access to the target MSR 4
        registry.

2. Retrieve the MSR 4 PostgreSQL credentials for the migration process:

    - Username:

      ```bash
      kubectl get secret \
        msr.msr-postgres.credentials.postgresql.acid.zalan.do \
        -o jsonpath="{.data.username}" | base64 --decode; echo
      ```

    - Password:

      ```bash
      kubectl get secret \
        msr.msr-postgres.credentials.postgresql.acid.zalan.do \
        -o jsonpath="{.data.password}" | base64 --decode; echo
      ```

    !!! note

        Connectivity will be validated in the later step.

3. Ensure that `socat` is installed on PostgreSQL worker nodes.

4. Identify the PostgreSQL leader Pod:

    ```bash
    kubectl exec msr-postgres-0 -- patronictl list | grep -i leader
    ```

5. Forward the port to expose PostgreSQL locally:

    ```bash
    kubectl port-forward pod/<LEADER-POD-NAME> 5432:5432
    ```

    Replace `<LEADER-POD-NAME>` with the actual Pod name returned in the previous
    command.

## Local database access

Before running the migration tool, you must first copy and run both the MKE
authorization store and the MSR database store locally.

To do so, complete the following steps on your local migration workstation:

1. Verify that a container runtime is installed, such as:

    - [Docker Desktop](https://docs.docker.com/desktop/)
    - [Mirantis Container Runtime (MCR)](https://docs.mirantis.com/mcr/current/install.html>)
    - [Docker CE](https://docs.docker.com/engine/install/)

2. Verify that [RethinkDB](https://rethinkdb.com/docs/install/) is
   installed.

3. Copy the `manage_source_registry_db.sh` script from the container image to
   your local machine. The script copies the eNZi and MSR databases and starts
   local instances. Because the script cannot run from within the container
   image, you must copy it to the local environment first.

    !!! note

        On **macOS**, the `manage_source_registry_db.sh` script requires
        `gnu-getopt`. Install the package by running the following command with
        Homebrew:

        ```bash
        brew install gnu-getopt
        ```

        After installation, follow the instructions to add `gnu-getopt` to your
        `PATH` before running the script.

    Example of copying the script, making it executable, and displaying its help
    information:

    ```bash
    docker run --rm registry.mirantis.com/msrh/migrate:latest cat utils/manage_source_registry_db.sh > manage_source_registry_db.sh

    chmod +x manage_source_registry_db.sh

    ./manage_source_registry_db.sh --help
    ```

4. Start the required local databases:

    !!! note

        You need to source a client bundle that has access to the source registry
        to use the copy commands.

    !!! info

        Both commands must be executed, and the processes must remain active
        throughout the migration. Select one of the following options to ensure
        they stay running:

        - Open each command in a separate terminal window or tab.
        - Run each command in the background by appending `&`.

    - Enzi database access:

      To copy and start a local Enzi database instance, run:

      ```bash
      ./manage_source_registry_db.sh --copy-enzidb --start-enzidb
      ```

    - MSR RethinkDB access:

      To copy and start a local MSR RethinkDB instance, run:

      ```bash
      ./manage_source_registry_db.sh --copy-msrdb --start-msrdb
      ```
