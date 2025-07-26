from flask import Flask, request, redirect, render_template
import os
from main import virtual_Painter  # Assuming main.py contains virtual_Painter()

app = Flask(__name__)

# Simulating user data storage
users = {"test@example.com": "password123"}

@app.route('/')
def index():
    return render_template('index.html')  # Serve your HTML file

@app.route('/signin', methods=['POST'])
def signin():
    email = request.form.get('email')
    password = request.form.get('password')
    if users.get(email) == password:
        # If credentials match, run the painter function
        virtual_Painter()
        return "Signed in successfully! Virtual Painter started."
    else:
        return "Incorrect email or password."

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if email in users:
        return "User already exists."
    else:
        users[email] = password
        virtual_Painter()  # Start the virtual painter after sign-up
        return "Signed up and Virtual Painter started."

if __name__ == "__main__":
    app.run(debug=True)
