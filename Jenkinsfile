# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:03:12 2025

@author: mzamankhan1
"""

pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repo/math-utils.git'  // Replace with your actual repository
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
