from flask import Flask, render_template

app = Flask(__name__)

# Route pour l'accueil
@app.route('/')
def home():
    return render_template('index.html', title="Accueil")

# Route pour les principes
@app.route('/principes')
def principes():
    return render_template('principes.html', title="Principes")

# Route pour les obédiences
@app.route('/obediences')
def obediences():
    return render_template('obediences.html', title="Obédiences")

# Route pour l'abécédaire
@app.route('/abecedaire')
def abecedaire():
    return render_template('abecedaire.html', title="Abécédaire")

if __name__ == '__main__':
    app.run(debug=True)