import os
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask import Flask,Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from bson.objectid import ObjectId
from flask_login import login_required, current_user
from datetime import datetime
from flask_login import UserMixin



db = SQLAlchemy()
mongo = PyMongo()



app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["MONGO_DBNAME"] = 'Artist'
app.config["MONGO_URI"] = "themongouri"


db.init_app(app)
mongo.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False


    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))

    login_user(user, remember=remember)

    return redirect(url_for('index'))

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    user_name = User.query.filter_by(name = name).first()
    if user:
        flash('Email address already exists.')
        return redirect(url_for('signup'))
    elif user_name:
        flash('Username already exists please chose another Username')
        return redirect(url_for('signup'))
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
    
@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect("login")
    else:
        return render_template('index.html', artist = mongo.db.artist_data.find() ,name=current_user.name)


@app.route("/<artist_name>/<artist_id>" )
def artist_page(artist_id ,artist_name):
    
    date = datetime.now().strftime("%d %b %Y")
    time = datetime.now().strftime("%H:%M:%S")

    artist = mongo.db.artist_data.find_one({"_id":ObjectId(artist_id)})
    comments = mongo.db.comments.find({"artist_id":ObjectId(artist_id)})
    nr_comments = mongo.db.comments.count({"artist_id":ObjectId(artist_id)})
    

    return render_template("artistpage.html", artist_id = artist_id , artist = artist, comments = comments , nr_comments = nr_comments ) 

@app.route("/<artist_id>/<artist_name>", methods = ["POST"])
def insert_comment(artist_id,artist_name):
    date = datetime.now().strftime("%d %b %Y")
    time = datetime.now().strftime("%H:%M:%S")

    
    messages_conn = mongo.db.comments
    messages_doc = {"messages":request.form.get('messages') ,"user_id":current_user.id, "user":current_user.name, "date":date, "time":time, "artist_id":ObjectId(artist_id)}
    messages_conn.insert_one(messages_doc)
    return redirect(url_for("artist_page",artist_id = artist_id, artist_name = artist_name) + "#sendform")

@app.route("/<comments_id>/<artist_name>/<artist_id>" )
def delete_comment(comments_id,artist_name,artist_id):
    mongo.db.comments.remove({"_id":ObjectId(comments_id)})
    return redirect(url_for("artist_page",artist_id = artist_id, artist_name = artist_name ) + "#sendform")


@app.route("/edit_message/<comments_id>/<artist_id>")
def edit_message(comments_id,artist_id):
    the_message = mongo.db.comments.find_one({"_id":ObjectId(comments_id)})
    artist_id = mongo.db.artist_data.find_one({"_id":ObjectId(artist_id)})
    return render_template("editmessage.html", messages = the_message ,artist = artist_id )

@app.route("/update_message/<comments_id>/<artist_name>/<artist_id>", methods = ["POST"])
def update_comment(comments_id,artist_id,artist_name):
    date = datetime.now().strftime("%d %b %Y")
    time = datetime.now().strftime("%H:%M:%S")
    
    messages = mongo.db.comments.update({"_id":ObjectId(comments_id)},
    {
       "date":date,
       "messages":request.form.get("messages"),
       "user":current_user.name,
       "time":time,
       "artist_id":ObjectId(artist_id),
       "user_id":current_user.id
    })
    return redirect(url_for("artist_page" ,artist_id = artist_id, artist_name = artist_name ) + "#sendform")
    


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),port=os.environ.get("PORT"),debug=True)
