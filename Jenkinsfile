// Powered by Infostretch
timestamps {
    node () {
    	stage ('python-unittest-job - Checkout') {
     	    checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/platformps/exercise.python_fundamentals']]]) 
    	}
    	stage ('python-unittest-job - Build') {
            // Unable to convert a build step referring to "jenkins.plugins.shiningpanda.builders.CustomPythonBuilder".
            // Please verify and convert manually if required. 
    	}
    }
}