from flask import Flask, jsonify


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):

    ''' this function is for catching an error and 
        returning a message incase of an invalid url '''
    return jsonify({"message": "Please put a valid URL"}), 405


@app.errorhandler(405)
def method_not_allowed(e):

    ''' this function is for catching an error and 
        returning a message incase of a method not allowed '''
    return jsonify({"message": "Method not allowed"}), 405

from app.views import product_view
