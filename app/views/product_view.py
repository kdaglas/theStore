''' these are the imports modules for the required packages '''
from app import app
from flask import request, json, jsonify
from app.models.product_model import Product
from app.validation import Validator
import uuid


product = Product()

@app.route("/api/v1/products", methods=['POST'])
def adding_product():

    ''' this function helps the store owner to create or add a product through the POST method it takes in input 
        from the owner which is the product and its arguments and posts the data returning the product made. '''
    try:
        data = request.get_json()
        productId = int(str(uuid.uuid1().int)[:5])
        product_name = data.get('product_name')
        unit_price = data.get('unit_price')
        quantity = data.get('quantity')
        category = data.get('category')
        valid = Validator.validate_product_inputs(data['product_name'], data['unit_price'], data['quantity'], data['category'])
        if valid == True:
            added_product = product.add_product(productId, product_name, unit_price, quantity, category)
            return jsonify({'Added_product': added_product,
                            'message': 'Product has been added'}), 201
        else:
            return jsonify({"message":valid}), 400
    except:
        return jsonify({"message": "The key or value fields are invalid or missing, please check"}), 403
