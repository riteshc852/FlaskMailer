
# FlaskMailer (Template)
This is a simple Flask backend template that takes input from an HTML form and sends the data as an email to a Gmail account. The frontend is built using HTML, CSS, and JavaScript, while Flask handles the backend logic and email sending using SMTP. The project demonstrates basic frontend–backend communication and server-side email handling.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`MAIL_USERNAME` 
`MAIL_PASSWORD`

For MAIL_USERNAME → use your gmail id\
For MAIL_PASSWORD → generate a new app password in your gmail account settings\
\
Follow the  instruction below for generating the app password : 

Prequisties: 

1. A Google account

2. Two-Step Verification enabled on that account
### Steps to generate the app Password
1. Go to google account : https://myaccount.google.com

2. After enabling 2-Step Verification:\
i. Go to Security\
ii. Scroll down\
iii. Click App passwords

3. Generate the App Password
i. Select app → Mail\
ii. Select device → Other\
iii. Enter a name like : Flask Mail app

4. Copy the password 
Something like this : abcd efgh ijkl mnop

Use this Password instead of your real orignal Google Account Password



 


## Run Locally

Clone the project

```bash
  git clone <repo-url>
```

Go to the project directory

```bash
  cd FlaskMailer
```
Install dependencies

```bash
  pip install flask flask-mail python-dotenv
```

Start the server

```bash
  python app.py
```
App running on 
```bash
http://127.0.0.1:8080/
``` 
If you Encounter any error 
1. Check if port 8080 is free 
2. modify app.run() if needed


## More Insights
For more debugging visit the documentation pages of respective prerequisite\
\
Flask : https://flask.palletsprojects.com/en/stable/

Flask-mail : https://flask-mail.readthedocs.io/en/latest/

Google Account help : https://support.google.com/accounts/?hl=en#topic=3382296