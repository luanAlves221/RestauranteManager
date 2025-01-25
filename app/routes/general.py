from flask import Blueprint, render_template, request, url_for, flash, redirect, session

general = Blueprint("general", __name__)

@general.route("/")
def index():
    if "usuario" in session:
        return render_template("dashboard.html")
    else:
        return render_template("index.html")

@general.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        flash("Por favor, faça login para acessar a sua conta.")
        return redirect(url_for("general.index"))
    return render_template("dashboard.html")

@general.route("/logout")
def logout():
    session.clear()
    
    flash("saindo...")
    return redirect(url_for("auth.login"))
