# Prepare MKE 3.x for MSR Installation

!!! info

    This procedure applies only to Kubernetes environments running  
    MKE 3.x. If you are using MKE 4.x, no additional preparation is  
    required before installing MSR.

To install MSR on MKE you must first configure both the  
`default:postgres-operator` user account and the  
`default:postgres-pod` service account in MKE 3.x with the  
**privileged** permission.

**To prepare MKE 3.x for MSR install:**

1.    Log in to the MKE web UI.  

2.    In the left-side navigation panel, click the **<username>**  
      drop-down to display the available options.  

3.    Click **Admin Settings > Privileges**.  

4.    Navigate to the **User account privileges** section.  

5.    Enter `<namespace-name>:postgres-operator` into the  
      **User accounts** field.  

      !!! note

          You can replace `<namespace-name>` with `default` to indicate  
          the use of the default namespace.  

6.    Select the **privileged** checkbox.  

7.    Scroll down to the **Service account privileges** section.  

8.    Enter `<namespace-name>:postgres-pod` into the  
      **Service accounts** field.  

      !!! note

          You can replace `<namespace-name>` with `default` to indicate  
          the use of the default namespace.  

9.    Select the **privileged** checkbox.  

10.   Click **Save**.  

!!! info

    For already deployed MSR instances, issue a rolling restart of  
    the `postgres-operator` deployment:  

    ```bash
    kubectl rollout restart deploy/postgres-operator
    ```
