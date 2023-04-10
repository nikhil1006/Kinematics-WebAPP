pipeline {
    agent { label 'master-node' }
    stages {
        stage('Prepare') {
            steps {
                script {
                    checkout scm
                    def myImage = docker.build 'python:3.9'
                    myImage.inside('-u root:root') {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image('python:3.9').inside('-u root:root') {
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

// pipeline {
//     agent {
//         docker {
//             image 'python:3.9'
//             args '-u root:root'
//         }
//     }
//     stages {
//         stage('Prepare') {
//             steps {
//                 sh 'pip install -r requirements.txt'
//             }
//         }
//         stage('Test') {
//             steps {
//                 sh 'pytest'
//             }
//         }
//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
//                         def app = docker.build("prasanna1006/inversekinematics:latest")
//                         app.push("latest")
//                     }
//                 }
//             }
//         }
//         stage('Deploy to Minikube') {
//             steps {
//                 sh '''
//                     minikube start
//                     kubectl config use-context minikube
//                     kubectl apply -f deployment.yaml
//                     kubectl apply -f service.yaml
//                 '''
//             }
//         }
//         stage('Deploy to EKS') {
//             steps {
//                 withCredentials([usernamePassword(credentialsId: 'aws-iam-creds', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
//                     sh '''
//                         aws eks update-kubeconfig --region us-east-1 --name inversekinematics-cluster
//                         kubectl config use-context arn:aws:eks:us-east-1:000065695109:cluster/inversekinematics-cluster
//                         kubectl apply -f deployment.yaml
//                         kubectl apply -f service.yaml
//                     '''
//                 }
//             }
//         }
//     }
// }
