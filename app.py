from flask import Flask, redirect, url_for, render_template, request, abort
import pymongo
from flask_bcrypt import Bcrypt




app = Flask(__name__)
bcrypt = Bcrypt(app)





client = pymongo.MongoClient("mongodb+srv://pstud:gVJQTsM2ftVKES5d@inf1039cardapuc.1cskrne.mongodb.net/?retryWrites=true&w=majority&authSource=admin")

db = client.cardapuc

col = db.usuarios


@app.route("/", methods=["POST", "GET"])
@app.route("/login/", methods=["POST", "GET"])
def landing_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        result = col.find_one({"username": username})
        if result is not None:
            pw_unhash = bcrypt.check_password_hash(result["password"], password)
            if pw_unhash == False:
                return render_template("failure.html")
            else:
                return "<p>login</p>"

        else:
            pw_hash = bcrypt.generate_password_hash(password)
            col.insert_one({"username": username, "password": pw_hash}) 
        
        return "<p>Success</p>"# render_template("register.html")
    
    return render_template("register.html")


