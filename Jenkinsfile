pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Application') {
            steps {
                bat 'python app.py'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m unittest discover -s tests -t .'
            }
        }
    }
    post {
        success {
            echo 'CI Build Completed Successfully'
        }
        failure {
            echo 'TESTS FAILED'
        }
    }
}
