from flask import Flask, render_template, request
from models import connect_to_db, db, User

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/get-users")
def get_users():
    users = User.query.all()
    return render_template("users.html", users = users)

@app.route("/add-user", methods=["POST"])
def add_user():
    new_username = request.form["username"]
    new_email = request.form["email"]
    new_user = User(username = new_username, email = new_email)
    db.session.add(new_user)
    db.session.commit()
    return "success"

@app.route("/update-username", methods=["POST"])
def update_username():
    old_username = request.form["old_username"]
    new_username = request.form["new_username"]
    user = User.query.filter_by(username = old_username).first()
    user.username = new_username
    db.session.add(user)
    db.session.commit()
    return "success"

@app.route("/delete-user", methods=["POST"])
def delete_user():
    username = request.form["username"]
    user = User.query.filter_by(username = username).first()
    db.session.delete(user)
    db.session.commit()
    return "success"


if __name__ == "__main__":
    connect_to_db(app)
    app.env = "development"
    app.run(port=5000, host="localhost", debug=True)

