import json
import os
import flask
from flask import Flask, jsonify, render_template, request
import psutil
import werkzeug

import common

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/backendMethod', methods=["POST"])
def backend_method():
    # json format: request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    if request.data:
        json_data = json.loads(request.data.decode('utf-8'))
        data = {"key": json_data["key"], "value": json_data["value"]}
        common.backend_method_to_load_sites_data()
        return json.dumps(data)
    # form format: request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    elif request.form:
        data = {"key": request.form["key"], "value": request.form["value"]}
        return json.dumps(data)
    else:
        return json.dumps({"result": False, "msg": "Invalid Parameters"})


@app.route('/upload', methods=["POST"])
def upload():
    print('uploading ...')
    ms = common.measure_spent_time()

    stream, form, files = werkzeug.formparser.parse_form_data(flask.request.environ, stream_factory=common.custom_stream_factory)
    total_size = stream.limit

    for fil in files.values():
        print(" ".join(["saved form name", fil.name, "submitted as", fil.filename, "to temporary file", fil.stream.name]))
        total_size += os.path.getsize(fil.stream.name)
    mb_per_s = "%.1f" % ((total_size / (1024.0 * 1024.0)) / ((1.0 + ms(raw=True)) / 1000.0))
    print(" ".join([str(x) for x in ["handling POST request, spent", ms(), "ms.", mb_per_s, "MB/s.", "Number of files:", len(files)]]))
    process = psutil.Process(os.getpid())
    print("memory usage: %.1f MiB" % (process.memory_info().rss / (1024.0 * 1024.0)))
    return jsonify({'result': True, 'msg': 'Upload successfully!'})


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            name = request.form['username']
            token = "test_token"
            return render_template('index.html', name=name, token=token)
            # return redirect(url_for("home", name=name, token=token))

            # make response 
            # response = make_response(redirect(url_for("home")))
            # response.set_cookie('token', token)
            # response.set_cookie('name', name)
            # return response
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
    app.run(host='0.0.0.0', port=7000, threaded=True)
