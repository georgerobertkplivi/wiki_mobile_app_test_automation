pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root:root' // Run as root user
        }
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run the tests
                sh './run__test.sh all'
            }
        }
    }
    post {
        always {
            // Archive test results or any other artifacts
            junit '**/test-results/*.xml' // Adjust the path as necessary
            archiveArtifacts artifacts: '**/allure-results/**', allowEmptyArchive: true
        }
    }
}