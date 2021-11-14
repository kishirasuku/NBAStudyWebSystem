from flask import *
from models import *
from models.averageW import averageW
from services.averageWService import queryAverageW
from controllers.yearDataController import *
from controllers.yearResultController import *
from controllers.homeController import *

app = Flask(__name__)

app.register_blueprint(homeViews)
app.register_blueprint(yearDataViews)
app.register_blueprint(yearResultViews)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)