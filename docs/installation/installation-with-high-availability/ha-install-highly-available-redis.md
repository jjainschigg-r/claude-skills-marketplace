# Install highly available Redis

1. Install the Redis Operator from the OT-Container-Kit Helm repository:

    ```bash
    helm install redis-operator redis-operator \
          --repo https://ot-container-kit.github.io/helm-charts
    ```

2. Generate a strong, random password for authenticating with Redis:

    ```bash
    PASSWORD=$(LC_ALL=C tr -dc A-Za-z0-9 </dev/urandom | head -c 24)
    ```

3. Create a Kubernetes secret to securely store the password:

    ```bash
    kubectl create secret generic msr-redis-secret \
       --from-literal=REDIS_PASSWORD=${PASSWORD}
    ```

4. Deploy the Redis instance:

    !!! note

        Set `clusterSize` to the desired number of Redis nodes.

    ```bash
    helm install -i msr-redis redis-replication \
        --repo https://ot-container-kit.github.io/helm-charts \
        --set redisReplication.clusterSize=3 \
        --set redisReplication.redisSecret.secretName=msr-redis-secret \
        --set redisReplication.redisSecret.secretKey=REDIS_PASSWORD \
        --set redisReplication.image=quay.io/opstree/redis \
        --set redisReplication.tag=v8.2.2
    ```

5. Retrieve the connection details for the Redis service:

    **Get the service's port number:**

    ```bash
    kubectl get svc msr-redis -o jsonpath={.spec.ports..port}
    ```
   
## Upgrade highly available Redis

1. Verify Redis version:

    ```bash
    kubectl get pod <Redis Pod> -o jsonpath='{.spec.containers[*].image}'
    ```

2. Upgrade Redis:

    ```bash
    helm upgrade msr-redis redis-replication \
      --repo https://ot-container-kit.github.io/helm-charts \
      --set redisReplication.clusterSize=3 \
      --set redisReplication.redisSecret.secretName=msr-redis-secret \
      --set redisReplication.redisSecret.secretKey=REDIS_PASSWORD \
      --set redisReplication.image=quay.io/opstree/redis \
      --set redisReplication.tag=v8.2.2
    ```

    !!! note

        Mirantis recommends installing Redis version 8.2.2 or the
        latest validated release. For more options, refer to the official
        [redis-operator page](https://github.com/OT-CONTAINER-KIT/redis-operator).
