pipeline {
    agent { label 'master-node' }
    environment {
        DOCKER_IMAGE = 'python:3.9'
    }
    stages {
        stage('Prepare') {
            steps {
                script {
                    checkout scm
                    def myImage = docker.build("${DOCKER_IMAGE}")
                    myImage.inside('-u root:root --entrypoint ""') {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").inside('-u root:root --entrypoint ""') {
                        sh 'pytest'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        def app = docker.build("prasanna1006/inversekinematics:latest")
                        app.push("latest")
                    }
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                sh '''
                    minikube start
                    kubectl config use-context minikube
                    kubectl apply -f deployment.yaml
                    kubectl apply -f service.yaml
                '''
            }
        }
        stage('Deploy to EKS') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'aws-iam-creds', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh '''
                        aws eks update-kubeconfig --region us-east-1 --name inversekinematics-cluster
                        kubectl config use-context arn:aws:eks:us-east-1:000065695109:cluster/inversekinematics-cluster
                        kubectl apply -f deployment.yaml
                        kubectl apply -f service.yaml
                    '''
                }
            }
        }
    }
}
