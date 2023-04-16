pipeline{
    agent any
        // docker{image 'python:3.10-slim-buster'
        // args '--user root -v /var/run/docker.sock:/var/run/docker.sock' }
    environment{
        IMAGE_TAG="$BUILD_NUMBER"
        DOCKER_CREDENTIALS=credentials("Aditya-dockerhub")
    }
    stages{
        stage('Build'){
            steps{
                sh' echo Building Docker image'
                sh 'docker build -t aditya115/flask-app:${IMAGE_TAG} .'
        }
        }
        stage('Testing'){
            steps{
                sh 'echo Testing...'
            }
        }
        stage('Push to Dockerhub'){
            steps{
                script{
                    withDockerRegistry(credentialsId: 'Aditya-dockerhub') {

                    sh 'echo Login to dockerhub.... '
                    sh '    docker push aditya115/flask-app:${IMAGE_TAG} '
                    }
            }
        }
            
        }
        stage('Deploy'){
            steps{
                sh 'echo Deploying...'
                sh 'docker-compose up -d --build --scale flask-app=2'
            }
        }   
    
}
}

