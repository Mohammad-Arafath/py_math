pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Mohammad-Arafath/py_math.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && pytest --junitxml=report.xml'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
