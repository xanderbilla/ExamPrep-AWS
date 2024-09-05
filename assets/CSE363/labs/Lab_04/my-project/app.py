from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__, template_folder='template')

def authenticate_user(username, password):
    if username == "admin" and password == "passwd":
        return True
    else:
        return False

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate_user(username, password):
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Replace with the desired redirect URL
        else:
            flash('Invalid credentials.', 'error')

    return render_template('login.html')

@app.route('/home')
def home():
    return "Welcome!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)