pipeline {
    agent any

    environment {
        PYTHON_VENV = 'venv' // Virtual environment name
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: 'github-private-key', url: 'https://github.com/Mohammad-Arafath/py_math.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            set -e
                            python3 -m venv $PYTHON_VENV
                            source $PYTHON_VENV/bin/activate
                            pip install --upgrade pip pytest
                        '''
                    } else {
                        bat '''
                            python -m venv %PYTHON_VENV%
                            call %PYTHON_VENV%\\Scripts\\activate
                            pip install --upgrade pip pytest
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            set -e
                            source $PYTHON_VENV/bin/activate
                            pytest --junitxml=report.xml
                        '''
                    } else {
                        bat '''
                            call %PYTHON_VENV%\\Scripts\\activate
                            pytest --junitxml=report.xml
                        '''
                    }
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'report.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.xml', fingerprint: true
        }
        failure {
            echo 'Build failed! Check the logs for details.'
        }
    }
}
