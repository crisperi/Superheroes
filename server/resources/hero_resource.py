from flask_restful import Resource 
from models import Hero

class HeroResource(Resource):
    def get(self):
        heroes =Hero.query.all()
        
        return [hero.to_dict() for hero in heroes],200