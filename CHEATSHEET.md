# command cheat sheet

List of all commands used for the project 

1. Flask application setup:
    - `pip install flask`
2. Docker-related commands:
    - `docker build -t <image-name>` . (Build Docker image)
    - `docker run -p 5000:5000 <image-name>` (Run Docker container locally)
    - `docker login` (Log in to Docker Hub)
    - `docker tag <image-name> <dockerhub-username>/<repository-name>` (Tag Docker image)
    - `docker push <dockerhub-username>/<repository-name>` (Push Docker image to Docker Hub)
3. Minikube-related commands:
    - `minikube start` (Start Minikube)
    - `kubectl create -f deployment.yaml` (Create Kubernetes deployment)
    - `kubectl get pods` (Check the status of pods)
    - `kubectl apply -f service.yaml` (Create Kubernetes service)
    - `minikube service <service-name> --url` (Get the URL of the application running on Minikube)
4. Amazon Web Services (AWS) related commands:
    - `aws ecr get-login-password | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.<region>.amazonaws.com` (Log in to Amazon ECR)
    - `docker tag <image-name> <aws-account-id>.dkr.ecr.<region>.amazonaws.com/<repository-name>` (Tag Docker image for ECR)
    - `docker push <aws-account-id>.dkr.ecr.<region>.amazonaws.com/<repository-name>` (Push Docker image to ECR)
5. Kubernetes on AWS (EKS) related commands:
    - `aws eks update-kubeconfig --region <region> --name <cluster-name>` (Configure kubectl to use EKS cluster)
    - `kubectl config use-context <context-name>` (Switch kubectl context to EKS cluster)
    - `kubectl apply -f deployment.yaml` (Deploy the application to EKS)
    - `kubectl apply -f service.yaml` (Create a LoadBalancer service on EKS)
    - `kubectl get svc` (Get the external IP address of the LoadBalancer service)