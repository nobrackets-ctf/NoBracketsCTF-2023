from flask import Flask, render_template, request, make_response
import jwt
import os
import secrets
import uuid

app = Flask(__name__)

# Big thanks to https://github.com/pun-private/writeup-barbhack2023-web/tree/main/chall-intleaks

@app.route('/')
def index():
    jwt_token = request.cookies.get('jwt')
    if not jwt_token:
        key_name = str(uuid.uuid4()) + ".key"
        key_path = f"jwt_keys/{key_name}"
        user_secret = secrets.token_urlsafe(128)
        open(key_path, 'w').write(user_secret)
        payload = {'isRedactor': False}
        jwt_token = jwt.encode(payload, user_secret, algorithm="HS512", headers={"kid": key_name})
    response = make_response(render_template('index.html'))
    response.set_cookie('jwt', jwt_token)
    return response

@app.route('/next-news-draw')
def secret():
    try:
        jwt_token = request.cookies.get('jwt')
        
        jwt_header = jwt.get_unverified_header(jwt_token)
        if ("kid" not in jwt_header):
            return 'Missing kid in JWT header.'

        key_path = f"jwt_keys/{jwt_header['kid']}"
        if (not os.path.exists(key_path)):
            return 'Key file not found.'

        if (os.path.getsize(key_path) == 0):
            return 'Key file is empty.'

        with open(key_path, 'r') as file:
            user_secret = file.read()
        payload = jwt.decode(jwt_token, user_secret, algorithms="HS512")
        if "isRedactor" in payload and payload["isRedactor"]==True:
            return render_template('secret-draw-news.html', jwt=jwt_token)
    except:
        pass
    return "Invalid JWT or isRedactor is not set to true"

if __name__ == '__main__':
    app.run(debug=False)
