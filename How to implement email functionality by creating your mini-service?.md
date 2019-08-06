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

Then, insider the Server.js file implement the following code:

```
const express = require('express')
const nodeoutlook = require('nodejs-nodemailer-outlook')
const bodyParser = require('body-parser')
const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))

app.post('/api/email', (req, res) => {
     nodeoutlook.sendEmail({
         auth: {
             user: 'YOUR_OUTLOOK_EMAIL',
             pass: 'YOUR_PASSWORD'
         },
         from: 'YOUR_OUTLOOK_EMAIL_ADDRESS', // this must be exactly the same as the user params in auth, otherwise, you will recieved error message from outlook
         to: req.body.email,
         subject: "Here is a email from YOUR_NAME"
         html:`<div>
                    <div>
                    Hello ${req.body.name}
                    </div>
                    <div>Here is your message</div>
                </div>`,

       // attachments: [{
           // filename: filename,
            //content: fileContent,
       // }]
        onError: (e) => console.log(e),
        onSuccess: (i) => console.log(i)
     })
})
const PORT = process.env.PORT || 3001
app.listen(PORT, () => {
    console.log(`Server Listening on port ${PORT}`)
})
```
