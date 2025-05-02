# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 10:06:08 2025

@author: fasts
"""
# pip install lxml_html_clean
# 
import requests
from bs4 import BeautifulSoup
def spoof(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Save HTML
    with open('example.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
        
        print("Page saved.")






