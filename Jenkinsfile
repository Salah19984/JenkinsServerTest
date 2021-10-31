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
                sh 'python3 calc.py'
            }
    }
        stage('Test') {
            steps {
               sh 'py.test --junitxml ./test_results/results.xml test_calc.py'
               step([$class: 'JUnitResultArchiver', checksName: '', testResults: 'test_results/results.xml'])
           }
        }
        stage('Deploy') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS' 
                }
            }
            steps {echo 'deploying build to /var/lib/jenkins/workspace/TestPipeline/'
        }
    }
}
}