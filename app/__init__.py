from flask import Flask, jsonify


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):

    ''' this function is for catching anerror and 
        returning a message incase of an invalid url '''
    response = jsonify({"message": "Please put a valid URL"})
    response.status_code = 405
    return response

from app.views import product_view
