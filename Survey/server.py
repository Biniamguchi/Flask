from flask import Flask,render_template, session, redirect, request, flash
app=Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/survey',methods=['POST'])
def survey():
    valid = True
    if len(request.form["name"])<2:
        flash("Name must be 2 characters or more")
        valid = False
    if not request.form["name"].isalpha():
        flash("Name must only contain letters and not numbers")
        valid = False
    if len(request.form["comment"])<10:
        flash("Comment must be 10 characters or more")
        valid=False

    session["results"] = request.form

    if valid:
        return redirect('/results')

    else:
        return redirect('/')
    # print request.form
    session["results"] = request.form
    return redirect('/results')
@app.route('/results')
def results():
    return render_template('results.html')
app.run(debug=True)
