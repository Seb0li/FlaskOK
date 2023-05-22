from flask import Flask, render_template, request, redirect, url_for
import pycountry
from wtforms.validators import DataRequired
from wtforms import validators
import re
import bleach.sanitizer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/merci", methods=["POST"])
def merci():
    return render_template("merci.html")

@app.route("/formulaires", methods=["GET", "POST"])
def formulaires():
    error_message = ""
    nom = ""
    prenom = ""
    email = ""
    pays = ""
    genre = ""
    sujet = ""
    commentaire = ""
    countries = [country.name for country in pycountry.countries]

    if request.method == "POST":
        nom = bleach.clean(request.form.get('nom'))
        prenom = bleach.clean(request.form.get('prenom'))
        email = bleach.clean(request.form.get('email'))
        pays = bleach.clean(request.form.get('pays'))
        genre = bleach.clean(request.form.get('choix-genre'))
        sujet = bleach.clean(request.form.get('choix-sujet'))
        commentaire = bleach.clean(request.form.get('commentaire'))

        if not (nom.isalpha() and prenom.isalpha() and re.match(r"[^@]+@[^@]+\.[^@]+", email)):

            if not nom.isalpha():
                nom = ""
                error_message = 'Nom et Prénom doivent être alphanumériques, et l adresse email doit être valide. Vérifiez vos inputs.'
            if not prenom.isalpha():
                prenom = ""
                error_message = 'Nom et Prénom doivent être alphanumériques, et l adresse email doit être valide. Vérifiez vos inputs.'
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                email = ""
                error_message = 'Nom et Prénom doivent être alphanumériques, et l adresse email doit être valide. Vérifiez vos inputs.'

    if nom == '' or prenom == '' or email == '':
        return render_template('formulaires.html', nom=nom, prenom=prenom, email=email, countries=countries, pays=pays, genre=genre, sujet=sujet, commentaire=commentaire, error=error_message)
    else:
        return render_template('merci.html', nom=nom, prenom=prenom, email=email, countries=countries, pays=pays, genre=genre, sujet=sujet, commentaire=commentaire)


if __name__ == '__main__':
    app.run(debug=True)

