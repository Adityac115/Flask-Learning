pipeline{
    agent any
        // docker{image 'python:3.10-slim-buster'
        // args '--user root -v /var/run/docker.sock:/var/run/docker.sock' }
    environment{
        IMAGE_TAG="$BUILD_NUMBER"
    }
    stages{
        stage('Build'){
            steps{
                sh' echo Building Docker image'
                sh 'docker build -t myapp:${BUILD_NUMBER} .'
        }
        }
        stage('Testing'){
            steps{
                sh 'echo Testing...'
            }
        }
        stage('Push to Dockerhub'){
            steps{
                sh'echo "Build Docker image" '
                sh 'docker push myapp:${BUILD_NUMBER} '

            }
        }
        stage('Deploy'){
            steps{
                sh 'echo Deploying...'
                sh 'docker-compose up -d --build --scale flask-app=5'
            }
        }   
    
}
}
