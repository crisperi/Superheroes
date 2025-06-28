from flask import Flask
from flask_migrate import Migrate
from models import db
from flask_restful import Api
from resources.hero_resource import HeroResource


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app,db)

api =Api(app)


#registering routes 
api.add_resource(HeroResource,"/heroes", "/heroes/<int:id>")

#setting up route 
if __name__=="__main__":
    app.run(port=5555,debug=True)