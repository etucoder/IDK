import os
from flask import Flask, Response, request
import requests

app = Flask(__name__)

# CHANGE THIS to the exact website you are trying to view
TARGET_URL = "https://example.com" 

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    url = f"{TARGET_URL}/{path}" if path else TARGET_URL
    
    headers = {key: value for (key, value) in request.headers if key.lower() != 'host'}
    
    try:
        response = requests.request(
            method=request.method,
            url=url,
            headers=headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            stream=True, # Streams the data instead of loading it all into memory
            timeout=15
        )
        
        # Strip out specific headers that cause layout or encoding breakages
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        resp_headers = [(name, value) for (name, value) in response.raw.headers.items()
                        if name.lower() not in excluded_headers]
        
        content_type = response.headers.get("Content-Type", "")
        
        # ONLY rewrite links if the content is an actual HTML webpage
        if "text/html" in content_type:
            # Using response.content instead of .text avoids character corruption
            try:
                html_text = response.content.decode('utf-8', errors='ignore')
            except Exception:
                html_text = response.text
                
            modified_content = html_text.replace('href="/', f'href="{TARGET_URL}/')
            modified_content = modified_content.replace('src="/', f'src="{TARGET_URL}/')
            return Response(modified_content, response.status_code, resp_headers, content_type=content_type)
            
        # For images, scripts, fonts, and stylesheets, send the RAW bytes directly
        return Response(response.content, response.status_code, resp_headers, content_type=content_type)

    except Exception as e:
        return Response(f"Proxy Connection Failure: {str(e)}", status=502)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
