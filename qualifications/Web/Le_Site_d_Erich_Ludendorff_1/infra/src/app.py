from flask import Flask, render_template, request, make_response, redirect, render_template_string, flash
import sqlite3
import os
from flag import FLAG_1, FLAG_2

app = Flask(__name__)
app.secret_key = os.urandom(30).hex()

# Page d'accueil
@app.route("/")
def index():
	name = "Not connected"
	if 'userID' in request.cookies :
		name = request.cookies.get('userID')
		con = sqlite3.connect("users.db")
		cur = con.cursor()
		rq_uid = request.cookies.get('userID')
		res = cur.execute("SELECT username FROM users WHERE uid=?;",(rq_uid,)).fetchone()
		if res == None:
			flash("Invalid token.")
			return redirect("/logout")
		name = res[0]
	return render_template("index.html",name=name)

# Déconnexion
@app.route("/logout")
def logout():
	resp = make_response(redirect("/"))
	resp.delete_cookie('userID')
	return resp

# Page des cibles des attaques
@app.route("/ziel")
def targets():
	con = sqlite3.connect("users.db")
	cur = con.cursor()
	rq_uid = request.cookies.get('userID')
	res = cur.execute("SELECT username,grade FROM users WHERE uid=?;",(rq_uid,)).fetchone()
	if res == None:
		flash("You should be logged in to access this page")
		return redirect("/")
	name, grade = res
	if grade == "admin":
		return render_template("ziel.html", FLAG_2=FLAG_2, name=name)
	else:
		flash("You should be admin to access this page. Check out your profile, you need to have : grade='admin'.")
		return redirect("/")

# Profile
@app.route("/profile")
def profile():
	con = sqlite3.connect("users.db")
	cur = con.cursor()
	rq_uid = request.cookies.get('userID')
	res = cur.execute("SELECT username,grade,uid FROM users WHERE uid=?;",(rq_uid,)).fetchone()
	if res != None:
		username,grade,uid = res
		return render_template("profile.html", name=username, grade=grade, uid=uid, FLAG_1=FLAG_1)
	else:
		flash("You're not logged in, please login first")
		return redirect("/logout")

# Page de connexion au site
@app.route("/login",methods = ['POST','GET'])
def login():
	if request.method == "GET":
		return render_template("login.html",name="")
	elif request.method == "POST":
		# Check inputs
		if 'username' not in request.form or 'passwd' not in request.form:
			return "Error you should provide username and passwd ! <a href=\"/\">back</a>"
		# Get inputs
		rq_username, rq_passwd = request.form["username"], request.form["passwd"]
		# Base de données
		con = sqlite3.connect("users.db")
		cur = con.cursor()
		# Requête à la BDD
		try:
			result = cur.execute(f"SELECT uid FROM users WHERE username='{rq_username}' and password='{rq_passwd}';").fetchone()
		except:
			flash("Sql error ! What have you done ???")
			return redirect('/login')
		# Si la BDD retourne un utilisateur, l'utilisateur est connecté
		if result:
			flash('Logged in')
			res = make_response(redirect("/profile"))
			res.set_cookie('userID', result[0])
			return res
		else:
			flash('User not found')
			return redirect("/login")

if __name__ == "__main__":
	app.run(host="0.0.0.0")