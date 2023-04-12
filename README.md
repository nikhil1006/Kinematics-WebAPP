# **Inverse Kinematics Flask Web Application**

This guide will walk you through the process of creating a Flask web application for a 2D inverse kinematics simulation, starting with a simple Python script and ending with the application hosted on an AWS EKS cluster.

## Overview

1. Creating a Flask Web Application
2. Adding P5.js for Visualization
3. Dockerizing the Flask Application
4. Running the App Locally with Minikube
5. Deploying the App on AWS EKS

## **1. Creating a Flask Web Application**

### **1.1. Setting up the Project Structure**

Create the following project structure:

```markdown
.
├── CHEATSHEET.md
├── Dockerfile
├── README.md
├── ROADMAP.MD
├── app.py
├── k8s
│   ├── deployment.yaml
│   └── service.yaml
├── log.txt
├── requirements.txt
├── static
│   ├── css
│   │   └── style.css
│   ├── images
│   │   ├── figure_0.png
│   │   ├── figure_1.png
│   │   ├── figure_2.png
│   │   ├── figure_3.png
│   │   ├── figure_4.png
│   │   ├── figure_5.png
│   │   ├── figure_6.png
│   │   ├── figure_7.png
│   │   ├── figure_8.png
│   │   └── figure_9.png
│   └── js
│       ├── app.js
│       └── visualization.js
└── templates
    ├── index.html
    ├── results.html
    └── visualization.html
```

### **1.2. Flask Application Code**

In **`app.py`**, add the following code:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    # Get form data from request
    length_1 = float(request.form['length1'])
    length_2 = float(request.form['length2'])
    x = float(request.form['x'])
    y = float(request.form['y'])

    # Perform calculations
    theta_2 = acos((x**2 + y**2 - length_1**2 - length_2**2) / (2 * length_1 * length_2))
    theta_1 = atan2(y, x) - atan2((length_2 * sin(theta_2)), (length_1 + length_2 * cos(theta_2)))
    theta_1 = degrees(theta_1)
    theta_2 = degrees(theta_2)

    # Render results template with calculated angles
    return render_template('results.html', theta1=theta_1, theta2=theta_2)

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

```

### **1.3. HTML Templates**

Create the **`index.html`** and **`visualization.html`** files inside the **`templates`** folder, following the content provided during the conversation.

### **1.4. CSS and JavaScript Files**

Add the **`style.css`** file inside the **`static/css`** folder, following the content provided during the conversation. Add any necessary JavaScript files in the **`static/js`** folder.

### **1.5. Install Dependencies and Run the App**

In the **`requirements.txt`** file, add the following dependencies:

```
Flask==2.2.3
matplotlib==3.7.1
matplotlib-inline==0.1.6
pandas==1.5.3
```

(feel free to add or remove any dependencies)

nstall the dependencies and run the app:

```bash
pip install -r requirements.txt
python3 app.py
```

## **2. Adding P5.js for Visualization**

### **2.1. Setting up P5.js**

In the **`visualization.html`** file, add the following script tags in the **`<head>`** section:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/addons/p5.dom.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/addons/p5.sound.min.js"></script>
```

### **2.2. Adding Visualization Code**

Add the P5.js visualization code to **`visualization.html`**. Modify the **`app.js`** file accordingly to handle the "View Visualization" button click.

## **3. Dockerizing the Flask Application**

### **3.1. Creating a Dockerfile**

Create a **`Dockerfile`** in the project root directory with the following content:

```docker
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
```

### **3.2. Building and Running the Docker Image**

Build and run the docker image:

```bash
docker build -t your-image-name .
docker run -d -p 80:5000 --name my_app_instance your-image-name
```

## **4. Running the App Locally with Minikube**

### **4.1. Installing Minikube and Kubernetes CLI (kubectl)**

