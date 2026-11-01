
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
                bat 'python -m unittest -v'
            }
        }

        stage('Data Quality Validation') {
            steps {
                bat 'python validate_assets.py'
            }
        }
    }
}
