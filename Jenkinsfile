pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Mohammad-Arafath/py_math.git'  // Replace with your actual repository URL
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh 'python -m venv venv'  // Create a virtual environment
                sh 'source venv/bin/activate' // Activate virtual environment (Linux/macOS)
                sh 'pip install --upgrade pip'
                sh 'pip install pytest'   // Install pytest for testing
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && pytest --junitxml=report.xml'  // Run tests and generate JUnit report
            }
        }

        stage('Publish Test Results') {
            post {
                always {
                    junit 'report.xml'  // Publish test results
                }
            }
        }
    }

    post {
        always {
            sh 'deactivate'  // Deactivate virtual environment (optional cleanup)
        }
        success {
            echo 'Tests passed successfully! ✅'
        }
        failure {
            echo 'Some tests failed. ❌'
        }
    }
}
