
pipeline {
    agent any

    stages {
        stage('Verify Source') {
            steps {
                bat '''
                    "C:\\Program Files\\Git\\cmd\\git.exe" log -1 --oneline
                    dir
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                bat 'python run_tests.py'
            }
            post {
                always {
                    junit testResults: 'test-reports/junit.xml'
                }
            }
        }

        stage('Data Quality Validation') {
            steps {
                bat 'python validate_assets.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'test-reports/junit.xml',
                             fingerprint: true
        }
    }
}
