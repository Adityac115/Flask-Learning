pipeline{
    agent{
        docker{image 'python:3.10-slim-buster'}
    }
    stages{
        stage('Build'){
            steps{
                sh 'echo Building...'
            }
        }
        stage('Release'){
            steps{
                sh 'echo Release...'
            }
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
