import os
import requests
from flask import Flask, send_file, abort, send_from_directory
from bs4 import BeautifulSoup

app = Flask(__name__)

BASE_FILE = r".\WebsiteStuff\Google.html"
BASE_DIR = r".\WebsiteStuff\Google_files"

def fetchUrl(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('Copied.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print("Page saved to example.html.")
    
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

@app.route('/<path:filepath>')
def serve_file(filepath):
    full_path = os.path.join(BASE_DIR, filepath)

    if not os.path.isfile(full_path):
        abort(404)

    directory = os.path.dirname(full_path)
    filename = os.path.basename(full_path)
    return send_from_directory(directory, filename)


@app.route("/")
def display():
   return send_file(BASE_FILE)



def run():
    app.run(host='0.0.0.0', port=5001)
    

