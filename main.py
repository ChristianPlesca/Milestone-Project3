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
    data = {
        'artist_name':request.form.get("artist_name"),
        'artist_genre':request.form.get("artist_genre"),
        'artist_description':request.form.get('artist_description'),
        'artist_members':request.form.get("artist_members"),
        'artist_albums':request.form.get("artist_albums"),
        'album_url':request.form.get('album_url'),
        'artist_icon':request.form.get('artist_icon')
    }


    artist_id = mongo.db.artist_data.find_one({"_id":ObjectId(artist_id)})

    comments = mongo.db.comments.find()

    return render_template("artistpage.html", artist_id = artist_id , comments = comments ) 

@main.route("/insert_comment/<artist_id>", methods = ["POST"])
def insert_comment(artist_id):
    date = datetime.now().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%H:%M:%S")
    artist_id = mongo.db.artist_data.find_one({"_id":ObjectId(artist_id)})
    
    messages_conn = mongo.db.comments
    messages_doc = {"messages":{request.form.get('messages') : current_user.id }, "user":current_user.name, "date":date, "time":time, "artist_id":artist_id.items()[4][1] }
    messages_conn.insert_one(messages_doc)
    return redirect(url_for("main.index"))

@main.route("/<comments_id>")
def delete_comment(comments_id):
    mongo.db.comments.remove({"_id":ObjectId(comments_id)})
    return redirect(url_for("main.artist_page"))


@main.route("/edit_message/<comments_id>")
def edit_message(comments_id):
    the_message = mongo.db.comments.find_one({"_id":ObjectId(comments_id)})
    return render_template("editmessage.html", messages = the_message)

@main.route("/update_message/<comments_id>", methods = ["POST"])
def edit_comment(comments_id):
    messages = mongo.db.comments.update({"_id":ObjectId(comments_id)},
    {
       "date":request.form.get("date"),
       "messages":request.form.get("messages"),
       "user":request.form.get("user"),
       "time":request.form.get("time") 
    })
    return redirect(url_for('main.index'))