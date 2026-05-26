pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t hello-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f hello-container || true'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name hello-container hello-app'
            }
        }
    }
}
