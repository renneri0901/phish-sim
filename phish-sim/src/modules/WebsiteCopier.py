import os
import requests
from flask import Flask, request, send_file
from bs4 import BeautifulSoup

app = Flask(__name__)

file = "example.html"

def fetch_url(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('example.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print("Page saved to example.html.")
    
def changefile(temp):
    if os.path.exists(temp):
        file = temp
    else:
        print(f"File does not exist: {temp}")


@app.route("/")
def display():
   return send_file(file)



def run():
    app.run(host='0.0.0.0', port=5000)
    

