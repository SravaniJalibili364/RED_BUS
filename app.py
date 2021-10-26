
from flask import Flask,render_template,request,redirect,session,flash,url_for
from functools import wraps
from flask_mysqldb import MySQL
import mysql.connector as db


app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Sravani@364'
app.config['MYSQL_DB']='RED_BUS'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)



mydb = db.connect(
   host="localhost",
   user="root",
   db = "RED_BUS",
   password = "Sravani@364"
 )

cur = mydb.cursor()
 
#Login
@app.route('/') 
@app.route('/login',methods=['POST','GET'])
def login():
    status=True
    if request.method=='POST':
        mobile_number=request.form["mobile_no"]
        pwd=request.form["password"]
        cur=mysql.connection.cursor()
        cur.execute("select * from user_info where mobile_no = %s and password=%s",(mobile_number,pwd))
        data=cur.fetchone()
        if data:
            session['logged_in']=True
            session['mobile_number']=data["mobile_no"]
            session['username'] = data["name"]
            flash('Login Successfully','sucess')

            return redirect(url_for('home'))
        else:
            flash('Invalid Login. Try Again','danger')
    return render_template("login.html")

  
#check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('Unauthorized, Please Login','danger')
			return redirect(url_for('login'))
	return wrap
  
#Registration  
@app.route('/reg',methods=['POST','GET'])
def reg():
    status=False
    if request.method=='POST':
        name=request.form["username"]
        mobile_number=request.form["mobile_no"]
        pwd=request.form["password"]
        cur=mysql.connection.cursor()
        cur.execute("insert into user_info(name,password,mobile_no) values(%s,%s,%s)",(name,pwd,mobile_number))
        mysql.connection.commit()
        cur.close()
        flash('Registration Successfully. Login Here...','success')
        return redirect('login')
    return render_template("reg.html",status=status)


#Home page
@app.route("/home")
@is_logged_in
def home():

    cur.execute('SELECT * FROM bus_available')
    data = cur.fetchall()
    return render_template('home.html', result = data)



@app.route('/bus_available',methods=['GET','POST'])
@is_logged_in
def bus_available():
    cur.execute('SELECT * FROM bus_deatails')
    data = cur.fetchall()
    return render_template('bus_available.html', result = data)



@app.route('/reg_details',methods=['GET','POST'])
@is_logged_in
def reg_details():
    status=False
    if request.method=='POST':
        user_id=request.form["user_id"]
        bus_id=request.form["bus_id"]
        source = request.form['source']
        destination = request.form['destination']
        cur=mysql.connection.cursor()
        cur.execute("insert into user_reg_details(user_id,bus_id,source,destination) values(%s,%s,%s,%s)",(user_id,bus_id,source,destination))
        mysql.connection.commit()
        cur.close()
        flash('Bus Booked Successfully','success')
        return redirect(url_for('book'))
    return render_template("reg_details.html",status=status)


# @app.route('/reg',methods=['POST','GET'])
# def bus_available():
#         source_=request.form["source"]
#         destination=request.form["destination"]
#         date = request.form['date']
#         cur=mysql.connection.cursor()
#         cur.execute("select * from bus_available where source = %s and destination=%s and date = %s",(source_,destination,date))
#         data=cur.fetchall()

#         return render_template('bus_avaiable.html',result = data)


@app.route("/book")
def book():

    return redirect(url_for('home'))
    
#logout
@app.route("/logout")
def logout():
	session.clear()
	flash('You are now logged out','success')
	return redirect(url_for('login'))



#caching-time for the application
@app.after_request
def add_header(response):

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control']   = 'public,max-age = 30'

    return response


    
if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True)