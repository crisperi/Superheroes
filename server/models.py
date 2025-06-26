from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model):
    __tablename__ = "heroes"
    
    id =db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    super_name = db.Column(db.String,nullable=False)
    
    def __repr__(self):
        return f"<Hero {self.id}, {self.name}, {self.super_name}>"
    

class Power(db.Model):
    __tablename__ ="powers"
    
    id =db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String)
    description = db.Column(db.String)
    
    @validates("description")
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return value


    def __repr__(self):
        return f"<Power {self.id}, {self.name}, {self.description}>"
    
class HeroPower(db.Model):
    __tablename__ = "hero_powers"
    
    id = db.Column(db.Integer, primary_key=True)
    strength=db.Column(db.String)
    hero_id =db.Column(db.Integer,db.ForeignKey("heroes.id"))
    power_id =db.Column(db.Integer,db.ForeignKey("powers.id"))
    
    @validates("strength")
    def validate_strength(self,key,value ):
        allowed =["Strong","Weak","Average"]
        
        if value not in allowed :
            raise ValueError(f"Strength must be one of {allowed}")
        return value
    
    
    def __repr__(self):
        return f"<HeroPower {self.hero_id}, {self.power_id}, {self.strength}>"
    
