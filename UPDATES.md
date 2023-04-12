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