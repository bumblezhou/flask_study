import json, time, asyncio
from flask import Flask, escape, redirect, url_for, render_template, request, make_response

#https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files
app = Flask(__name__)

from common import backend_method_to_load_sites_data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/backendMethod', methods=["POST"])
def backend_method():
    # json format: request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    if request.data:
        json_data = json.loads(request.data.decode('utf-8'))
        data = {"key": json_data["key"], "value": json_data["value"]}
        backend_method_to_load_sites_data()
        return json.dumps(data)
    # form format: request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    elif request.form:
        data = {"key": request.form["key"], "value": request.form["value"]}
        return json.dumps(data)
    else:
        return json.dumps({"result": False, "msg": "Invalid Parameters"})

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            name = request.form['username']
            token = "test_token"
            return render_template('index.html', name=name, token=token)
            #return redirect(url_for("home", name=name, token=token))

            #make response 
            #response = make_response(redirect(url_for("home")))
            #response.set_cookie('token', token)
            #response.set_cookie('name', name)
            #return response
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def valid_login(username, password):
    # access database
    return username == "zhou" and password == "123456"


# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
