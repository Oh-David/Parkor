from app import db

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    
class ParkingSpace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50), nullable=False)
    daily_rate = db.Column(db.Float)
    hourly_rate = db.Column(db.Float)
    weekly_rate = db.Column(db.Float)
    monthly_rate = db.Column(db.Float)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
