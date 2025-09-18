pipeline {
    agent any

    stages {
        stage('Build Flask App Docker Image') {
            steps {
                sh "docker build -t mohammedsami99852/v1:v1 ."
            }
        }

        stage('Push Flask App Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push mohammedsami99852/v1:v1"
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    sh "docker-compose down || true"
                    sh "docker-compose up -d --build"
                }
            }
        }
    }
}
