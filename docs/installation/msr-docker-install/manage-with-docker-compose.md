# Manage MSR with Docker Compose

You can manage MSR services using Docker Compose commands. For example:

- To stop MSR services:

    ```bash
    sudo docker compose down
    ```

- To restart MSR services:

    ```bash
    sudo docker compose up -d
    ```

- To view service logs for troubleshooting:

    ```bash
    sudo docker compose logs <SERVICE-NAME>
    ```
