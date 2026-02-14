pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Mayank150Git/test_repo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment
                bat 'python -m venv venv'
                // Activate venv and install dependencies
                bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
                // Install Playwright browsers
                bat 'call venv\\Scripts\\activate && playwright install'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat 'call venv\\Scripts\\activate && pytest -v -s --headed --browser webkit'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'results.xml'
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '',
                    reportFiles: 'report.html',
                    reportName: 'Playwright Test Report'
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.html, *.xml', fingerprint: true, allowEmptyArchive: true
        }
    }
}