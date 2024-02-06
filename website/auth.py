from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash
from .import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET',  'POST'])
def  login():
    if request.method == 'POST':
      email = request.form.get('email')
      password = request.form.get('password')
      user = User.query.filter_by(email=email).first()
      if user:
          if (user.password, password):
              flash('Logged in successfully!', category='success')
              return redirect(url_for('views.home'))
          else:
              flash('Incorrect password, try again.', category='error')
      else:
          flash('Email does not exist.', category='error')

    return render_template("login.html")

@auth.route('/logout')
def  logout():
    return '<p>logout</p>'

@auth.route('/sign_up', methods=['GET',  'POST'])
def  sign_up():
    if  request.method == "GET":
        pass
    elif request.method == "POST":
        #do something with the data
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if password1 != password2:
            flash("Passwords Doesn't mach !!",category='error')
        elif user :
            flash('this email already exist !!', category='error')
        else :
            new_user = User(email=email, first_name=firstname, password=password1)
            db.session.add(new_user)
            db.session.commit()

            #add use data to database
            flash("Account successfull created !!",category='success')

            return redirect(url_for('views.home'))
        
    return render_template("/sign_up.html")