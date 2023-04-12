# Command Cheat Sheet

1. Flask application and Ray setup:
    - **`pip install flask ray`**
2. Jenkins setup:
    - Install Jenkins using Homebrew: **`brew install jenkins`**
    - Start Jenkins: **`brew services start jenkins`**
    - Open a web browser and go to **`http://localhost:8080`** to complete the Jenkins setup.
3. Docker-related commands:
    - **`docker build -t <image-name> .`** (Build Docker image)
    - **`docker run -p 80:5000 <image-name>`** (Run Docker container locally)
    - **`docker login`** (Log in to Docker Hub)
    - **`docker tag <image-name>:<tag-name> <dockerhub-username>/<repository-name>:<tag-name>`** (Tag Docker image)
    - **`docker push <dockerhub-username>/<repository-name>:<tag-name>`** (Push Docker image to Docker Hub)
4. Minikube-related commands:
    - **`minikube start`** (Start Minikube)
    - **`kubectl create -f deployment.yaml`** (Create Kubernetes deployment)
    - **`kubectl get pods`** (Check the status of pods)
    - **`kubectl apply -f service.yaml`** (Create Kubernetes service)
    - **`minikube service <service-name> --url`** (Get the URL of the application running on Minikube)
5. Amazon Web Services (AWS) related commands:
    - **`aws ecr get-login-password | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.<region>.amazonaws.com`** (Log in to Amazon ECR)
    - **`docker tag <image-name> <aws-account-id>.dkr.ecr.<region>.amazonaws.com/<repository-name>`** (Tag Docker image for ECR)
    - **`docker push <aws-account-id>.dkr.ecr.<region>.amazonaws.com/<repository-name>`** (Push Docker image to ECR)
6. Kubernetes on AWS (EKS) related commands:
    - **`aws eks update-kubeconfig --region <region> --name <cluster-name>`** (Configure kubectl to use EKS cluster)
    - **`kubectl config use-context <context-name>`** (Switch kubectl context to EKS cluster)
    - **`kubectl apply -f deployment.yaml`** (Deploy the application to EKS)
    - **`kubectl apply -f service.yaml`** (Create a LoadBalancer service on EKS)
    - **`kubectl get svc`** (Get the external IP address of the LoadBalancer service)

This updated command cheat sheet incorporates the steps for setting up Jenkins on macOS.