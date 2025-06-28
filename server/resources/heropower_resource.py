from flask_restful import Resource
from models import HeroPower

class HeroPowerResource(Resource):
    def get(self):
        hero_powers = HeroPower.query.all()
        return [hero_power.to_dict() for hero_power in hero_powers], 200

    def post(self):
        # Logic to create a new HeroPower
        pass

    def delete(self, id):
        # Logic to delete a HeroPower by id
        pass    