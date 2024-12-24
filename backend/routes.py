from flask import Blueprint, jsonify, request
from backend.models import User, Brewery, Bar, Beer, Event, EventBar, BarAddedBeer, Review
from backend.extensions import db

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@api_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(email=data['email'], username=data['username'], country=data['country'], rol=data['rol'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())

@api_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    return jsonify(user.serialize())

@api_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    user.email = data['email']
    user.username = data['username']
    user.country = data['country']
    user.rol = data['rol']
    db.session.commit()
    return jsonify(user.serialize())

@api_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})

@api_blueprint.route('/breweries', methods=['GET'])
def get_breweries():
    breweries = Brewery.query.all()
    return jsonify([brewery.serialize() for brewery in breweries])

@api_blueprint.route('/breweries', methods=['POST'])
def create_brewery():
    data = request.get_json()
    brewery = Brewery(name=data['name'], address=data['address'], history=data['history'], facebook_url=data['facebook_url'], instagram_url=data['instagram_url'], x_url=data['x_url'], picture_of_brewery_url=data['picture_of_brewery_url'], logo_of_brewery_url=data['logo_of_brewery_url'], latitude=data['latitude'], longitude=data['longitude'])
    db.session.add(brewery)
    db.session.commit()
    return jsonify(brewery.serialize())

@api_blueprint.route('/breweries/<int:brewery_id>', methods=['GET'])
def get_brewery(brewery_id):
    brewery = Brewery.query.get(brewery_id)
    return jsonify(brewery.serialize())

@api_blueprint.route('/breweries/<int:brewery_id>', methods=['PUT'])
def update_brewery(brewery_id):
    data = request.get_json()
    brewery = Brewery.query.get(brewery_id)
    brewery.name = data['name']
    brewery.address = data['address']
    brewery.history = data['history']
    brewery.facebook_url = data['facebook_url']
    brewery.instagram_url = data['instagram_url']
    brewery.x_url = data['x_url']
    brewery.picture_of_brewery_url = data['picture_of_brewery_url']
    brewery.logo_of_brewery_url = data['logo_of_brewery_url']
    brewery.latitude = data['latitude']
    brewery.longitude = data['longitude']
    db.session.commit()
    return jsonify(brewery.serialize())

@api_blueprint.route('/breweries/<int:brewery_id>', methods=['DELETE'])
def delete_brewery(brewery_id):
    brewery = Brewery.query.get(brewery_id)
    db.session.delete(brewery)
    db.session.commit()
    return jsonify({'message': 'Brewery deleted'})

@api_blueprint.route('/bars', methods=['GET'])
def get_bars():
    bars = Bar.query.all()
    return jsonify([bar.serialize() for bar in bars])

@api_blueprint.route('/bars', methods=['POST'])
def create_bar():
    data = request.get_json()
    bar = Bar(name=data['name'], address=data['address'], history=data['history'], facebook_url=data['facebook_url'], instagram_url=data['instagram_url'], x_url=data['x_url'], picture_of_bar_url=data['picture_of_bar_url'], logo_of_bar_url=data['logo_of_bar_url'], latitude=data['latitude'], longitude=data['longitude'])
    db.session.add(bar)
    db.session.commit()
    return jsonify(bar.serialize())

@api_blueprint.route('/bars/<int:bar_id>', methods=['GET'])
def get_bar(bar_id):
    bar = Bar.query.get(bar_id)
    return jsonify(bar.serialize())

@api_blueprint.route('/bars/<int:bar_id>', methods=['PUT'])
def update_bar(bar_id):
    data = request.get_json()
    bar = Bar.query.get(bar_id)
    bar.name = data['name']
    bar.address = data['address']
    bar.history = data['history']
    bar.facebook_url = data['facebook_url']
    bar.instagram_url = data['instagram_url']
    bar.x_url = data['x_url']
    bar.picture_of_bar_url = data['picture_of_bar_url']
    bar.logo_of_bar_url = data['logo_of_bar_url']
    bar.latitude = data['latitude']
    bar.longitude = data['longitude']
    db.session.commit()
    return jsonify(bar.serialize())

@api_blueprint.route('/bars/<int:bar_id>', methods=['DELETE'])
def delete_bar(bar_id):
    bar = Bar.query.get(bar_id)
    db.session.delete(bar)
    db.session.commit()
    return jsonify({'message': 'Bar deleted'})

@api_blueprint.route('/beers', methods=['GET'])
def get_beers():
    beers = Beer.query.all()
    return jsonify([beer.serialize() for beer in beers])

@api_blueprint.route('/beers', methods=['POST'])
def create_beer():
    data = request.get_json()
    beer = Beer(name=data['name'], bjcp_style=data['bjcp_style'], IBUs=data['IBUs'], volALC=data['volALC'], description=data['description'], picture_of_beer_url=data['picture_of_beer_url'])
    db.session.add(beer)
    db.session.commit()
    return jsonify(beer.serialize())

@api_blueprint.route('/beers/<int:beer_id>', methods=['GET'])
def get_beer(beer_id):
    beer = Beer.query.get(beer_id)
    return jsonify(beer.serialize())

