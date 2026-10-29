pipeline {
    agent any

    environment {
        DOCKER = 'C:\\Users\\nilka\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Check Docker') {
            steps {
                bat '"%DOCKER%" --version'
                bat '"%DOCKER%" info'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" build -t hello-devops:latest .'
            }
        }

        stage('Run Application') {
            steps {
                bat '"%DOCKER%" run --rm hello-devops:latest'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '"%DOCKER%" run --rm --entrypoint python hello-devops:latest -m pytest -v'
            }
        }
    }
}