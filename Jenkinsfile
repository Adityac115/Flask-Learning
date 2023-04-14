pipeline{
    agent{
        docker{image 'python:3.10-slim-buster'
        args '--user root -v /var/run/docker.sock:/var/run/docker.sock' }
    }
    stages{
        stage('Build'){
            steps{
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
            }
        }   
    
}
}
