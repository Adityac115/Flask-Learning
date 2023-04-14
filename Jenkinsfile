pipeline{
    agent any
        // docker{image 'python:3.10-slim-buster'
        // args '--user root -v /var/run/docker.sock:/var/run/docker.sock' }
    
    stages{
        stage('Build'){
            steps{
                sh' echo Building Docker image'
                sh 'docker build -t myapp .'
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
                sh 'docker-compose up -d --build --scale flask-app=10'
            }
        }   
    
}
}
