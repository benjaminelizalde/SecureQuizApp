import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars).  

@app.route('/')
def renderMain():
    session.clear()
    return render_template('home.html')
   

@app.route('/startOver')
def startOver():
    
    session.clear()
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    
    if "answer1" in session:
        print(session["answerscorrect"])
    else:
        session["answer1"] = request.form["answer1"] 
        if session["answer1"] == "french" or  session["answer1"] == "French":
            session["answerscorrect"]= 1
        else:
            session["answerscorrect"]= 0
    
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if "answer2" in session:
        print(session["answerscorrect"])
    else:
        session["answer2"] = request.form["answer2"] 
        if session["answer2"] == "6":
            session["answerscorrect"]= session["answerscorrect"] + 1
        else:
            session["answerscorrect"]= session["answerscorrect"]
    print(session["answerscorrect"])
    return render_template('page3.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    if "answer3" in session:
        print(session["answerscorrect"])
    else:
        session["answer3"] = request.form["answer3"] 
        if session["answer3"] == "spiders" or session["answer3"] == "Spiders" :
            session["answerscorrect"]= session["answerscorrect"] + 1
        else:
            session["answerscorrect"]= session["answerscorrect"]
    print(session["answerscorrect"])
    
    return render_template('page4.html')
if __name__=="__main__":
    app.run(debug=True)
