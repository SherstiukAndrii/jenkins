pipeline {
    agent { docker { image 'python:3.10-slim' } } 

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install pylint'
            }
        }
        
        stage('Static Analysis (Pylint)') {
            steps {
                sh 'pylint --rcfile=.pylintrc --output-format=json:pylint_report.json app.py'
            }
            post {
                always {
                    sh 'cat pylint_report.json || true' 
                }
            }
        }
        
        stage('Build if successful') {
            when {
                expression { return currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo 'Static analysis passed. Ready for next stage (e.g., tests/build).'
            }
        }
    }
}
