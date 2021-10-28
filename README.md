# RED_BUS


Red Bus application is an online Bus registration application offers a simple booking procure bus tickets on luxury buses.


Features for this project

1. User can select the bus based on source,destination and date of the journey.
2. After selecting the bus based on the requirements it will show the entire details of the bus like cost,timings,
   bus_no,rest_stops,available_seats and rating of the bus.
3. After slecting the bus with all the reuirements of the user , user can register the bus with bus_id,user_id,sorce and destinstion.

4.After registration of the user , it will store in data user_registration tables.




Software Requirements of the project :

1. Visual Studio Code
2. MySql version 8.0.26
3. Python 3.8.10
4.from flask import Flask,render_template,request,redirect,session,flash,url_for
5.from functools import wraps
6.from flask_mysqldb import MySQL
7.import mysql.connector as db
8.from flask_caching import Cache

      The above softwares,frameworks,databases,packages that are the required for this project to run this project.

Project Execution:

For this project , In the visual studio first we need to import mysql connector from mysql module and also we have to import datetime module,
flask frmaework,cache.

      A connection with the MySQL server can be established using either the mysql.connector.connect() method.
mydb = db.connect(
   host="localhost",
   user="root",
   db = "RED_BUS",
   password = "Sravani@364"
 )


      Flask is an API of Python that allows us to build up web-applications.We have to connect your Flask app to an existing MYSQL database. Connecting will require your own database username and database password. 

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Sravani@364'
app.config['MYSQL_DB']='RED_BUS'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)





