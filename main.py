from flask import Flask     
app = Flask(__name__)

@app.route("/")
def index(): 
    data = open(file="./html/index.html", encoding="utf8")
    return data

@app.route("/page/<page_id>")
def page(page_id="index"):
    try:
        data = open(file="./html/" + page_id + ".html", encoding="utf8")
        return data
    except:
        return open(file="./html/404.html", encoding="utf8")
    
@app.route("/asset/<asset_id>")
def asset(asset_id):
    try:
        data = open(file="./static/" + asset_id)
        return data
    except:
        return open(file="./html/404.html", encoding="utf8")

  
if __name__=='__main__': 
   app.run(port=80)