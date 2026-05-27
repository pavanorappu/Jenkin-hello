pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker Image..."
                docker build -t hello-app .
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                echo "Stopping old container..."
                docker rm -f hello-container || true
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                echo "Running new container..."
                docker run -d -p 5000:5000 --name hello-container hello-app
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                echo "Checking application..."
                sleep 5
                curl http://localhost:5000 || exit 1
                '''
            }
        }

        stage('Clean Up Images') {
            steps {
                sh '''
                echo "Cleaning unused Docker images..."
                docker image prune -f
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment Successful - App updated via Jenkins UI!"
        }
        failure {
            echo "❌ Deployment Failed - Check logs"
        }
    }
}
