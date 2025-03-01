pipeline {
    agent any
    
    environment{
        IMAGE_NAME = "scientific-calculator"
        CONTAINER_NAME = "scientific-calc"
        REGISTRY = "meenalj21"
        DOCKER_CREDENTIALS = "docker-hub-credentials"
        RECIPIENT_EMAIL = "mpbjain@gmail.com"
    }
    
    stages{
        stage("Cleanup Existing Containers"){
            steps{
                sh 'docker stop ${CONTAINER_NAME} || true'
                sh 'docker rm ${CONTAINER_NAME} || true'
            }
        }
        stage("Checkout Code"){
            steps{
                git branch:'main', url: "https://github.com/meenal21/SPE-mini-project.git"
            }
        }
        
        stage("Build Docker Image"){
            steps{
                sh 'docker build -t ${IMAGE_NAME} . '
            }
        }
        stage("Run Code on Container"){
            steps{
                sh 'docker run -it -d -p 5000:8000 --name ${CONTAINER_NAME} ${IMAGE_NAME}'
            }
        }
        stage("Containerized Testing"){
            steps{
                sh 'docker exec scientific-calc pytest /app/test_main.py'
            }
        }
        stage("Cleanup after Testing"){
            steps{
                sh 'docker stop scientific-calc'
                sh 'docker rm scientific-calc'
            }
        }
        stage("Push Image to Registry"){
            steps{
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                        sh "docker tag ${IMAGE_NAME} ${REGISTRY}/${IMAGE_NAME}:latest"
                        sh "docker push ${REGISTRY}/${IMAGE_NAME}:latest"
                }
            }
        }
        stage("Deploy using Ansible"){
            steps{
                sh 'ansible-playbook -i inventory.ini deploy.yml'
            }
        }
    }
    post {
        success {
            echo "Pipeline completed successfully!"

            mail to: "${RECIPIENT_EMAIL}",
                 subject: "Jenkins Pipeline Successful: ${env.JOB_NAME}",
                 body: "The Jenkins pipeline '${env.JOB_NAME}' completed. Check the logs for more details: ${env.BUILD_URL}"
        
        }

        failure {
            echo "Pipeline failed! Sending email notification..."

            mail to: "${RECIPIENT_EMAIL}",
                 subject: "Jenkins Pipeline Failed: ${env.JOB_NAME}",
                 body: "The Jenkins pipeline '${env.JOB_NAME}' failed. Check the logs for more details: ${env.BUILD_URL}"
        }
    }
}