pipeline {
    agent any

    environment {
        TARGET_ENV = "${env.BRANCH_NAME == 'develop' ? 'dev' : (env.BRANCH_NAME == 'qa' ? 'qa' : 'prod')}"
    }

    stages {
        stage('Test') {
            agent {
                docker { image 'python:3.12-slim' }
            }
            steps {
                dir('app-python') {
                    sh '''
                       python3 -m venv venv
                       . venv/bin/activate
                       pip3 install -r requirements-dev.txt
                       pytest
                    '''
                }
            }
        }
        stage('Docker Build') {
            steps {
                echo 'Construyendo imagen Docker...'
                dir('app-python') {
                    sh "docker build -t localhost:5000/app-python:\$(git rev-parse --short HEAD) ."
                    sh "docker push localhost:5000/app-python:\$(git rev-parse --short HEAD)"
                }
            }
        }
        stage('Deploy') {
            steps {
                echo "Desplegando en el ambiente: ${TARGET_ENV}"
                sh '''
                    kubectl apply -f k8s/${TARGET_ENV}/app-python-deployment.yaml
                    kubectl set image deployment/app-python app-python=local-registry:5000/app-python:$(git rev-parse --short HEAD) -n ${TARGET_ENV}
                '''
            }
        }
    }
}
