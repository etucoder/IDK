from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Render Python Test</title>
            <style>
                .title { display : flex ; justify-content : center;}
                .card { padding: 40px; background: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
                .credentials { display : flex ; justify-content : center;}
                .input-group {display : flex; align-items: center; margin-bottom : 6px}
                label {width : 90px; text-align :left;}
                input {flex : 1; padding : 3px ; border : 1px solid #000000; }
                h1 { color: #4F46E5; }
            </style>
        </head>
        <body>
            <div class="title" style="">
                <h1>Welcome to IDK</h1>
            </div>
            <div class = "credentials">
              <form action="submit-credentials" method = "post">
                <div class = "input-group">
                  <label for="username-input">Username : </label>
                  <input type = "text" id = "username-input" name = "username">
                </div>
                
                <div class = "input-group">
                  <label for="password-input">Password: </label>
                  <input type = "password" id = "password-input" name = "password">
                </div>
              </form>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
