pipeline {
    agent any

    stages {
        stage('Project Check') {
            steps {
                echo '======================================'
                echo 'Build Failure Prediction using Random Forest'
                echo 'Jenkins CI/CD project is working!'
                echo '======================================'
            }
        }

        stage('Run Python') {
            steps {
                sh 'python3 src/hello.py'
            }
        }
    }
}
