from flask_restful import Resource 
from models import Hero

class HeroResource(Resource):
    def get(self,id=None):
        if id is None:
            heroes =Hero.query.all()
            return [hero.to_dict() for hero in heroes],200
        else:
            hero = Hero.query.get(id)
            if hero:
                return {
                    "id": hero.id,
                    "name": hero.name,
                    "super_name": hero.super_name,
                    "hero_powers": [hero_power.to_dict() for hero_power in hero.powers]
                }
            else:
                return {"error": "Hero not found"}, 404