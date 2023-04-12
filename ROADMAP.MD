1. Created a Python Flask app for the inverse kinematics of a robotic arm:
    - Developed the backend using Python and the Flask framework.
    - Integrated Ray for parallel processing of inverse kinematics calculations.
    - Implemented the frontend using HTML, CSS, and JavaScript.
2. Incorporated a visualization feature using p5.js for the robotic arm simulation.
3. Set up a Jenkins pipeline for Continuous Integration and Continuous Deployment:
    - Installed and configured Jenkins on the local machine.
    - Created a Jenkins pipeline to build, test, and deploy the application.
    - Configured GitHub webhooks to trigger the Jenkins pipeline on code pushes.
4. Containerized the Flask application using Docker:
    - Created a Dockerfile to define the application container.
    - Built the Docker image using the Dockerfile.
    - Ran the Docker container locally to ensure the application works correctly.
5. Pushed the Docker image to Docker Hub.
6. Deployed the Flask application using Kubernetes:
    - Set up a local Kubernetes cluster using Minikube and deployed the application.
    - Verified that the application is running correctly on the local cluster.
7. Prepared the application for deployment on Amazon Web Services (AWS):
    - Created an Amazon ECR repository to store the application's Docker image.
    - Pushed the Docker image to the Amazon ECR repository.
8. Deployed the Flask application on AWS using Amazon Elastic Kubernetes Service (EKS):
    - Created an EKS cluster and configured kubectl to use the cluster.
    - Deployed the application to the EKS cluster using a deployment YAML file.
    - Exposed the application using a LoadBalancer service and a service YAML file.
    - Navigated to the external IP address to access the application.