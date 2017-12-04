from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def signup():
        return render_template('user-signup.html')

@app.route('/welcome')
def welcome():
    name=request.args.get('name')
    template = jinja_env.get_template('welcome.html')
    return template.render()

        

@app.route('/', methods=['POST'])
def user_signup():

    
    password = request.form['password']
    passwordVer = request.form['verPass']
    userName = request.form['username']
    email = request.form['Email']
    
    password_error = ''
    passwordVerf_error = ''
    email_error = ''
    username_error = ''


    if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
        email = email
    else:
        email_error = "Email is invalid"

    if userName=='':
        username_error = 'You must enter a user Name'
    
    if " " in userName:
        username_error = 'No spaces allowed in the User Name'

    if password=='':
        password_error= 'You must enter a password!'

    if passwordVer=='':
        passwordVerf_error= 'You must enter a Verification password also!' 

    if " " in password:
        password_error = 'No spaces allowed in the password'   

    if  len(userName)<3 or len(userName)>20:
        username_error = 'Username must be between 3 and 20 characters'

    if  len(password)<3 or len(password)>20:
        password_error = 'Password must be between 3 and 20 characters'    

    if password != passwordVer:
        password_error = 'The passwords must match'



    if not password_error and not username_error and not email_error and not passwordVerf_error:
        
        
        return render_template('welcome.html', name=userName)
    
    
    else:
        
        return render_template('user-signup.html', password_error=password_error,
            email_error=email_error,username_error=username_error,passwordVerf_error=passwordVerf_error,
            username=userName,
            email=email)

app.run()