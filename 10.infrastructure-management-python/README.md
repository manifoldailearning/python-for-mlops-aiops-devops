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

# Commands for Hands On - Pulumi on AWS


**Step 1: Create a New Pulumi Project**

1. Create a new directory for your project:
   ```bash
   mkdir my-pulumi-project
   cd my-pulumi-project
   ```

2. Initialize a Pulumi project using Python:
   ```bash
   pulumi new aws-python
   ```
   * Choose a project name, description, and a default stack name (`dev`).
   * Accept or provide a value for the AWS region.

**Step 2: Review the Project Structure**

* **\_\_main\_\_.py:** Your main Python file
* **Pulumi.yaml:** Contains project-level configuration
* **Pulumi.(stack-name).yaml:** Contains stack-specific configuration (e.g., `Pulumi.dev.yaml`)

**Step 3: Implement an S3 Bucket**

1. Install the Pulumi AWS package:
   ```bash
   pip install pulumi_aws
   ```

2. Edit your `__main__.py` file, adding the following code:

   ```python
   import pulumi
   import pulumi_aws as aws

   # Create an S3 bucket
   bucket = aws.s3.Bucket("my-bucket")

    # Export the name of the bucket
   pulumi.export('bucket_name', bucket.id)
   ```


**Step 3: Deploy Your First Stack**

- Deploy your resources to AWS:
   ```bash
   pulumi up
   pulumi stack output bucket_name
   ```

**Step 4: Modify Your Program**

1. Open your project's `__main__.py` 
2. add new index.html file and modify the code as below
```python
# Create an S3 Bucket object
bucketObject = s3.BucketObject(
    'index.html',
    bucket=bucket.id,
    source=pulumi.FileAsset('./index.html')
)
```


3. Save your changes.

**Step 5: Deploy Your Changes**

- Apply the updates to your AWS infrastructure:
   ```bash
   pulumi up --yes
   ```

**Step 6: Destroy Your Stack**

1. To remove all resources created by Pulumi:
   ```bash
   pulumi destroy 
   ```

