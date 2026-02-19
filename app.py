from flask import Flask, render_template

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    # Comme vos fichiers sont en local (statiques), 'self' suffit largement
    response.headers['Content-Security-Policy'] = "default-src 'self'; style-src 'self' 'unsafe-inline';"
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Referrer-Policy'] = 'no-referrer'
    response.headers['Permissions-Policy'] = 'camera=(), microphone=(), geolocation=()'
    return response

# --- Vos routes ---
@app.route('/')
def home():
    return render_template('index.html', title="Accueil")

@app.route('/principes')
def principes():
    return render_template('principes.html', title="Principes")

@app.route('/obediences')
def obediences():
    return render_template('obediences.html', title="Obédiences")

@app.route('/abecedaire')
def abecedaire():
    return render_template('abecedaire.html', title="Abécédaire")

if __name__ == '__main__':
    app.run(debug=True)
