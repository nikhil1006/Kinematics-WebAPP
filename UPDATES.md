### Updates

1. Modified the **`app.py`** script to parallelize the computation of joint angles using Ray.
    - Imported the **`ray`** library and initialized it.
    - Created a remote function **`compute_joint_angles`** for parallel computation.
    - Used **`ray.get()`** and **`ray.wait()`** for parallel computation and error handling.
2. Updated the **`requirements.txt`** file to include the Ray library.
    - Added **`ray==1.7.0`** to the **`requirements.txt`** file.
3. Built and ran the Docker container with the updated application.
    - Created a new Docker image called **`inversekinematics-v1`** based on the modified code.
    - Ran the Docker container using the new image.
4. Pushed the updated Docker image to Amazon Elastic Container Registry (ECR).
    - Tagged the new Docker image.
    - Pushed the tagged image to the ECR repository.
5. Updated the Amazon Elastic Kubernetes Service (EKS) to use the new Docker image.
    - Modified the Kubernetes deployment file to reference the new image.
    - Applied the changes using **`kubectl apply`**.
    - Monitored the deployment status using **`kubectl rollout status`**.
    - Troubleshot issues with the deployment, such as the Progress Deadline Exceeded error.
6. Discussed the relationship between ECR and EKS in detail.
    - Explained how ECR stores Docker images and EKS uses those images to deploy and manage containerized applications.
7. Addressed concerns with the Jenkins pipeline that was attempted earlier.
    - Reviewed the pipeline stages and potential issues with the build.

## **7. Jenkins Integration**

### **7.1. Setting up Jenkins**

1. Install Jenkins on your local machine or server.
2. Configure the necessary plugins (GitHub, Docker, etc.).
3. Set up necessary credentials for Docker Hub and GitHub.

    ### **7.2. Creating a Jenkins Pipeline**

1. Create a new Jenkins Pipeline job.
2. Set the build trigger to Poll SCM or use webhooks.
3. Add the following pipeline script:

```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from the Git repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                script {
                    dockerImage = docker.build("your-dockerhub-username/your-image-name")
                }
            }
        }

        stage('Test') {
            steps {
                // Run the tests (if any)
            }
        }

        stage('Deploy') {
            steps {
                // Push the Docker image to Docker Hub
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        dockerImage.push("latest")
                    }
                }
            }
        }
    }
}

```

1. Save and execute the pipeline.

### **7.3. Troubleshooting Jenkins (continued)**

If the pipeline fails, check the console output for errors. Common issues include:

- Invalid or expired credentials: Make sure the credentials you provided are correct and up-to-date.
- Missing plugins: Ensure you have installed and configured all necessary plugins for Jenkins.
- Networking issues: Check your internet connection and any firewall settings that might be affecting Jenkins.
- Misconfiguration: Verify that your pipeline script is correct and properly configured.

If you cannot resolve the issue based on the error message, try searching for the error online or consult the Jenkins documentation for further guidance.

### 7.4. **Jenkins Integration (Failed)**

During the integration process with Jenkins, we faced the following error:

```lua

Caused: java.io.IOException: Cannot run program "docker": error=2, No such file or directory
```

The error indicates that Jenkins cannot find the "docker" command in its environment. This is likely due to either the Docker installation being missing or the Docker executable not being included in the system PATH.

Unfortunately, we were unable to resolve the issue and successfully integrate Jenkins with our project. Therefore, we need to look for alternative CI/CD tools.

### 7.5. **To-Do: Research and Integrate Alternative CI/CD Tool**

As Jenkins did not work for our specific use case, we need to research and explore other CI/CD tools that can be integrated with our project. Some popular alternatives to Jenkins are:

- [ ]  GitLab CI/CD
- [ ]  Travis CI
- [ ]  CircleCI
- [ ]  GitHub Actions
- [ ]  Azure Pipelines

It is essential to choose a CI/CD tool that fits our project requirements, can be easily integrated, and has good documentation and support.

To integrate Terraform into your project, follow these steps:

1. Install Terraform: First, download and install Terraform on your local machine. You can follow the instructions from the official Terraform website: **[https://learn.hashicorp.com/tutorials/terraform/install-cli](https://learn.hashicorp.com/tutorials/terraform/install-cli)**
2. Create a Terraform configuration file: In your project directory, create a new directory called **`terraform`**. Inside this folder, create a file named **`main.tf`**. This file will contain your Terraform configuration code. You can also create other **`.tf`** files if you want to organize your infrastructure configuration.
3. Write the Terraform configuration: Define the resources you want to create, update, or delete using the Terraform configuration language (HCL). In the **`main.tf`** file, you need to specify the provider (e.g., AWS) and define the resources.

Example **`main.tf`** for creating an AWS S3 bucket:

```
hclCopy code
provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-example-bucket"
  acl    = "private"
}

```

Replace the example code with the resources you need for your specific use case.

1. Initialize the Terraform working directory: Run **`terraform init`** in the **`terraform`** directory. This command downloads the required provider plugins and sets up the backend for storing your Terraform state.
2. Validate and format the configuration: Run **`terraform validate`** to check if the configuration is valid, and **`terraform fmt`** to automatically format the configuration files to make them consistent and easy to read.
3. Plan the changes: Run **`terraform plan`** to see what changes Terraform will apply to your infrastructure. Review the output to ensure it matches your expectations.
4. Apply the changes: Run **`terraform apply`** to create, update, or delete the resources specified in your configuration files. This command will prompt you to confirm before executing the changes. Type **`yes`** to proceed.
5. (Optional) Store your Terraform state remotely: By default, Terraform stores the state of your infrastructure in a local file called **`terraform.tfstate`**. To store the state remotely (e.g., in an S3 bucket), you can configure a backend in your **`main.tf`** file. Storing state remotely is essential when working in a team to prevent conflicts and inconsistencies.

Example of configuring the S3 backend:

```
hclCopy code
terraform {
  backend "s3" {
    bucket = "my-terraform-state-bucket"
    key    = "path/to/my/key"
    region = "us-west-2"
  }
}

```

Replace the example values with your actual S3 bucket, key, and region.

1. (Optional) Integrate Terraform with CI/CD: If you want to automate the process of applying infrastructure changes, you can integrate Terraform with your CI/CD pipeline. In the case of GitHub Actions, you can create a new workflow that runs on specific events (e.g., push to the main branch), and executes the necessary Terraform commands (**`init`**, **`validate`**, **`fmt`**, **`plan`**, and **`apply`**).

Remember to store your AWS credentials and other sensitive information as GitHub Secrets, and inject them into your GitHub Actions environment variables.

Regenerate response