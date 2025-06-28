from flask import Flask
from flask_migrate import Migrate
from models import db
from flask_restful import Api
from resources.hero_resource import HeroResource
from resources.heropower_resource import HeroPowerResource
from resources.power_resource import PowerResource


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app,db)

api =Api(app)


#registering routes 
api.add_resource(HeroResource,"/heroes", "/heroes/<int:id>")
api.add_resource(HeroPowerResource,"/hero_powers")
api.add_resource(PowerResource,"/powers", "/powers/<int:id>")

#setting up route 
if __name__=="__main__":
    app.run(port=5555,debug=True)