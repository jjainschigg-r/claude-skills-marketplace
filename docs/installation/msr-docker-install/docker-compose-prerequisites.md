# Prerequisites

To ensure that all of the key prerequisites are met:

- Verify that your system is running a Linux-based operating system.  
  Recommended distributions include Red Hat Enterprise Linux (RHEL), Rocky
  Linux, and Ubuntu.

- Verify the Docker installation. If Docker is not installed, run:

    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    ```

- Verify the Docker Compose installation:

    !!! note 

        If you are using Docker Compose v1, replace all instances of
        `docker compose` with `docker-compose` in the relevant steps
        of the installation procedure.

    ```bash
    docker compose
    ```

    If the command returns help information, Docker Compose is already installed.
    Otherwise, install Docker Compose:

    ```bash
    sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d '"' -f 4)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    ```

- Ensure the following ports are available and not blocked by firewalls:

    | Port  | Protocol | Description|
    |-------|----------|------------|
    | 443   | HTTPS    | Harbor portal and core API accept HTTPS requests on this port.                       |
    | 80    | HTTP     | Harbor portal and core API accept HTTP requests on this port if SSL is not configured. |
    | 4443  | HTTPS    | Connections required for administrative purposes.                                    |
