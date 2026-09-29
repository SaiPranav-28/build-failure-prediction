pipeline {
    agent any

    stages {

        stage('Project Check') {
            steps {
                echo '======================================'
                echo 'Build Failure Prediction using Random Forest'
                echo '======================================'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    PYTHON=/opt/homebrew/opt/python@3.14/bin/python3.14

                    $PYTHON -m venv .jenkins_venv
                    .jenkins_venv/bin/python --version
                    .jenkins_venv/bin/python -m pip install --upgrade pip
                    .jenkins_venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Train Random Forest') {
            steps {
                sh '''
                    .jenkins_venv/bin/python src/train_model.py
                '''
            }
        }

        stage('Predict Build Failure') {
            steps {
                sh '''
                    .jenkins_venv/bin/python src/predict_build.py
                '''
            }
        }
    }
}