@api_blueprint.route('/beers/<int:beer_id>', methods=['PUT'])
def update_beer(beer_id):
    data = request.get_json()
    beer = Beer.query.get(beer_id)
    beer.name = data['name']
    beer.bjcp_style = data['bjcp_style']
    beer.IBUs = data['IBUs']    
    beer.volALC = data['volALC']
    beer.description = data['description']
    beer.picture_of_beer_url = data['picture_of_beer_url']
    db.session.commit()
    return jsonify(beer.serialize())

@api_blueprint.route('/beers/<int:beer_id>', methods=['DELETE'])
def delete_beer(beer_id):
    beer = Beer.query.get(beer_id)
    db.session.delete(beer)
    db.session.commit()
    return jsonify({'message': 'Beer deleted'})

@api_blueprint.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([event.serialize() for event in events])

@api_blueprint.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = Event(name=data['name'], description=data['description'], date=data['date'], picture_of_event_url=data['picture_of_event_url'])
    db.session.add(event)
    db.session.commit()
    return jsonify(event.serialize())

@api_blueprint.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get(event_id)
    return jsonify(event.serialize())

@api_blueprint.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    event = Event.query.get(event_id)
    event.name = data['name']
    event.description = data['description']
    event.date = data['date']
    event.picture_of_event_url = data['picture_of_event_url']
    db.session.commit()
    return jsonify(event.serialize())

@api_blueprint.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Event deleted'})

@api_blueprint.route('/eventbars', methods=['GET'])
def get_eventbars():
    eventbars = EventBar.query.all()
    return jsonify([eventbar.serialize() for eventbar in eventbars])

@api_blueprint.route('/eventbars', methods=['POST'])
def create_eventbar():
    data = request.get_json()
    eventbar = EventBar(name=data['name'], description=data['description'], date=data['date'], picture_of_event_url=data['picture_of_event_url'])
    db.session.add(eventbar)
    db.session.commit()
    return jsonify(eventbar.serialize())

@api_blueprint.route('/eventbars/<int:eventbar_id>', methods=['GET'])
def get_eventbar(eventbar_id):
    eventbar = EventBar.query.get(eventbar_id)
    return jsonify(eventbar.serialize())

@api_blueprint.route('/eventbars/<int:eventbar_id>', methods=['PUT'])
def update_eventbar(eventbar_id):
    data = request.get_json()
    eventbar = EventBar.query.get(eventbar_id)
    eventbar.name = data['name']
    eventbar.description = data['description']
    eventbar.date = data['date']
    eventbar.picture_of_event_url = data['picture_of_event_url']
    db.session.commit()
    return jsonify(eventbar.serialize())

@api_blueprint.route('/eventbars/<int:eventbar_id>', methods=['DELETE'])
def delete_eventbar(eventbar_id):
    eventbar = EventBar.query.get(eventbar_id)
    db.session.delete(eventbar)
    db.session.commit()
    return jsonify({'message': 'EventBar deleted'})

@api_blueprint.route('/baraddedbeers', methods=['GET'])
def get_baraddedbeers():
    baraddedbeers = BarAddedBeer.query.all()
    return jsonify([baraddedbeer.serialize() for baraddedbeer in baraddedbeers])

@api_blueprint.route('/baraddedbeers', methods=['POST'])
def create_baraddedbeer():
    data = request.get_json()
    baraddedbeer = BarAddedBeer(name=data['name'], bjcp_style=data['bjcp_style'], IBUs=data['IBUs'], volALC=data['volALC'], description=data['description'], picture_of_beer_url=data['picture_of_beer_url'])    
    db.session.add(baraddedbeer)
    db.session.commit()
    return jsonify(baraddedbeer.serialize())

@api_blueprint.route('/baraddedbeers/<int:baraddedbeer_id>', methods=['GET'])
def get_baraddedbeer(baraddedbeer_id):
    baraddedbeer = BarAddedBeer.query.get(baraddedbeer_id)
    return jsonify(baraddedbeer.serialize())

@api_blueprint.route('/baraddedbeers/<int:baraddedbeer_id>', methods=['PUT'])
def update_baraddedbeer(baraddedbeer_id):
    data = request.get_json()
    baraddedbeer = BarAddedBeer.query.get(baraddedbeer_id)
    baraddedbeer.name = data['name']
    baraddedbeer.bjcp_style = data['bjcp_style']
    baraddedbeer.IBUs = data['IBUs']    
    baraddedbeer.volALC = data['volALC']
    baraddedbeer.description = data['description']
    baraddedbeer.picture_of_beer_url = data['picture_of_beer_url']
    db.session.commit()
    return jsonify(baraddedbeer.serialize())

@api_blueprint.route('/baraddedbeers/<int:baraddedbeer_id>', methods=['DELETE'])
def delete_baraddedbeer(baraddedbeer_id):
    baraddedbeer = BarAddedBeer.query.get(baraddedbeer_id)
    db.session.delete(baraddedbeer)
    db.session.commit()
    return jsonify({'message': 'BarAddedBeer deleted'})

@api_blueprint.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.serialize() for review in reviews])

@api_blueprint.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    review = Review(rating=data['rating'], comment=data['comment'])
    db.session.add(review)
    db.session.commit()
    return jsonify(review.serialize())

@api_blueprint.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get(review_id)
    return jsonify(review.serialize())

@api_blueprint.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = Review.query.get(review_id)
    review.rating = data['rating']
    review.comment = data['comment']
    db.session.commit()
    return jsonify(review.serialize())

@api_blueprint.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted'})

