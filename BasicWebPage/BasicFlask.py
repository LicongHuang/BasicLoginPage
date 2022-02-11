#Importing flask module in the project is mandatory
#An object of Flask class is our WSGI applications
from flask import Flask, render_template, redirect, url_for, request
import insertsql 
import mysql.connector


mydb = mysql.connector.connect(user='root',host='localhost',password="",database="login")
cursor=mydb.cursor(buffered=True)


#Flask constructor takes the name of the current
#module(__name__) as argument
app = Flask(__name__,template_folder='template')

#the route() function of the Flask class is a decorator,
#which tell the app which url should call the associated
#func

@app.route('/')
def hello():
    return "Hello World"


@app.route('/Error/<err>')
def Error(err):
    return 'Problem: %s' % err

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=='POST':
        insert_login_info = insertsql.add_info(request.form['username'],request.form['password'])
        #return "Username: "+request.form['username'] +"\n"+"Password: "+request.form["password"]
        #print(insert_login_info)
        if insert_login_info:
            return render_template('RegisterPage.html')
        else:
            urnm = request.form["username"]
            return redirect(url_for('welcome',urnm=urnm))
    return render_template('RegisterPage.html')

#basic input 
@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        print(insertsql.find_info(request.form['username']))
        if insertsql.verification(request.form['username'],request.form['password']): #add a check with the password
            return redirect(url_for('welcome',urnm=request.form['username']))
        else:
            error = "User name not in Databse"
    return render_template('LoginPage.html', error=error)

    
@app.route('/welcome/<urnm>',methods=['POST','GET'])
def welcome(urnm):
    data=[
        {
            'urnm':urnm
        }
    ]
    if request.method=="POST":
        try:
            insertsql.delete_info(urnm)
            return redirect(url_for("register"))
        except:
            return "Cry"

    return render_template("welcome.html",data=data)
    





if __name__=="__main__":
    #run() method of Flask class runs the app on local
    #development server
    app.run(debug=True)