pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv .venv
                . .venv/bin/activate
                python -m pip install --upgrade pip
                python -m pip install pylint
                '''
            }
        }
        
        stage('Static Analysis (Pylint)') {
            steps {
                sh '.venv/bin/python -m pylint --rcfile=.pylintrc --output-format=json:pylint_report.json app.py'
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
