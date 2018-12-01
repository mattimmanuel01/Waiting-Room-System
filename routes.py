from flask import request, render_template,url_for,redirect
from flask_login import current_user,login_required,login_user,logout_user
from server import app, sys,login_manager
from src.session import *

@login_manager.user_loader
def load_user(name):
	return sys.get_session(name)

@app.route('/',methods=['POST','GET'])
def login():
	if request.method == "POST":
		name = request.form["name"]
		password = request.form["password"]

		if authenticate_session(name,password) == True:
			session = sys.get_session(name)
			return redirect(url_for('manage_session',sessionname=name))
		return render_template('login.html',wrongpassword=True)
	return render_template('login.html',wrongpassword=False)

@app.route('/manage_session',methods=['POST','GET'])
@login_required
def manage_session():
	if request.method == "GET":
		sessionname = request.args['sessionname']
		session = sys.get_session(sessionname)
		return render_template('manage_session.html',session = session)

	if request.method == "POST":
		sessionname = request.form['name']
		number = request.form['number']
		print("number is" + number)
		session = sys.get_session(sessionname)
		session.remove_number(int(number))
		return render_template('manage_session.html',session = session)

	return redirect(url_for('login'))


@app.route('/create_session',methods=['POST','GET'])
def create_session():
	if request.method == "POST":
		name = request.form['name']
		password = request.form['password']
		if(sys.get_session(name) != False):
			return render_template("create_sess.html",error=True)
		new_session = session(name,password)
		sys.add_session(new_session)
		return render_template("base.html",create=True)
	return render_template("create_sess.html",error=False)

def authenticate_session(name,password):
	if sys.verify_user(name,password) == True:
		user = sys.get_session(name)
		login_user(user)
		return True
	return False

@app.route('/join_session',methods=['POST','GET'])
def join_session():
	if request.method == "POST":
		name = request.form['name']
		qty = request.form['qty']

		session = sys.get_session(name)
		if session == False:
			return render_template("session.html",number=False,join=False)
		number = session.get_number()
		session.set_quantity(number,qty)
		return render_template("session.html",number=number,join=True,session=session)
	return render_template("session.html",join=False)

@app.route('/cancel/<cancel>/<number>',methods=['POST','GET'])
def cancel_booking(cancel,number):
	return render_template("session.html",number=number,cancel=True)
