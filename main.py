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

                .input-group button {
                  padding : 5px;
                  height : 40px;
                  width : 80px;
                  font-family : 'Segoe UI',Tahoma,Geneva, Verdana, sans-serif;
                  font-size : 1rem;
                  font-weight : 750;
                  border-radius:  5px;
                }

                .card {
                    padding: 40px; 
                    background: white;
                    border-radius: 12px;
                    max-width : 600px; 
                    width : 100%;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    text-align: center;
                    overflow : hidden;
                    }

                .tab-header {
                  display : flex;
                  border-bottom : 1px solid #e5e7eb;
                  background-color : #f9fafb;
                  width : 100%;
                }

                .tab-btn {
                  flex : 1;
                  padding : 14px;
                  border: none;
                  background : none;
                  font-size : 1rem;
                  font-weight : 600;
                  color : #6b7280;
                  cursor : pointer;
                  transition : all 0.2s ease;
                }


                .tab-btn:hover {
                  color : #4F46E5;
                  background-color : #f3f4f6;
                }

                .tab-btn:active {
                  color : #4F46E5;
                  background-color : #ffffff;
                  border-bottom : 3px solid #4F46E5

                }
                
                .card-content {
                  padding : 30px;
                }

                .form-panel {
                  display : block;
                }
              
                .hidden {
                  display : none !important;
                }
                
                <!-- #hide-for-now : {
                  display : none;
                  
                } -->

                .play-button {
                  width : 540px;
                  height: 60px;
                  font-size : 24px;
                  font-weight : 1000;
                  border-radius : 6px;
                  border : 3px solid ;
                  margin : 10px;
                }

                .play-div {
                  display : flex;
                  flex-direction : column;
                  margin : 20px;
                }
                .credentials { display : flex ; align-items:center; justify-content : center; flex-direction : column;}
                .input-group {display : flex; align-items: center; margin-bottom : 6px}
                .credentials form {width : 300px}
                .credentials button {flex : 1;}
                .sign-up {display : flex; align-items : center; width: 300px; flex-direction : column;}
                .sign-up button {background : none; border : none; text-decoration : underline; color : blue;}
                label {width : 90px; text-align :left;}
                input {flex : 1; padding : 3px ; border : 1px solid #000000;  }
                .FAQs {max-width : 100%; width : 100%;}
                .FAQs details {margin-top : 6px; margin-bottom : 3px;  width : 100%; font-size : 24px;}
                .FAQs p {margin : 12px; font-size : 18px;}
                h1 { color: #4F46E5; }
            </style>



            <script>
              function switchTab(tabName){
                const loginTab = document.getElementById('login-tab');
                const signupTab = document.getElementById('signup-tab');
                const loginPanel = document.getElementById('login-panel');
                const signupPanel = document.getElementById('signup-panel');

                loginTab.classList.remove('active');
                signupTab.classList.remove('active');
                loginPanel.classList.add('hidden');
                signupPanel.classList.add('hidden');

                if (tabName === 'login') {
                  loginTab.classList.add('active');
                  loginPanel.classList.remove('hidden');
                } else if (tabName === 'signup') {
                  signupTab.classList.add('active');
                  signupPanel.classList.remove('hidden');
                }
                
              }
            
            </script>
        </head>
        <body>
            <div class="title" style="">
                <h1>Welcome to IDK</h1>
            </div>
            <div class = "play-div">
              <a href= "/strands">
                <button  class = "play-button" style = "background-color : #eafa07;"> Play Strands </button>
              </a>

              <a href = "/connections">
                <button class = "play-button" style = "background-color : #ca23fc" > Play Connections </button>
              </a>
            </div>
            <div href = "/connections" class = "card" id = "hide-for-now" style = "display : none;">
              <div class = "tab-header">
                <button type= "button" class = "tab-btn active" id = "login-tab" onclick = "switchTab('login')">Log In</button>
                <button type= "button" class = "tab-btn active" id = "signup-tab" onclick = "switchTab('signup')">Sign Up</button>
              </div>
              <div  class = "card-content">
                
                <div id = "login-panel" class = "form-panel">

                  <div class = "credentials">
                    <h2 style = "margin-bottom : 10px">Login to IDK</h2>
                    <form action="submit-credentials" method = "POST">
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
                      <p>Forgot your password? Too bad...</p>
                    </div>
                  </div>
                </div>

                <div id = "signup-panel" class = "form-panel hidden">

                  <div class = "credentials">
                    <h2 style = "margin-bottom : 10px">Sign Up to IDK</h2>
                    <form action="add-credentials" method = "POST">
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

                  </div>
                </div>
              </div>
            </div>
            </div>
            <div class = "card" style = "margin-top : 20px ; max-width : 800px; width : 100%;">
              <div class = "FAQs">
                <h2>FAQ's and Important Information</h2>
                <!-- <details>
                  <summary>How do I sign up?</summary>
                  <p>Go to the Sign Up page by clicking the link or scrolling down.Then, enter a unique username and a password and click "Sign Up".</p>

                </details>

                <details>
                  <summary>What is the difference between a DM and a Group Chat?</summary>
                  <p>A DM (Direct Message) allows you to communicate with 1 person only. You cannot add or remove anyone from a DM. A Group chat allows 3+ people to communicate. You can leave or add people to a group chat freely.</p>
                </details>

                <details>
                  <summary>How do I join a IDK Group Chat?</summary>
                  <p>To join a IDK Group Chat, first find out the name and type of the group chat. If the type of the group chat is public , search for the group chat and click 'join'. If the type is 'Join with code', ask any of the members for the join code. If the type is invite only, ask for a invite and then click 'Accept' when one of the managers sends it to you.</p>
                </details>

                <details>
                  <summary>How does IDK work?</summary>
                  <p>IDK uses a Render URL to host the frontend, or the page you are seeing right now. It uses Supabase (A SQL Database) to hold your information securly even when you exit the website , and to be able to show your message to other people</p>
                </details>

                <details>
                  <summary>What if I forgot my password?</summary>
                  <p>IDK does not store passwords in plain text for security reasons, so I cannot find your password in the database. I also did not implement a email recovery system so just remember your password.</p>
                </details>

                <details>
                  <summary>What if I forgot my username?</summary>
                  <p>First of all, how do you even? Second of all, just ask your friends what it is??</p>
                </details> -->
                <details>
                  <summary>How was IDK created?</summary>
                  <p>IDK was created using a mix of Python (Site hosting and changing), HTML (Web Content), and CSS (Styling) </p>
                </details>
                <details>
                  <summary>Why is it called IDK?</summary>
                  <p>IDK.</p>
                </details>

                <details>
                  <summary>Why does this exist?</summary>
                  <p>Because I was bored...</p>
                </details>

                <details>
                  <summary>Should I use this?</summary>
                  <p>IDK, that's up to you.</p>
                </details>

                <details>
                  <summary>Can I request features?</summary>
                  <p>Can you? Yes. Will they be added? Maybe. Do I have the time or budget to add the entirety of YouTube or whatever you think of on here? No.</p>
                </details>


                <details>
                  <summary>Don't click this</summary>
                  <p>It can't be that interesting...</p>
                </details>

              
              </div>
            </div>

          
        </body>
    </html>
"""
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/connections")
def read_root():
    html_content = """
            <!DOCTYPE html>
            <html>
            <style>
                iframe {
                max-width : 100%;
                max-height : 1000px;
                width : 100%;
                height : 1000px;
                }
                h1 {
                font-family : 'Segoe UI',Tahoma,Geneva, Verdana, sans-serif;
                font-size : 40px;
                
                }

                h3 {
                font-family : 'Segoe UI',Tahoma,Geneva, Verdana, sans-serif;

                
                }
                .title-holder {
                display : flex;
                align-items : center;
                justify-content : center;
                flex : 1;
                flex-direction : column;
                }
            </style>

            <head>
                <title>Connections</title>
            </head>

            <body>
                <div class = "title-holder">
                <h3 style = "margin : 5px;">(Unofficial)</h3>
                <h1 style = "margin : 5px;">Connections</h1>
                </div>
                
                <iframe
                src = "https://connectionsplus.io/" 
                >

                </iframe>
            </body>
            </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/strands")
def read_root():
    html_content = """
    <!DOCTYPE html>
<html>
  <style>
    iframe {
      max-width : 100%;
      max-height : 1000px;
      width : 100%;
      height : 1000px;
    }
    h1 {
      font-family : 'Segoe UI',Tahoma,Geneva, Verdana, sans-serif;
      font-size : 40px;
    
    }

    h3 {
      font-family : 'Segoe UI',Tahoma,Geneva, Verdana, sans-serif;

    
    }
    .title-holder {
      display : flex;
      align-items : center;
      justify-content : center;
      flex : 1;
      flex-direction : column;
    }
  </style>

  <head>
    <title>Connections</title>
  </head>

  <body>
    <div class = "title-holder">
      <h3 style = "margin : 5px;">(Unofficial)</h3>
      <h1 style = "margin : 5px;">Strands</h1>
    </div>
    
    <iframe
      src = "https://strandsgame.net/" 
    >

    </iframe>
  </body>
</html>

    


    """
    return HTMLResponse(content=html_content, status_code=200)