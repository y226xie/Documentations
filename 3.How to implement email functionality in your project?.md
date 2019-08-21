# How to implement email functionality in project?

There are two main ways to implement it:
1. Use 3-rd party service
2. create your own service


## Using 3-rd party service

In this example, we will use Email.js as our 3-rd party service, and use React.js as our front-end.

### Overview
1. create your React.js front-end template
2. set up Email.js service
3. import Email.js in your code

For a quickly set up, we can implement the following code in App.js file.
Before that, let's install the reactstrap library first, so we can focus on the email functionality of the project

```
npm i -s reactstrap
```
Then install the emailjs dependency for react 

```
npm i -s emailjs-com
```
Then, we can implement the following code in App.js file

```
import React, { Component } from "react"
import { Form, FormGroup, Input, Label, Button } from "reactstrap"
import * as emailjs from "emailjs-com"

class Email extends Component {
    constructor() {
        this.state = {
            name: "",
            email: "",
            otherInfo: "",
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }


    handleChange(e) {
        this.setState({
            [e.target.name]: e.target.value
        })
    }

    async handleSubmit(e) {
        const { name, email, otherInfo} = this.state
        let templateParams = {
            from_name: "YOUR_NAME",
            to_name: email,
            name: name,
            other_info: otherInfo,
        }

        emailjs.send(
            "default_service", //Name of the email service you are going to use
            "TEMPLATE_ID",// template ID can be found at email templates section at Email.js dashboard
            templateParams, // Params you are going to pass to email.js service
            "USER_ID", //User ID can be found at Account section at Email.js dashboard
        )

        console.log("sent!")

    }

    render() {
        return (
            <div>
                <Form>
                    <FormGroup onSubmit={this.handleSubmit}>
                        <Label for='name'>
                            Name
                        </Label>
                        <Input
                        type="text"
                        name="name"
                        onChange={this.handleChange}
                        />
                    </FormGroup>
                    <FormGroup>
                        <Label for='email'>
                            Email
                        </Label>
                        <Input
                        type="email"
                        name="email"
                        onChange={this.handleChange}
                        />
                    </FormGroup>
                    <FormGroup>
                        <Label for='otherInfo'>
                            Other Info
                        </Label>
                        <Input
                        type="text"
                        name="otherInfo"
                        onChange={this.handleChange}
                        />
                    </FormGroup>
                </Form>
            </div>
        );
    }
}

export default Email

```
Finally, we need to go to emailjs.com to create a new account. After setting that up, we can copy the required credientials to our code to replace TEMPLATE_ID, USER_ID, and services.

Done! ☺️
