from flask import Blueprint, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.user import User

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Este email já está cadastrado. Tente fazer login ou use outro email.")
            return redirect(url_for("auth.signup"))


        user = User(username=username, email=email, password=generate_password_hash(password))


        db.session.add(user)
        db.session.commit()

        flash("Conta criada com sucesso!")
        return redirect(url_for("auth.login"))

    return render_template("signup.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash("Email ou senha incorretos. Tente novamente.")
            return redirect(url_for("auth.login"))

        session["usuario"] = {"nome": user.username, "email": user.email}
        return redirect(url_for("general.dashboard"))
        

    return render_template("login.html")

@auth.route("/logout")
def logout():
    session.clear()
    
    flash("saindo...")
    return redirect(url_for("auth.login"))