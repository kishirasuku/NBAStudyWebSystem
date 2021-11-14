from flask import *
from services.averageWService import *


yearResultViews = Blueprint("yearResultViews",__name__)

@yearResultViews.route('/homeYearResult')
def viewHomeYearResult():
    return render_template("/yearResult/homeYearResult.html")

@yearResultViews.route('/YearResult/list')
def ListYearResult():
    return render_template("/yearResult/listYearResult.html")

@yearResultViews.route('/YearResult/<year>')
def showListYearResult(year):
    year = int(year)
    resultW = queryAverageW(year)
    return render_template("/yearResult/showYearResult.html",resultW = resultW)
