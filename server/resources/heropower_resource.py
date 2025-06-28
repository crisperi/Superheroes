from flask_restful import Resource
from models import HeroPower,db, Hero, Power
from flask import request

class HeroPowerResource(Resource):
    def post(self):
        # Logic to create a new HeroPower
        data = request.get_json()
        hero_id = data.get("hero_id")
        power_id = data.get("power_id")
        strength = data.get("strength")
        
        if not isinstance(hero_id,int) or not isinstance(power_id, int) :
            return {"error": "hero_id and power_id must be integers"}, 400
        
        hero =Hero.query.get(hero_id)
        power = Power.query.get(power_id)
        if not hero or not power:
            return {"error": "Hero or Power not found"}, 404
        try :
            hero_power = HeroPower(strength=strength, 
                                   hero_id=hero_id,
                                   power_id=power_id)
            db.session.add(hero_power)
            db.session.commit()
            
        except ValueError as e :
            db.session.rollback()
            return {"error": "validation errors"}, 400
            
        return hero_power.to_dict(), 201