from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Model


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
    
    
class HeroPower(db.model):
    __tablename__ = "hero_powers"
    
    strength=db.Column(db.String)
    hero_id =db.Column(db.Integer,db.ForeignKey("heroes.id"))
    power_id =db.Column(db.Integer,db.ForeignKey("powers.id"))
    
    
