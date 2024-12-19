import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the login page (GET request)
@app.route("/", methods=["GET"])
def login_page():
    return render_template("login.html")

# Route for handling the login form submission (POST request)
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Basic validation (you can extend this to check username/password from a database)
    if username == "biker" and password == "password123":  # Example credentials
        return f"Welcome, {username}!"
    else:
        return redirect(url_for("login_page"))  # Redirect back to login page if incorrect

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
