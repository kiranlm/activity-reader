from flask import request, jsonify, make_response
from app import app
from functools import wraps
import json
from app.reader.gpx import parseGpx

@app.route("/")
def get_initial_response():
    """Welcome message"""
    # Message
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'API v1.0'
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp

@app.route('/api/v1/process-gpx', methods=['POST'])
def process_gpx():
    gpxFile = request.files['gpx']
    # return jsonify(data)
    data = parseGpx(gpxFile)
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    """Send message to the user with notFound 404 status."""
    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp
