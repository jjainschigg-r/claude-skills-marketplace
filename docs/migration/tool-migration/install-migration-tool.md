# Install Migration Tool

To install the migration tool:

1. Download the migration tool image:

   ```bash
   docker pull registry.mirantis.com/msrh/migrate:latest
   ```

2. Verify if the pulled image is valid by running `help` command:

   ```bash
   docker run -it --rm registry.mirantis.com/msrh/migrate:latest poetry run migration --help
   ```
