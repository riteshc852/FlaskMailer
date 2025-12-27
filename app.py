from flask import Flask, render_template , request , jsonify 
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
load_dotenv() # load the env variables  
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
mail = Mail() # creation of mail object 
mail.init_app(app) # configuration of mail 

@app.route("/" ,methods=["GET" , "POST" ])
def index():
    if request.method == 'POST':
          name = request.form.get('name')
          email = request.form.get('email')
          subject = request.form.get('subject')
          message = request.form.get('message')   
        # store the data inside dictionary for ease of access of data 
          detail = {
               "name" : name,
               "email" : email,
               "subject" : subject,
               "message" : message
               }
          msg = Message (
              subject = "New Message",
              sender = detail['email'],
              recipients = [os.getenv('MAIL_USERNAME')]
         )
          # you could use html here by using msg.html = f""" """ and send html 
          msg.body = f"Name: {detail['name']}\nEmail: {detail['email']}\n Subject:{detail['subject']}\n Message: {detail['message']}"
          
          try: 
                mail.send(msg)
                return jsonify({"status" : "success"})
          except Exception as e:
                print(e)
                return jsonify({"status" : "error"})        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False, port = 8080)