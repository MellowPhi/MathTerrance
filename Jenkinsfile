pipeline {
    agent any
    
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MellowPhi/terryology-calculator']])
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                script {
                    sh 'docker build -t mellowphi/terryology-calc .'
                }
            }
        }
        
        stage('Push Image To Docker Hub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'dockerhubpwd', variable: 'dockerhubpwd')]) {
                    sh 'docker login -u mellowphi -p ${dockerhubpwd}'
                    sh 'docker push mellowphi/terryology-calc'
                }
                }
                
            }
        }
        

    }
    
}