pipeline {
    agent any
    stages {
        stage('run backend server') {
            steps {
                bat 'start/min python rest_app.py'
            }
        }
        stage('run frontend server') {
            steps {
                bat 'start/min python web_app.py'
            }
        }
        stage('run backend testing') {
            steps {
                bat 'python backend_testing.py'
            }
        }
        stage('run frontend testing') {
            steps {
                bat 'python frontend_testing.py'
            }
        }
        /*stage('run clean enviroment') {
            steps {
               bat 'python clean_enviroment.py'
            }
        }*/
    }
}

