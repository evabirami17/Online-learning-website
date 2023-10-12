pipeline{
    agent any 
      
      triggers{
         githubPush()
      }

      stages{
          stage("Checkout"){
             steps{
               //checkout the repository
              checkout scm 
             }
         }
      }
}
