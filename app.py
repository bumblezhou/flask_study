from flask import Flask, escape, redirect, url_for, render_template, request, make_response

#https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files
app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            name = request.form['username']
            token = "test_token"
            #return redirect(url_for("login_callback", name=name, token=token))
            #return render_template('callback.html', name=name, token=token)
            return render_template('index.html', name=name, token=token)
            #return redirect(url_for("menu", name=name, token=token))

            #make response 
            #response = make_response(redirect(url_for("index")))
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
    app.run(debug=True)