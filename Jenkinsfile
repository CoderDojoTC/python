pipeline {
  agent { label 'docker-kitchensink-slave' }  // docker-kitchensink-slave is available on jenkins central, update this for other jenkins instances accordingly
  environment {
    ORG = 'CoderDojoTC'
    REPO = 'python'
    CREDENTIALS_ID = '{{JenkinsCredentialId}}'  // This needs to be updated with your jenkins credential, having access to the this github repository
    
    // do not change any parameters below
    MKDOCS_VERSION = '1.0.4'
    LC_ALL='en_US.utf-8'
    LANG='en_US.utf-8'
  }
  stages {
    stage('Build & Deploy Docs') {
      when { branch 'master' }
      steps {
        withCredentials([usernamePassword(credentialsId: "$env.CREDENTIALS_ID", usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh """
            . /etc/profile.d/jenkins.sh
            git config --global user.name "${USERNAME}"
            git remote set-url origin https://${USERNAME}:${PASSWORD}@github.com/${env.ORG}/${env.REPO}.git
            export GIT_USER=${USERNAME}:${PASSWORD}
            export GITHUB_HOST=github.com
            mkdocs gh-deploy --force
          """
        }
      }
    }
  }
}
