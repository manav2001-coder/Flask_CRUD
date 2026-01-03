from flask import Blueprint,request,jsonify
from .models import User
from .db import db
from werkzeug.security import generate_password_hash,check_password_hash
import jwt 

auth = Blueprint("auth",__name__)

@auth.route("/signup/",methods=["POST"])
def signup():
    user = request.json
    firstName = user.get("firstName")
    lastName = user.get("lastName")
    email = user.get("email")
    password = user.get("password")

    if firstName and lastName and email and password:
        user =  User.query.filter_by(email=email).first()
        if user:
            return jsonify({"ok":True,"message":"User already exists"})
        user = User(firstName=firstName,lastName=lastName,email=email,password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return jsonify({"ok":True,"message":"User has been successfully created"})
    else:
        return jsonify({"ok":True,"message":"Fill all the details"})

@auth.route("/login/",methods=["POST"])
def login():
    auth = request.json
    email = auth.get("email")
    password = auth.get("password")

    if email and password:
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({"ok":True,"message":"The user doesn't exist."})
        if check_password_hash(user.password,password):
            return jsonify({"ok":True,"message":"Successfully Logged in."})
        else:
            return jsonify({"ok":True,"message":"Invalid Creds"})
    else:
        return jsonify({"ok":True,"message":"Fill the creds."})