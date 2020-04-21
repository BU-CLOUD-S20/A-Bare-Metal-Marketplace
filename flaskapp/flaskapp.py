# flaskapp.py

from flask import Flask, request
import sys



# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/stardust/A-Bare-Metal-Marketplace/database_setup/APIs/')
sys.path.insert(2, '/home/stardust/A-Bare-Metal-Marketplace/database_setup/Models/')
sys.path.insert(3, '/home/stardust/A-Bare-Metal-Marketplace/database_setup/')
import marketAPI
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import marketModel as Market
import data



app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Home Page for BMM</h1>"

@app.route('/get-bids', methods=['GET', 'POST']) #allow both GET and POST requests
def get_bids():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        bids = marketAPI.bid_select_all()

        return '''<h1>view variable bids</h1>'''

    return '''<form method="POST">
                  <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/get-offers', methods=['GET', 'POST']) #allow both GET and POST requests
def get_offers():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/insert-bid', methods=['GET', 'POST']) #allow both GET and POST requests
def insert_bid():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/insert-offer', methods=['GET', 'POST']) #allow both GET and POST requests
def insert_offer():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/auction', methods=['GET', 'POST']) #allow both GET and POST requests
def auction():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/get-contracts', methods=['GET', 'POST']) #allow both GET and POST requests
def get_contracts():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == "__main__":
    engine = create_engine("mysql+pymysql://root:220110605@10.0.0.79/market")
    app.run(host='0.0.0.0')