from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates, relationship
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin



metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model,SerializerMixin):
    __tablename__ = "heroes"
    
    id =db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    super_name = db.Column(db.String,nullable=False)
    
    powers =relationship("HeroPower",back_populates="hero",cascade="all, delete-orphan")
    
    serialize_rules =("-powers.hero",)
    
    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "super_name":self.super_name
        }
    
    def __repr__(self):
        return f"<Hero {self.id}, {self.name}, {self.super_name}>"
    

class Power(db.Model,SerializerMixin):
    __tablename__ ="powers"
    
    id =db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String)
    description = db.Column(db.String)
    
    
    heroes =relationship("HeroPower",back_populates="power",cascade="all, delete-orphan")
    
    @validates("description")
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return value

    serialize_rules=("-heroes.power",)
    
    def __repr__(self):
        return f"<Power {self.id}, {self.name}, {self.description}>"
    
class HeroPower(db.Model,SerializerMixin):
    __tablename__ = "hero_powers"
    
    id = db.Column(db.Integer, primary_key=True)
    strength=db.Column(db.String)
    hero_id =db.Column(db.Integer,db.ForeignKey("heroes.id"))
    power_id =db.Column(db.Integer,db.ForeignKey("powers.id"))
    
    hero =relationship("Hero",back_populates="powers")
    power =relationship("Power",back_populates="heroes")
    
    
    serialize_rules =("-hero.powers","-power.heroes")
    @validates("strength")
    def validate_strength(self,key,value ):
        allowed =["Strong","Weak","Average"]
        
        if value not in allowed :
            raise ValueError(f"Strength must be one of {allowed}")
        return value
    
    
    def __repr__(self):
        return f"<HeroPower {self.hero_id}, {self.power_id}, {self.strength}>"
    
