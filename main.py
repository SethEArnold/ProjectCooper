# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# [START gae_python37_app]
from flask import Flask, render_template, request
#import requests
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
myurl = "no_video"
myskip = "no"
q = []
@app.route('/', methods=['GET', 'POST'])
def hello():
    global q
    if request.method == 'POST':
        print(request.form['text'])
        global myurl
        q.append(request.form['text'])
        #HTML Request to add url to video queue
        return render_template('index.html')
    else:
        #HTML Request to skip video
        global myskip
        myskip = "yes"
        if q:
            print("popping")
            q.pop(0)
        return render_template('index.html')
@app.route('/myurl')
def myfunc():
    global myurl
    toReturn = ""
    for url in  q:
        toReturn +=(url+" ")
    return toReturn
@app.route('/skip')
def myfunc2():
    global myskip
    toreturn =  myskip
    myskip = "no"
    return toreturn
@app.route('/vidover')
def myfunc3():
    global q
    if q:
        q.pop(0)
    return ''
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=False)
# [END gae_python37_app]
