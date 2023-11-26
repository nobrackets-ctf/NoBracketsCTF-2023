from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Afficher le fichier HTML "index.html"
    response = make_response(render_template('index.html'))
    response.headers['Flag'] = 'NBCTF{r3qU35t_h34d3R5_C0Nt41n32_1nt3r35T1N9_1Nf02}'
    return response

@app.route('/very-private-zone')
def flag():
    # Créer une réponse HTTP avec un drapeau dans les en-têtes
    response = make_response('NBCTF{goOgL3_rO8o7S_wON7_fIND_U2}')
    return response

@app.route('/robots.txt')
def robots():
    # Créer un fichier "robots.txt" avec un drapeau
    robots_txt = "User-agent: *\nDisallow: /very-private-zone"
    return robots_txt, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run()
