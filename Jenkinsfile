/* Declarative Format of Jenkinsfile for RWU Continuous Integration Project */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                build 'TestBuildCalc'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 unittest/test_calc.py'
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'deploying build to /var/lib/jenkins/workspace/TestBuildCalc/'
            }
        }
    }
}
