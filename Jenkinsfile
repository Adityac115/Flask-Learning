pipeline{
    agent {
        docker {
            image python:3.10-slim-buster
        }
    }
        stages{
            stage("Build"){
                sh 'Build here...'
            }   

            stage("Release"){
                sh 'Release here...'
            }

            stage("Integration test"){
                sh 'Integration test here...'
            }

            stage("Pushing to dockerhub"){
                sh 'Pushing to dockerhub...'
            }
        
    }
}
