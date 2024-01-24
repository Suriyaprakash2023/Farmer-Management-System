from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key='my_secrect_key'




# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///farmers.db'
db=SQLAlchemy(app)
app.app_context().push()

from farmer import routes


 

