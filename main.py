from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# The website you are trying to embed
TARGET_URL = "https://connectionsplus.io/"

# The HTML template that displays the content without an iframe
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bypass Container</title>
    <style>
        body { margin: 0; font-family: sans-serif; background: #111; color: white; }
        header { background: #222; padding: 10px; text-align: center; font-weight: bold; }
        #content-container {
            width: 100%;
            height: 90vh;
            background: white;
            color: black;
            overflow-y: auto;
            padding: 10px;
            box-sizing: border-box;
        }
    </style>
</head>
<body>
    <header>Web View Container (No Iframe)</header>
    
    <!-- The raw site code gets injected natively right here -->
    <div id="content-container">
        {{ embedded_html | safe }}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    try:
        # Fetch the target website from the server-side
        response = requests.get(TARGET_URL, headers={"User-Agent": "Mozilla/5.0"})
        site_markup = response.text
    except Exception as e:
        site_markup = f"<p>Error loading website data: {str(e)}</p>"
        
    return render_template_string(HTML_TEMPLATE, embedded_html=site_markup)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
