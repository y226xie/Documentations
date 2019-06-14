## How to deploy && host your Vue.application by using Firebase?

1. IMPORTANT: Create a `branch` first, please do not use `master` branch for deployment.
2. Create a firebase account, here is their offical site: https://firebase.google.com
3. After creating the account, go to the top right corner of the page and clicke on **Go TO Console** 
4. Add a new project by clicking on **Add Project**.Project name can be anything, then click on **Create Project** button at the bottom
5. Once, the project has been created, you can go click the **Setting icon** at the left navigation bar. Then you will find a button for **Project settings**
6. Then copy the **Project ID**, we need to use it later.
7. Go back to **Visual Studio Code**, or **Terminal**, run `npm install -g firebase-tools` to install the Firebase CLI
8. Once you have successfully install the Firebase CLI, run `npm run build` in the project root folder. 
9. Go back to the project folder, check if there is a folder called  **dist**. This folder contains everything we are going to deploy.
10. Next, in the root folder create a new file called **.firebaserc** with following content:
```
{
  "projects":{
    "default" : "your-firebase-project-id"
  }
}
```
