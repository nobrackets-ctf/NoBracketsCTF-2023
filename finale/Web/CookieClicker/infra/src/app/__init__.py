##################################################################
# This app is vulnerable to several attacks as it was created    #
# for the NoBracketsCTF 2023 finals, don't use in in production. #
#                                                                #
# @Author : Drahoxx                                              #
# @Created : 19 nov. 2023                                        #
# @LastModified : 19 nov. 2023                                   #
# @Comments : Bon flag !                                         #
##################################################################

from flask import Flask, render_template, request, make_response, url_for, jsonify, flash, render_template_string
from hashlib import sha256
import sqlite3
import os

app = Flask(__name__)

# Route 1: Default static page
@app.route('/')
def default_page():
	resp = make_response(render_template("default.html"))
	resp.set_cookie('score', "0")
	return resp

# Route 2: flag checking
@app.route('/flag', methods=['POST'])
def flag():
	request_data = request.get_json()
	if 'score' not in request_data:
		return jsonify({'error': 'Missing score parameter in JSON request'}), 400
	received_score = request_data['score']
	if received_score > 100000:
		if 'score' in request.cookies:
			if int(request.cookies['score'])==received_score:
				return jsonify({'flag': 'NBCTF{Tru3_Click3rMaster_OnlY_Uses_C00ki3s}'}), 200
			return jsonify({'flag': "Cookie score should be equal to received_score."}), 200
		return jsonify({'flag': "Cookie score should be defined."}), 200
	return jsonify({'flag': "Score should be greater than 100.000."}), 200
	
if __name__ == '__main__':
	app.run(debug=False)
