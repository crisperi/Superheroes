from flask import request
from flask_restful import Resource
from models import Power, db


class PowerResource(Resource):
    def get(self,id=None):
        if id is None:
            powers= Power.query.all()
            return [power.to_dict() for power in powers], 200
        else:
            power =Power.query.get(id)
            if power:
                return {
                    "description": power.description,
                    "id": power.id,
                    "name": power.name,
                }
            else:
                return {"error": "Power not found"}, 404    
            
    def patch(self,id):
        power=Power.query.get(id)
        if not power:
            return {"error": "Power not found"}, 404
        data= request.get_json()
        if "description" in data : 
            power.description = data["description"]
        db.session.commit()
        return power.to_dict(), 200
    
        