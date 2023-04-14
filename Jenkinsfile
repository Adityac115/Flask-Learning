pipeline{
    agent{
        docker{image 'python:3.10-slim-buster'}
    }
    stages{
        stage('Build'){
            steps{
                sh 'docker build -t $(BUILD_NUMBER) .'
        }
        stage('Testing'){
            steps{
                sh 'echo Testing...'
            }
        }
        stage('Deploy'){
            steps{
                sh 'echo Deploying...'
            }
        }   
    }
}
}
