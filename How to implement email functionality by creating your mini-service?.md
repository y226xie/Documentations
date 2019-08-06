# How to implement email functionality in project?

There are two main ways to implement it:
1. Use 3-rd party service
2. create your own service

## Create you own Mini-Service

### Overview
1. Create your own react.js front-end template
2. Outside of the folder of your project, create a file called server.js which is going to perform sending email functionality

Create a folder called email before we start anything
then Open Terminal, and run

```
npx create-react-app client
```
Outside of client folder, but inside of the email folder, create a Javascipt file called Server.js

Inside the email folder, run
```
npm init --yes
```

That would create a basic package.json file for us
Inside email folder, install the following dependencies:

```
npm i -s express
npm i -s body-parser
```

If you want to use outlook client, you can install nodejs-nodemailer-outlook. Otherwise, we can use nodemailer

```
npm i -s nodejs-nodemailer-outlook
```
or
```
npm i -s nodemailer

```

