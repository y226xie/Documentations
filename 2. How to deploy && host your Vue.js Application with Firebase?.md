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
10. Next, in the root folder create a new file **.firebaserc** with following content:
```
{
  "projects":{
    "default" : "your-firebase-project-id"
  }
}
```
Then make sure you use the project ID that we had copied to replace with **your-firebase-project-id**.

11. Then, Again, from the root folder create a new file **firebase.json** with following content: 

```
{
	"hosting":{
		"public":"dist",
		"ignore": [
			"firebase.json",
			"**/.*",
			"**/node_modules/**"
		],
		"rewrites":[
			{
				"source":"**",
				"destination":"/index.html"
			}
		]

	}
}
```
12. In the **Terminal**, type `firebase login`. If you are successfully logged in, in the firebase website, you will be able to see a success message.
13. Now, in the root directory, run `firebase deploy`. If you receive any error message, then run `firebase init` and following the instructions in your terminal to initialize it.  **TIPS:** Make usre you select the **Hosting** option.
14. Then run `firebase deploy` again in your terminal. 
15. You should be able to see a URL pop up on your terminal, and copy it. This is the public URL for your project. You can also view the url through the firbase console from your browser.
