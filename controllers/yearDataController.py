from flask import *
from services.averageWService import queryAverageW

yearDataViews = Blueprint("yearDataViews",__name__)

@yearDataViews.route('/homeYearData')
def viewHomeYearData():
    return render_template("/yearData/homeYearData.html")

