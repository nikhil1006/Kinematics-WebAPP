# **Inverse Kinematics Web Application**

This web application demonstrates inverse kinematics functionality for a 2D robotic arm simulation. It uses a Flask server on the backend, HTML, CSS & JavaScript on the frontend, and p5.js for interactive visualization. The application is containerized using Docker and deployed on Amazon EKS using Kubernetes.

## **Prerequisites**

1. Install **[Docker](https://www.docker.com/get-started)**
2. Install **[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)** (if you haven't already)
3. Install **[kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)** (for Kubernetes deployment)
4. Install and configure **[AWS CLI](https://aws.amazon.com/cli/)** (for Amazon EKS deployment)

## **Setup and Running the Application Locally**

1. Clone the repository:
    
    ```bash
    git clone https://github.com/nikhil1006/Kinematics-WebAPP.git
    cd Kinematics-WebAPP
    
    ```
    
2. Build the Docker image: **`docker build -t your-image-name .`**
    
    Replace **`your-image-name`** with a name of your choice for the Docker image.
    
3. Run the Docker container: **`docker run -p 5000:5000 your-image-name`**
    
    If port 5000 is already in use, you can choose another port, e.g., **`-p 5001:5000`**, and update your application configuration accordingly.
    
4. Access the application in your browser by navigating to **`http://localhost:5000`**.

## **Deployment to Amazon EKS (Kubernetes)**

1. Create an Amazon ECR repository for your Docker image.
2. Push the Docker image to the Amazon ECR repository.
3. Create an Amazon EKS cluster.
4. Configure kubectl to use the new EKS cluster.
5. Create the necessary Kubernetes YAML files for deployment and service (LoadBalancer).
6. Apply the Kubernetes YAML files using **`kubectl apply`**.
7. Retrieve the external IP of the LoadBalancer service and access the application in your browser.

## **Development**

When making changes to the application:

1. Rebuild the Docker image.
2. Run the updated Docker container.
3. Test your changes by accessing the application in your browser.
4. For Amazon EKS deployment, push the updated Docker image to the Amazon ECR repository and update the Kubernetes deployment.

## **Troubleshooting**

If you encounter an error about the port being already in use, follow these steps:

1. Find the process using the port and stop it:
- On Linux/macOS:
    
    ```bash
    sudo lsof -i :5000
    sudo kill [PID]
    ```
    
    Replace **`[PID]`** with the process ID from the first command.
    
- On Windows:
    
    ```powershell
    netstat -a -n -o | findstr :5000
    taskkill /F /PID [PID]
    ```
    
    Replace **`[PID]`** with the process ID from the first command.
    
1. Alternatively, use a different port for your application, updating both the Docker run command and the application configuration as necessary.

## **License**

This project is licensed under the MIT License.