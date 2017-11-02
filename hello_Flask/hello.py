from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')


def hello_world():
 	return render_template('index.html')

@app.route("/ninjas")
def ninja():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojo():
    return render_template('dojo.html')
app.run(debug=True)

# @app.route('/users/new')
# def dojo():
#    # print "Got Post Info"
#    # # # we'll talk about the following two lines after we learn a little more
#    # # # about forms
#    # name = request.form['name']
#    # email = request.form['email']
#    # # redirects back to the '/' route
#    return redirect('/')
#    return render_template('dojo.html')
# app.run(debug=True)
