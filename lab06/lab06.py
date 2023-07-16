from flask import Flask, render_template, request
app = Flask (__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    password = request.args.get('password')
    message = isPasswordValid(password)
    return render_template('report.html', username=username, message=message)

def isPasswordValid(password):
    n = len(password)
    lastChar = password[n - 1]
    if n < 8 or lastChar.isnumeric() == False or password.isupper() or password.islower():
        return "The password does not meet all the requirements."
    return "The password meets all the requirements."

    
if __name__ == '__main__':
    app.run(debug=True)