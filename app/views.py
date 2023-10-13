from flask import jsonify
from app import app, db
from app.models import Venue, ParkingSpace

@app.route('/venues', methods=['GET'])
def get_venues():
    venues = Venue.query.all()
    return jsonify([v.serialize() for v in venues])

@app.route('/parkingspaces/<int:venue_id>', methods=['GET'])
def get_parkingspaces_for_venue(venue_id):
    spaces = ParkingSpace.query.filter_by(venue_id=venue_id).all()
    return jsonify([s.serialize() for s in spaces])
