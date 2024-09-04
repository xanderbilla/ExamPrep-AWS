from flask import Flask

app = Flask(__name__)

# __name__ is a special variable in Python that is used to determine whether the script is being run on its own or being imported from another module.

# create web oage to display Hello World!

@app.route('/') 
# This is a decorator that tells Flask what URL should trigger the function that follows it.
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__': # This is to ensure that the server only runs if the script is 
    # executed directly.
    app.run(host='0.0.0.0', port=5000)