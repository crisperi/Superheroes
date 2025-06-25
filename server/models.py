from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Model
from sqlalchemy.orm import validates


metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class Hero(db.model):
    __tablename__ = "heroes"
    
    id =db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    super_name = db.Column(db.String,nullable=False)
    
    
    

class Power(db.model):
    __tablename__ ="powers"
    
    id =db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String)
    description = db.Column(db.String)
    
    @validates("description")
    def validate_description(self, key, value):
        if len(value) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return value

class HeroPower(db.model):
    __tablename__ = "hero_powers"
    
    strength=db.Column(db.String)
    hero_id =db.Column(db.Integer,db.ForeignKey("heroes.id"))
    power_id =db.Column(db.Integer,db.ForeignKey("powers.id"))
    
    @validates("strength")
    def validate_strength(self,key,value ):
        allowed =["Strong","Weak","Average"]
        
        if value not in allowed :
            raise ValueError(f"Strength must be one of {allowed}")
        return value
    
    
    
    
