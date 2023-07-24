import os
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS']=False

db = SQLAlchemy(app)
Migrate(app,db)

#Data Model
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)    
    password = db.Column(db.String)


    def __init__(self, email, firstName, lastName, password):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
    

    def __repr__(self):
        return f"Name: {self.firstName} {self.lastName}, Email: {self.email} Password: {self.password}"

# create databse tables
db.create_all()

#routes
@app.route('/')
def index():
    return render_template('sign-in.html')


@app.route('/sign-in', methods=['POST'])
def signInForm():
    email = request.form.get('email')
    password = request.form.get('password')

    if (checkSignInInfo(email, password)):
        return redirect('/secret-page')
    else:
        message = logInMessage(email)
        return render_template('sign-in.html', message=message )
    
@app.route('/sign-up', methods=['POST'])
def signUpForm():
    firstName = request.form.get('first')
    lastName = request.form.get('last')
    email = request.form.get('email')
    password = request.form.get('password')
    copyPassword = request.form.get('confirm-password')

    if (checkSignUpInfo(email, firstName, lastName, password, copyPassword)):
        return redirect('/thankyou')
    else:
        message = signUpMessage(email, password)
        return render_template('sign-up.html', message=message)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/secret-page')
def secretPage():
    return render_template('secret-page.html')

@app.route('/sign-up')
def signUp():
    return render_template('sign-up.html')


#functionality
def createUser(email, firstName, lastName, password):
    newUser = User (email, firstName, lastName, password)
    db.session.add(newUser)
    db.session.commit()

def checkSignInInfo(email, password):
    user = User.query.filter(User.email == email).first()
    if user and user.password == password:
        return True
    else:
        return False
    
def checkSignUpInfo(email, first, last,  password, copyPassword):
    user = User.query.filter(User.email == email).first()
    if user == None and password == copyPassword and isPasswordValid(password):
        createUser(email, first, last, password)
        redirect('/secret-page')
        return True
    else:
        return False
    
def isPasswordValid(password):
    n = len(password)
    lastChar = password[n - 1]
    if n < 8 or lastChar.isnumeric() == False or password.isupper() or password.islower():
        return False
    return True

def logInMessage(email):
    user = User.query.filter(User.email == email).first()
    message = None
    if user is None:
        message = "User does not exist"
    else:
        message = "Incorrect Password"
    return message

def signUpMessage(email, password):
    user = User.query.filter(User.email == email).first()
    message = None
    
    if user is not None:
        message = 'User already exists'
    elif isPasswordValid(password) != True:
        message = 'Password does not meet requirements'
    else:
        message = 'Passwords do not match'
    return message




if __name__ == "__main__":
    app.run(debug=True)