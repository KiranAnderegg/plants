from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    __tablename = "plants"
    plant_id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(100))
    latin_name = db.Column(db.String(100))
    watering = db.Column(db.String(100))
    sunlight = db.Column(db.String(100))

    def __init__(self, common_name, latin_name, watering, sunlight):
        self.common_name = common_name
        self.latin_name = latin_name
        self.watering = watering
        self.sunlight = sunlight

class User(db.Model):
    __tablename = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    plant_id = db.Column(db.Integer, db.ForeignKey("plants.id"))

    def __init__(self, name, email):
        self.name = name
        self.email = email
