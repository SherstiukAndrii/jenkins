pipeline {
    // Use a generic agent and run Docker commands inside steps so this Jenkins doesn't need the
    // declarative `agent docker` feature (which may not be available on the controller).
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                // Install pylint directly on the agent (use --user to avoid permission issues)
                sh 'python3 -m pip install --user --upgrade pip pylint'
            }
        }
        
        stage('Static Analysis (Pylint)') {
            steps {
                // Run pylint directly on the agent; using python3 -m pylint ensures module is invoked even
                // if the user-local bin dir is not on PATH.
                sh 'python3 -m pylint --rcfile=.pylintrc --output-format=json:pylint_report.json app.py'
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
