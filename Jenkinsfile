pipeline {
    agent { node { label 'Windows-node' } }
    environment {
        FILENAME_INPUT = 'test.blend'
        FILENAME_OUTPUT = 'out'
        FILE_EXTENSION = 'PNG'
        RESOLUTION_PERCENT = 10
        SAMPLES = 32
    }
    stages {
        stage('render') {
            steps {
                
                echo FILENAME_INPUT
                bat '''
                    chcp 437
                    python begin.py -- ''' + FILENAME_INPUT + " " + FILENAME_OUTPUT + " " + FILE_EXTENSION + " " + RESOLUTION_PERCENT + " " + SAMPLES
                
            }
        }
    }
}
