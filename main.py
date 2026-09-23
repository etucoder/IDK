import os
from flask import Flask, Response, request
import requests

app = Flask(__name__)

# CHANGE THIS to the exact website you are trying to view
TARGET_URL = "https://connectionsplus.io/" 

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    # Construct the true target URL for the current asset or button press
    url = f"{TARGET_URL}/{path}" if path else TARGET_URL
    
    # Exclude host headers to prevent domain conflicts
    headers = {key: value for (key, value) in request.headers if key.lower() != 'host'}
    
    try:
        # Pass along incoming payload data (crucial for interactive clicks/forms)
        response = requests.request(
            method=request.method,
            url=url,
            headers=headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            timeout=15
        )
        
        # Prepare the proxy response back to your browser
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        resp_headers = [(name, value) for (name, value) in response.raw.headers.items()
                        if name.lower() not in excluded_headers]
        
        # Dynamically inject absolute paths into HTML payloads so scripts interact correctly
        if "text/html" in response.headers.get("Content-Type", ""):
            modified_content = response.text.replace('href="/', f'href="{TARGET_URL}/')
            modified_content = modified_content.replace('src="/', f'src="{TARGET_URL}/')
            return Response(modified_content, response.status_code, resp_headers)
            
        return Response(response.content, response.status_code, resp_headers)

    except Exception as e:
        return Response(f"Proxy Connection Failure: {str(e)}", status=502)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
