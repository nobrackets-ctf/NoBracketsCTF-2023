from flask import Flask, render_template, request, make_response
import jwt
app = Flask(__name__)

SECRET_KEY = "badboy1"

@app.route('/')
def index():
    jwt_token = request.cookies.get('jwt')
    if not jwt_token:
        payload = {'isRedactor': False}
        jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    response = make_response(render_template('index.html'))
    response.set_cookie('jwt', jwt_token)
    return response

@app.route('/next-news-draw')
def secret():
    jwt_token = request.cookies.get('jwt')
    try:
        payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        if "isRedactor" in payload and payload["isRedactor"]==True:
            return render_template('secret-draw-news.html')
    except :
        pass
    return "Invalid JWT or isRedactor is not set to true"

if __name__ == '__main__':
    app.run(debug=False)
