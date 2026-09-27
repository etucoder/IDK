from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import csv
from flask import Flask, request, jsonify
import requests
import random
from pydantic import BaseModel
app = FastAPI() 


templates = Jinja2Templates(directory="templates")
templates.env.cache = None

SHEET_ID = "1xM-GG4u16PiTrxSJQWZnX4Iiqh36ROobzcFGBKiRPIA"
SHEET_URL = "https://docs.google.com/spreadsheets/d/1xM-GG4u16PiTrxSJQWZnX4Iiqh36ROobzcFGBKiRPIA/export?format=csv"

cached_words = []
last_seen_tag = None
categories = []

def get_current_connections_from_sheet():
    global cached_words, last_seen_tag, categories

    try :
      header_check = requests.head(SHEET_URL)
      current_etag = header_check.headers.get("ETag")

      if cached_words and (current_etag == last_seen_tag):
        return cached_words

      print("Sheet changed. Updating...")

      response = requests.get(SHEET_URL)
      response.raise_for_status()

      lines = response.text.splitlines()
      reader = csv.reader(lines)

      words = []
      categories = []
      for row in reader:
         for cell in row:
            if cell.strip():
               if words.__len__() <= 15:
                words.append(cell.strip())
               else:
                categories.append(cell.strip())
                

      if words:
        cached_words = words
        last_seen_tag = current_etag

      return cached_words
    except Exception as e :
      print(e)

get_current_connections_from_sheet()
print(cached_words)
@app.get("/",response_class=HTMLResponse)
def read_root(request : Request):

    return templates.TemplateResponse(request = request, name = "index.html")


actual_words = cached_words.copy()
print(actual_words)
correct_groups = {"1" : [actual_words[0],actual_words[1],actual_words[2],actual_words[3]],"2" : [actual_words[4],actual_words[5],actual_words[6],actual_words[7]],"3" : [actual_words[8],actual_words[9],actual_words[10],actual_words[11]],"4" : [actual_words[12],actual_words[13],actual_words[14],actual_words[15]]}
random.shuffle(cached_words)
print(cached_words)
print(categories)
print(correct_groups)
words_are_matching = False
def check_correct_answers(words_chosen : list) -> dict[str,list[str]]:
  global words_are_matching, correct_groups
  for category_num, answers in correct_groups.items(): 
    print(correct_groups.items())
    print(f"Category Num : {int(category_num) - 1}, Answers : {answers}")
    words_are_matching = True
    for word in words_chosen:
      if word in answers:
        pass
      else:
        words_are_matching = False
    if words_are_matching:
      print(f"Words: {words_chosen}, Answers : {answers}, Category : {categories[int(category_num) - 1]}")
      return {"category" : categories[(int(category_num) - 1)], "answers" : answers, "id" : int(category_num)}

  return {}




class GuessRequest(BaseModel):
  words : list[str]

@app.post("/check_guess")
def check_guess(request_data : GuessRequest):

  words_chosen = request_data.words

  result = check_correct_answers(words_chosen)

  return result

@app.get("/connections")
def read_root(request : Request):
    return templates.TemplateResponse(request = request, name = "connections.html", context = {"words" : cached_words})

# @app.get("/connections")
# def read_root():
#     html_content = """
#             <!DOCTYPE html>
# <html>
#   <style>
#     iframe {
#       max-width : 100%;
#       max-height : 1000px;
#       width : 100%;
#       height : 1000px;
#     }
#     h1 {
#       font-family : 'Segoe UI',Tahoma,Geneva, Verdana, sans-serif;
#       font-size : 40px;
    
#     }

#     h3 {
#       font-family : 'Segoe UI',Tahoma,Geneva, Verdana, sans-serif;

    
#     }
#     .title-holder {
#       display : flex;
#       align-items : center;
#       justify-content : center;
#       flex : 1;
#       flex-direction : column;
#     }
#   </style>

#   <head>
#     <title>Connections</title>
#   </head>

#   <body>
#     <div class = "title-holder">
#       <h3 style = "margin : 5px;">(Unofficial)</h3>
#       <h1 style = "margin : 5px;">Connections</h1>
#     </div>
    
#     <object
#       data = "https://connectionsplus.io/" 
#       style = "width : 1000px; height : 1000px;"
#     >

#     </object>
#   </body>
# </html>
#     """
#     return HTMLResponse(content=html_content, status_code=200)

# @app.get("/strands")
# def read_root():
#     html_content = """
#     <!DOCTYPE html>
# <html>
#   <style>
#     iframe {
#       max-width : 100%;
#       max-height : 1000px;
#       width : 100%;
#       height : 1000px;
#     }
#     h1 {
#       font-family : 'Segoe UI',Tahoma,Geneva, Verdana, sans-serif;
#       font-size : 40px;
    
#     }

#     h3 {
#       font-family : 'Segoe UI',Tahoma,Geneva, Verdana, sans-serif;

    
#     }
#     .title-holder {
#       display : flex;
#       align-items : center;
#       justify-content : center;
#       flex : 1;
#       flex-direction : column;
#     }
#   </style>

#   <head>
#     <title>Connections</title>
#   </head>

#   <body>
#     <div class = "title-holder">
#       <h3 style = "margin : 5px;">(Unofficial)</h3>
#       <h1 style = "margin : 5px;">Strands</h1>
#     </div>
    
#     <iframe
#       src = "https://strandsgame.net/" 
#     >

#     </iframe>
#   </body>
# </html>

    


#     """
#     return HTMLResponse(content=html_content, status_code=200)