pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'SonarScanner'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out from SCM'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('MySonarQube') {
                    sh '''
                        $SCANNER_HOME/bin/sonar-scanner \
                          -Dsonar.projectKey=sonar-demo \
                          -Dsonar.projectName="Sonar Demo" \
                          -Dsonar.projectVersion=1.0 \
                          -Dsonar.sources=. \
                          -Dsonar.sourceEncoding=UTF-8 \
                          -Dsonar.python.version=3
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Check SonarQube dashboard for results.'
        }
    }
}
