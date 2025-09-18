pipeline {
    agent any

    stages {
        stage('Run Tests') {
            steps {
                sh "pip install -r requirements.txt"
                sh "pytest --maxfail=1 --disable-warnings -q"
            }
        }
        
        

        stage('Build Flask App Docker Image') {
            steps {
                sh "docker build -t mohammedsami99852/flask-mysql-app:latest ."
            }
        }

        stage('Push Flask App Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push mohammedsami99852/flask-mysql-app:latest"
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
