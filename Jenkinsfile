pipeline {
    // Use a generic agent and run Docker commands inside steps so this Jenkins doesn't need the
    // declarative `agent docker` feature (which may not be available on the controller).
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                // Use `docker run` to execute pip inside a Python container and write into the workspace
                sh 'docker run --rm -v $PWD:/ws -w /ws python:3.10-slim pip install pylint'
            }
        }
        
        stage('Static Analysis (Pylint)') {
            steps {
                // Run pylint inside the same Python image and write JSON report to the workspace
                sh 'docker run --rm -v $PWD:/ws -w /ws python:3.10-slim pylint --rcfile=.pylintrc --output-format=json:pylint_report.json app.py'
            }
            post {
                always {
                    // Show the report if present (it will be created by the container via the mounted volume)
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
