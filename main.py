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
                * {box-sizing : border-box; margin : 0; padding : 0;}
                body {font-family : 'Segoe UI',Tahoma,Geneva, Verdana, sans-serif; background-color : #f3f4f6; display : flex;  min-height : 100vh; flex-direction : column; align-items : center;}
                
                .title { display : flex ; justify-content : center; font-size : 40px; margin-bottom : 40px}
                .card { padding: 40px; background: white; border-radius: 12px; max-width : 400px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
                .credentials { display : flex ; align-items:center; justify-content : center; flex-direction : column;}
                .input-group {display : flex; align-items: center; margin-bottom : 6px}
                .credentials form {width : 300px}
                .credentials button {flex : 1;}
                .sign-up {display : flex; align-items : center; width: 300px; flex-direction : column;}
                .sign-up button {background : none; border : none; text-decoration : underline; color : blue;}
                label {width : 90px; text-align :left;}
                input {flex : 1; padding : 3px ; border : 1px solid #000000; }
                h1 { color: #4F46E5; }
            </style>
        </head>
        <body>
            <div class="title" style="">
                <h1>Welcome to IDK</h1>
            </div>
            <div class = "card">
              <div class = "credentials">
                <h2 style = "margin-bottom : 10px">Login to IDK</h2>
                <form action="submit-credentials" method = "post">
                  <div class = "input-group">
                    <label for="username-input">Username : </label>
                    <input type = "text" id = "username-input" name = "username">
                  </div>
                  
                  <div class = "input-group">
                    <label for="password-input">Password: </label>
                    <input type = "password" id = "password-input" name = "password">
                  </div>

                  <div class = "input-group">
                    <button>Login</button>
                  </div>
                </form>

                <div class = "sign-up" >
                  <button style = "margin-bottom : 6px;">Don't have an account? Sign up instead!</button>
                  <p>Forgot your password? Sucks for you!</p>
                </div>
              </div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