Install **[Minikube](https://minikube.sigs.k8s.io/docs/start/)** and **[kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)**.

### **4.2. Creating Kubernetes Configuration Files**

Create the following YAML configuration files:

- **`deployment.yaml`**
- **`service.yaml`**

### **4.3. Starting Minikube and Deploying the App**

Start Minikube:

```bash
minikube start
```

Deploy Using the config files:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Get the Minikube URL:

```bash
minikube service flask-app --url
```

Access the application using the URL provided.

## **5. Deploying the App on AWS EKS**

### **5.1. Prerequisites**

- AWS CLI installed and configured
- kubectl installed
- eksctl installed
- Docker Hub account

### **5.2. Pushing Docker Image to Docker Hub**

Tag and push your Docker image to Docker Hub:

```bash
docker tag your-image-name your-dockerhub-username/your-image-name
docker push your-dockerhub-username/your-image-name
```

### **5.3. Creating an Amazon EKS Cluster**

Create an Amazon EKS cluster using eksctl:

```bash
eksctl create cluster --name your-cluster-name --region your-region
```

### **5.4. Configuring kubectl for the EKS Cluster**

Configure `kubectl` to use the new cluster:

```bash
aws eks update-kubeconfig --region your-region --name your-cluster-name
```

### **5.5. Deploying the Application**

Update the **`deployment.yaml`** file with the Docker Hub image name. Apply the Kubernetes configuration files to the EKS cluster:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### **5.6. Accessing the Application**

Get the external IP address of the LoadBalancer:

```bash
kubectl get svc flask-app
```
## **6. Adding Ray for Parallel Computation**

### **6.1. Modifying the Flask Application**

Modify the **`app.py`** script to parallelize the computation of joint angles using Ray:

```python
import ray
from ray.util import ActorPool

ray.init()

@ray.remote
def compute_joint_angles(length_1, length_2, x, y):
    # Perform calculations
    theta_2 = acos((x**2 + y**2 - length_1**2 - length_2**2) / (2 * length_1 * length_2))
    theta_1 = atan2(y, x) - atan2((length_2 * sin(theta_2)), (length_1 + length_2 * cos(theta_2)))
    theta_1 = degrees(theta_1)
    theta_2 = degrees(theta_2)

    return theta_1, theta_2

@app.route('/results', methods=['POST'])
def results():
    # Get form data from request
    length_1 = float(request.form['length1'])
    length_2 = float(request.form['length2'])
    x = float(request.form['x'])
    y = float(request.form['y'])

    # Call remote function
    joint_angle_results = compute_joint_angles.remote(length_1, length_2, x, y)

    # Retrieve results and handle exceptions
    ready_results, remaining_results = ray.wait([joint_angle_results], num_returns=1, timeout=None)
    try:
        theta_1, theta_2 = ray.get(ready_results[0])
    except Exception as e:
        return str(e)

    # Render results template with calculated angles
    return render_template('results.html', theta1=theta_1, theta2=theta_2)

```

### **6.2. Updating requirements.txt**

Update the **`requirements.txt`** file to include the Ray library:

```
ray
```

### **6.3. Rebuilding and Running the Docker Image**

Build and run the Docker container with the updated application:

```bash
docker build -t your-new-image-name .
docker run -d -p 80:5000 --name my_new_app_instance your-new-image-name
```

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

## **8. Troubleshooting**

### **8.1. Docker Issues**

- **Cannot access the application after running the Docker container**: Check if the application is running within the container using **`docker logs <container_name>`** and make sure that the host and container ports are correctly mapped when running **`docker run`**.
- **Docker build error**: Review your **`Dockerfile`** and ensure all dependencies are installed correctly. Check if the base image is compatible with your application.

### **8.2. AWS EKS Issues**

- **Application not accessible after deploying to EKS**: Verify that the **`LoadBalancer`** service is running and has a valid external IP address using **`kubectl get svc`**. Also, check your **`deployment.yaml`** and **`service.yaml`** files for any configuration errors.
- **Deployment errors or stuck deployments**: Use **`kubectl describe deployment <deployment_name>`** to get more information about the error. Check your deployment configurations and make sure the Docker image is accessible.

### **8.3. Ray Issues**

- **Ray initialization error**: Ensure that Ray is properly installed and that the version is compatible with your Python environment. Verify that there are no conflicts with other libraries in your **`requirements.txt`** file.
- **Ray remote function error**: Make sure the remote function is properly defined and decorated with **`@ray.remote`**. Check that the function arguments and return values are consistent with your application logic.

### **8.4. Jenkins Issues**

- **Pipeline failure**: Analyze the console output and identify the failing stage. Check the pipeline script and configurations for any errors or missing information.
- **Build trigger issues**: Ensure that the build trigger (Poll SCM or webhook) is properly configured. Check your webhook settings on your Git repository and the Jenkins job configuration.

## **9. Conclusion**

This guide has walked you through the process of creating a Flask web application for a 2D inverse kinematics simulation, including parallelizing computation with Ray, deploying the application to AWS EKS, and setting up a Jenkins pipeline for continuous integration and deployment.

Feel free to adapt and expand on this guide for your own projects, and don't hesitate to ask for help if you encounter any issues along the way.
Access the application using the external IP in your browser.


