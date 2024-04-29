**Title: Getting Started with Pulumi on AWS**

**Prerequisites**

* **AWS Account:** If you don't have one, sign up at [https://aws.amazon.com/](https://aws.amazon.com/)
* **AWS Credentials:** Set up an IAM user with programmatic access. Keep access keys secure. See AWS IAM Docs: [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).
* **Pulumi CLI:** Install following the instructions at [https://www.pulumi.com/docs/get-started/install/](https://www.pulumi.com/docs/get-started/install/)

**Configure Pulumi for AWS**

1. **Export Credentials:** 
   ```bash
   export AWS_ACCESS_KEY_ID=your_access_key_id
   export AWS_SECRET_ACCESS_KEY=your_secret_access_key

   #windows powershell
   $env:AWS_ACCESS_KEY_ID = "your_access_key_id" 
   $env:AWS_SECRET_ACCESS_KEY = "your_secret_access_key"
   ```
   **Important:** Replace placeholders with your actual credentials.

2. **(Optional) Set AWS Region:** If you want to work with a region other than the default:
    ```bash
    export AWS_REGION=your_preferred_region 

    #windows
    $env:AWS_REGION = "your_preferred_region"
    ```
    See available region codes in AWS documentation. 

**You're ready to start using Pulumi for AWS!**

**Additional Notes:**

* The Pulumi AWS provider automatically uses these environment variables for authentication.
* You can alternatively use `pulumi config` commands for more persistent configuration.

