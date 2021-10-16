from flask import request, redirect, url_for, render_template, flash, session
from test_app import app
from test_app import db, bcrypt
from test_app.models.user import User
from test_app.forms.users_form import UserForm
from flask_login import login_required, current_user, login_user, logout_user

@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/register_user.html", form = form)
    
    else:
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(str(form.password.data))
            user = User(
                username = form.username.data,
                password = hashed_password
            )
            db.session.add(user)
            db.session.commit()
            flash("Registered")
            return render_template("login.html")      
        return render_template("users/register_user.html", form=form)