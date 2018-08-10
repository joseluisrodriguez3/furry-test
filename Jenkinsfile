pipeline {
    agent { docker { image 'python' } }
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('unittest') {
            steps {
                sh 'python --version'
            }
        }
    }
    post {
        always {
            junit 'python_unittests_xml/**/*.xml'
        }
    }
}
