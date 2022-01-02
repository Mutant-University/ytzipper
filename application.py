import flask
import subprocess
from flask import Flask
from flask import render_template


YOUTUBE_DOWNLOAD_COMMAND = "youtube-dl"
CHANGE_DIRECTORY = "cd; ls"
TRIAL = 'cd playlist'
# __name__ gets the environment variable called FLASK_APP 
app = Flask(__name__)
@app.route("/", methods = ["GET"])
def home_get():      
    return render_template('index.html')
    
         

@app.route("/", methods = ["POST"] )     
def home_post():
    url=flask.request.form.get("link")
    subprocess.Popen([YOUTUBE_DOWNLOAD_COMMAND,str(url)],cwd="playlist")
    return render_template('index.html')

    