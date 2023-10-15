from flask import jsonify, request, abort
from app import app, db
from app.models import Venue, ParkingSpace

# Fetch all venues
@app.route('/venues', methods=['GET'])
def get_venues():
    venues = Venue.query.all()
    return jsonify([v.serialize() for v in venues])

# Fetch specific venue
@app.route('/venues/<int:venue_id>', methods=['GET'])
def get_venue(venue_id):
    venue = Venue.query.get(venue_id)
    if venue is None:
        abort(404)  # Not Found
    return jsonify(venue.serialize())

# Add a new venue
@app.route('/venues', methods=['POST'])
def add_venue():
    data = request.json
    new_venue = Venue(name=data['name'], latitude=data['latitude'], longitude=data['longitude'])
    db.session.add(new_venue)
    db.session.commit()
    return jsonify(new_venue.serialize()), 201  # Created

# Update an existing venue
@app.route('/venues/<int:venue_id>', methods=['PUT'])
def update_venue(venue_id):
    venue = Venue.query.get(venue_id)
    if venue is None:
        abort(404)  # Not Found
    data = request.json
    venue.name = data['name']
    venue.latitude = data['latitude']
    venue.longitude = data['longitude']
    db.session.commit()
    return jsonify(venue.serialize())

# Delete a venue
@app.route('/venues/<int:venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    venue = Venue.query.get(venue_id)
    if venue is None:
        abort(404)  # Not Found
    db.session.delete(venue)
    db.session.commit()
    return jsonify({}), 204  # No Content

# Similar endpoints can be created for ParkingSpace
