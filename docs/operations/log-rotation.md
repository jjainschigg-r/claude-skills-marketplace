# Log Rotation in Mirantis Secure Registry

Mirantis Secure Registry (MSR) maintains a comprehensive audit log of all image
pull, push, and delete operations. To effectively manage these logs, MSR
provides functionalities to configure audit log retention periods and to
forward logs to a syslog endpoint.

## Scheduling Log Purge

To schedule a log purge in MSR:

1. **Access the MSR Interface**  
   Log in with an account that has system administrator privileges.

2. **Navigate to Administration**

    - Select **Clean Up**.

3. **Select Log Rotation**

    - Select the **Schedule to purge** drop-down menu, choose the desired
      frequency for log rotation:

      - **None**: No scheduled log rotation.  
      - **Hourly**: Executes at the start of every hour.  
      - **Daily**: Executes daily at midnight.  
      - **Weekly**: Executes every Saturday at midnight.  
      - **Custom**: Define a custom schedule using a cron expression.

    - To adjust the audit log retention period, select **Keep records in**,  
      specify the duration to retain audit logs.

      - Choose between **Hours** or **Days**.  
      - For instance, setting this to 7 days will purge audit logs older than  
        7 days.

    - Under **Included Operations**, select the operations to include in the  
      purge:

      - **Create**  
      - **Delete**  
      - **Pull**

    - Click **Save** to apply the log rotation schedule.

4. **Optional Actions**

    - **Dry Run**: Click **DRY RUN** to simulate the purge and view the  
      estimated number of logs that would be deleted.  
    - **Immediate Purge**: Click **PURGE NOW** to execute the purge  
      immediately, bypassing the scheduled time.

## Viewing Log Rotation History

To review the history of log purges:

1. **Access the Purge History**:

    - Navigate to **Administration → Clean Up → Log Rotation**.
    - The **Purge History** table displays details of each purge, including:

        - **Task ID**: Unique identifier for each purge operation.  
        - **Trigger Type**: Indicates whether the purge was initiated manually  
          or by schedule.  
        - **Dry Run**: Specifies if the purge was a dry run.  
        - **Status**: Current status of the purge operation.  
        - **Creation Time**: Timestamp when the purge started.  
        - **Update Time**: Timestamp of the last update to the purge operation.  
        - **Logs**: Links to detailed logs generated during the purge.

## Stopping an In-Progress Log Rotation

To halt a running log purge operation:

1. **Access the Purge History**:

    - Navigate to **Administration → Clean Up → Log Rotation**.

2. **Select the Running Purge Task**:

    - In the **Purge History** table, locate the running purge operation.  
    - Check the box next to the corresponding **Task ID**.

3. **Stop the Purge**:

    - Click **Stop**.

        - Confirm the action when prompted.  
        - Note: Stopping the purge will cease further processing, but any logs  
          already purged will not be restored.

## Configuring Audit Log Forwarding

To forward audit logs to a syslog endpoint:

1. **Access System Settings**:

    - Log in with system administrator privileges.  
    - Navigate to **Configuration → System Settings**.

2. **Set Syslog Endpoint**:

    - In the **Audit Log Forward Endpoint** field, enter the syslog endpoint,  
      for example, **harbor-log:10514**.

3. To skip storing audit logs in the MSR database and forward them directly to  
   the syslog endpoint:

    - Select the **Skip Audit Log Database** checkbox.  
    - This action ensures that all audit logs are forwarded immediately to the  
      specified endpoint without being stored in the MSR database.

For more detailed information, refer to the Harbor documentation on  
Log Rotation.
