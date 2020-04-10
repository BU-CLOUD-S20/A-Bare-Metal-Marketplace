import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
Offers = [
    {'id': 0,
     'Machine Configuration': 'CPU, RAM, GPU',
     'Allocated Time': '1 hour',
     'Expiry Time': '6:30 AM',
     'Cost': '$500'},
    {'id': 1,
     'Machine Configuration': 'CPU, RAM, GPU',
     'Allocated Time': '2 hours',
     'Expiry Time': '7:30 AM',
     'Cost': '$1000'},
    {'id': 2,
     'Machine Configuration': 'CPU, RAM, GPU',
     'Allocated Time': '3 hours',
     'Expiry Time': '9:30 AM',
     'Cost': '$7800'}
]


Bids = [
    {'bid_id': '0',
     'project_id': '0',
     'quantity': '50',
     'start_time': '7:30',
     'end_time': '8:30',
     'duration': '1 hour',
     'status': 'open',
     'config_query': '??',
     'cost': '$500'},

    {'bid_id': '1',
     'project_id': '1',
     'quantity': '10',
     'start_time': '9:30',
     'end_time': '11:30',
     'duration': '2 hours',
     'status': 'open',
     'config_query': '??',
     'cost': '$600'},

    {'bid_id': '2',
     'project_id': '2',
     'quantity': '20',
     'start_time': '10:30',
     'end_time': '13:30',
     'duration': '3 hours',
     'status': 'open',
     'config_query': '??',
     'cost': '$1500'}
]




@app.route('/', methods=['GET'])
def home():
    return '''<h1>Auction Engine for Bare Metal Servers</h1>
<p>Ayush Upneja</p>'''


@app.route('/api/v1/resources/offers/all', methods=['GET'])
def api_all():
    return jsonify(Offers)


@app.route('/foo', methods=['POST']) 
def foo():
    data = request.json
    return jsonify(data)


@app.route('/api/v1/resources/offers', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for offer in Offers:
        if offer['id'] == id:
            results.append(offer)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()