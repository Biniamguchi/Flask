# from flask import Flask, render_template, request, redirect, session
# import random
# app = Flask(__name__)
# app.secret_key = 'Top_secret'

# @app.route("/")
# def radom():

#     if 'random' and 'guess' not in session:
#         session['guess'] = 0
#         session['random'] = random.randrange(0, 101)
#     print 'the random number is ' + str(session['random'])
#     # session['guess'] = request.form
#     return render_template("greatnumber.html")

# @app.route("/check", methods=['POST'])
# def check():
#     guess = request.form['guess']

#     guess = int(guess)
#     session['guess'] = guess
#     for random in session:
#         if random == 'guess':
#             print "You got it"
#         else:
#             print "Wrong number"

#     return redirect("/")

# @app.route("/reset")
# def reset():
#     session.clear()
#     return redirect("/")
# app.run(debug=True)
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('greatnumber.html')
@app.route('/process', methods=['Post'])
def process():
  #do some validations here!
  return redirect('/')
app.run(debug=True)