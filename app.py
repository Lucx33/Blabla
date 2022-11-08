from flask import Flask, redirect, url_for, render_template, request, abort
import pymongo
from flask_bcrypt import Bcrypt




app = Flask(__name__)
bcrypt = Bcrypt(app)





client = pymongo.MongoClient("mongodb+srv://pstud:gVJQTsM2ftVKES5d@inf1039cardapuc.1cskrne.mongodb.net/?retryWrites=true&w=majority")

db = client.cardapuc

col = db.restaurantes


@app.route("/", methods=["POST", "GET"])
def landing_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        result = col.find_one({"username": username})
        try:
            pw_hash = bcrypt.generate_password_hash(password)
            col.find_one({"password": pw_hash})
        except:
            abort(404)
        return render_template("register.html", result = result)
    
    return render_template("register.html")
