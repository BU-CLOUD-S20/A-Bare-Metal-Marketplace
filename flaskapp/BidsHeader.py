from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import sqlalchemy_jsonfield

from datetime import datetime
import os
import sys
import statuses

import flaskapp.py

# Bids
class Bids(db.Model):
    bid_id = db.Column(db.String(64), primary_key=True)
    project_id = db.Column(db.String(64), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime(timezone=True), nullable=False)
    end_time = db.Column(db.DateTime(timezone=True), nullable=False)
    expire_time = db.Column(db.DateTime(timezone=True), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(16), nullable=False, default=statuses.AVAILABLE)
    config_query = db.Column(db.JSON( 
        #enforce_string=True,
        #enforce_unicode=False
        ), nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __init__(self, bid_id, project_id, quantity, start_time, end_time, expire_time, duration, status, config_query, cost):
        self.bid_id = bid_id
        self.project_id = project_id
        self.quantity = quantity 
        self.start_time = start_time
        self.end_time = end_time
        self.expire_time = expire_time
        self.duration = duration
        self.status = status
        self.config_query = config_query
        self.cost = cost  

# Bid Schema 
class BidSchema(ma.Schema):
    class Meta:
        fields = ('bid_id', 'project_id', 'quantity', 'start_time', 'end_time', 'expire_time', 'duration', 'status', 'config_query', 'cost')

