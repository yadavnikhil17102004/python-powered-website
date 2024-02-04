from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET',  'POST'])
def  login():
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

        if password1 != password2:
            flash("Passwords Doesn't mach !!",category='error')
        else :
            #add use data to database
            flash("Account successfull created !!",category='success')
        
    return render_template("/sign_up.html")