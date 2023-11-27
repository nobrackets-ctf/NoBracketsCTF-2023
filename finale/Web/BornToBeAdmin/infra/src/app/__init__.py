##################################################################
# This app is vulnerable to several attacks as it was created    #
# for the NoBracketsCTF 2023 finals, don't use in in production. #
#                                                                #
# @Author : Drahoxx                                              #
# @Created : 19 nov. 2023                                        #
# @LastModified : 19 nov. 2023                                   #
# @Comments : Bon flag !                                         #
##################################################################

from flask import Flask, render_template, request, redirect, session, url_for, jsonify, flash, render_template_string
from hashlib import sha256
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)  # Secret key for session management

# Route 1: Default static page
@app.route('/')
def default_page():
    return render_template("default.html", is_admin=(session.get('isAdmin',default=False)==True))

# Route 2: Login using SQLite database
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        print(username)
        print(password)
        # Validate the login credentials with hashed password
        user_info = validate_login(username, password)

        if user_info:
            # Create a session token with user information
            session['username'] = user_info['username']
            session['isAdmin'] = user_info['isAdmin']
            flash(f"Login successful. Welcome, {username}!")
        else:
            flash("Login failed. Please check your credentials.")
        return ""

# Route 3: Search in SQLite database
@app.route('/search', methods=['POST'])
def search():
    # Check if the user is authenticated
    query = request.json.get("search")
    result = search_database(query)
    return jsonify(result)
        

# Route 4: Admin route with inline template rendering
@app.route('/admin/', methods=['POST'])
def admin():
    # Check if the user is an admin
    if 'username' in session and session.get('isAdmin', True):
        query = request.json.get("admin_search")
        # Filter
        if "." in query or "_" in query or "'" in query:
            return "Error : . _ and ' are filtered to avoid interfering with sql."

        result = search_admin_database(query)
        res = "Hello, {{session['username']}}. You searched for the username "+query+", here is your results :\n"
        for r in result:
            res+=r[0]+"\n"
        return render_template_string(res,context=(session,))
    else:
        return "You can't access this page unless you're admin."

# Helper function to validate login credentials and retrieve user information
def validate_login(username, password):
    conn = sqlite3.connect('database.db')  # Replace 'your_database.db' with your actual database file
    cursor = conn.cursor()

    cursor.execute('SELECT username, is_admin, password FROM users WHERE username=?', (username,))
    user_info = cursor.fetchone()

    conn.close()

    if user_info:
        stored_password = user_info[2]
        # Verify the hashed password
        print(stored_password)
        print(sha256(password.encode()).hexdigest())
        if sha256(password.encode()).hexdigest() == stored_password:
            return {'username': user_info[0], 'isAdmin': bool(user_info[1])}

    return None

# Helper function to search in the database
def search_database(query):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT content FROM data WHERE content LIKE '%{query}%'")
    result = cursor.fetchall()

    conn.close()

    return result
def search_admin_database(query):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT username FROM users WHERE username LIKE '%{query}%'")
    result = cursor.fetchall()

    conn.close()

    return result
if __name__ == '__main__':
    app.run(debug=False)
