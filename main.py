from flask import Blueprint, render_template ,redirect,url_for,request
from bson.objectid import ObjectId
from flask_login import login_required, current_user
from datetime import datetime
from . import db
from . import mongo

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect("login")
    else:
        return render_template('index.html', artist = mongo.db.artist_data.find() ,name=current_user.name)


@main.route("/<artist_name>/<artist_id>" )
def artist_page(artist_id ,artist_name):
    
    date = datetime.now().strftime("%d %b %Y")
    time = datetime.now().strftime("%H:%M:%S")

    artist = mongo.db.artist_data.find_one({"_id":ObjectId(artist_id)})
    comments = mongo.db.comments.find({"artist_id":ObjectId(artist_id)})
    nr_comments = mongo.db.comments.count({"artist_id":ObjectId(artist_id)})
    

    return render_template("artistpage.html", artist_id = artist_id , artist = artist, comments = comments , nr_comments = nr_comments ) 

@main.route("/<artist_id>/<artist_name>", methods = ["POST"])
def insert_comment(artist_id,artist_name):
    date = datetime.now().strftime("%d %b %Y")
    time = datetime.now().strftime("%H:%M:%S")

    
    messages_conn = mongo.db.comments
    messages_doc = {"messages":request.form.get('messages') ,"user_id":current_user.id, "user":current_user.name, "date":date, "time":time, "artist_id":ObjectId(artist_id)}
    messages_conn.insert_one(messages_doc)
    return redirect(url_for("main.artist_page",artist_id = artist_id, artist_name = artist_name) + "#sendform")

@main.route("/<comments_id>/<artist_name>/<artist_id>" )
def delete_comment(comments_id,artist_name,artist_id):
    mongo.db.comments.remove({"_id":ObjectId(comments_id)})
    return redirect(url_for("main.artist_page",artist_id = artist_id, artist_name = artist_name ) + "#sendform")


@main.route("/edit_message/<comments_id>/<artist_id>")
def edit_message(comments_id,artist_id):
    the_message = mongo.db.comments.find_one({"_id":ObjectId(comments_id)})
    artist_id = mongo.db.artist_data.find_one({"_id":ObjectId(artist_id)})
    return render_template("editmessage.html", messages = the_message ,artist = artist_id )

@main.route("/update_message/<comments_id>/<artist_name>/<artist_id>", methods = ["POST"])
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
    return redirect(url_for("main.artist_page" ,artist_id = artist_id, artist_name = artist_name ) + "#sendform")