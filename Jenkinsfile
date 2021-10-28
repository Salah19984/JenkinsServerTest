/* Declarative Format of Jenkinsfile for RWU Continuous Integration Project */
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Salah19984/JenkinsServerTest.git']]])
        }
    }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Salah19984/JenkinsServerTest.git'        
                sh 'python3 ./src/calc.py'
            }
    }
        stage('Test') {
            steps {
               sh 'python3 -m ./unittest/test_calc.py' 
           }
        }
        stage('Deploy') {
            steps {
                echo 'deploying build to /var/lib/jenkins/workspace/TestPipeline/'
        }
    }
}
}