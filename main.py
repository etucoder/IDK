import os
from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

app = Flask(__name__)

# CHANGE THIS to the website you want to embed
TARGET_URL = "https://connectionsplus.io/" 

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactivity Container</title>
    <style>
        body { margin: 0; font-family: sans-serif; background: #111; color: white; }
        header { background: #222; padding: 12px; text-align: center; font-weight: bold; font-size: 1.1rem; }
        #content-container {
            width: 100%;
            height: 92vh;
            background: white;
            color: black;
            overflow: auto;
            box-sizing: border-box;
        }
    </style>
</head>
<body>
    <header>Interactive Web Portal (No Iframe)</header>
    <div id="content-container">
        {{ embedded_html | safe }}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    try:
        # Fetch the site content safely from the backend
        response = requests.get(TARGET_URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Fix relative links: Convert things like "/style.css" to "https://example.com"
        for tag in soup.find_all(['sidebar', 'script', 'link', 'a', 'img', 'form']):
            # Fix CSS and Javascript links
            if tag.name in ['script', 'img'] and tag.get('src'):
                tag['src'] = urljoin(TARGET_URL, tag['src'])
            elif tag.name == 'link' and tag.get('href'):
                tag['href'] = urljoin(TARGET_URL, tag['href'])
            # Fix clickable anchors so links work inside the container
            elif tag.name == 'a' and tag.get('href'):
                tag['href'] = urljoin(TARGET_URL, tag['href'])
            # Fix interactive forms
            elif tag.name == 'form' and tag.get('action'):
                tag['action'] = urljoin(TARGET_URL, tag['action'])

        site_markup = str(soup)
    except Exception as e:
        site_markup = f"<div style='padding:20px; color:red;'>Proxy Error: {str(e)}</div>"
        
    return render_template_string(HTML_TEMPLATE, embedded_html=site_markup)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
