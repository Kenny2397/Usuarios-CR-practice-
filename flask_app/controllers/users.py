from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.users import User
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)    

@app.route('/')
def main():
    users = User.read()
    
    return render_template('leer.html',users=users)

@app.route('/new')
def new():
    return render_template("crear.html")

@app.route('/create', methods=['POST'])
def create():
    User.create(request.form)
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete():
    return redirect('/')