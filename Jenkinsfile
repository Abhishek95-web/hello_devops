pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hello-devops:latest .'
            }
        }

        stage('Run Application') {
            steps {
                bat 'docker run --rm hello-devops:latest'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'docker run --rm --entrypoint python hello-devops:latest -m pytest -v'
            }
        }
    }
}