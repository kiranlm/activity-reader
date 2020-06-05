"""This is init module."""

from flask import Flask
from reader.gpx import rq

# Place where app is defined
app = Flask(__name__)
rq.init_app(app)

from app import gpxReader
