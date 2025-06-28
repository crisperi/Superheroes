
from flask_Restful import Resource
from models import Power

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