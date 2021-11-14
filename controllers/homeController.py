from flask import *

homeViews = Blueprint("homeViews",__name__)

@homeViews.route('/')
def home():
    return render_template("index.html")
