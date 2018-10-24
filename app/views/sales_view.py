''' these are the imports modules for the required packages '''
from app import app
from flask import request, json, jsonify
from app.models.sales_model import SaleRecord
from app.validation import Validator
from datetime import datetime
import uuid


record = SaleRecord()

@app.route("/api/v1/sales", methods=['POST'])
def creating_sale_record():

    ''' this function helps the store attendant to create a sale record through the POST method it takes in input 
        from the attendant which is the sale record and its arguments and posts the data returning the record created. '''
    try:
        data = request.get_json()
        recordId = int(str(uuid.uuid1().int)[:5])
        product_name = data.get('product_name')
        quantity = data.get('quantity')
        pay_amount = data.get('pay_amount')
        attendant = data.get('attendant')
        today = datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        valid = Validator.validate_sale_record_inputs(data['product_name'], data['quantity'], data['pay_amount'], data['attendant'])
        if valid == True:
            created_record = record.create_record(recordId, product_name, quantity, pay_amount, attendant, today)
            return jsonify({'Created_record': created_record,
                            'message': 'Sale record has been created'}), 201
        else:
            return jsonify({"message":valid}), 400
    except:
        return jsonify({"message": "The key or value fields are invalid or missing, please check"}), 403


@app.route("/api/v1/sales", methods=['GET'])
def fetch_all_the_sale_records():
    
    ''' this function routes to /api/v1/sales and uses the GET method to return all the sale records created '''
    all_sales = record.fetch_all_the_sales()
    if all_sales:
        return jsonify({'All_sales': all_sales,
                        'message': 'All sale records viewed'}), 200
    return jsonify({'message': 'No sale record found'}), 404


@app.route("/api/v1/sales/<recordId>", methods=["GET"])
def fetch_a_single_sale_record(recordId):
    
    ''' this function routes to /api/v1/sales/<recordId> and uses the GET method to return one created sale record '''
    valid = Validator.validate_input_type(recordId)
    if valid:
        return jsonify({"message":valid}), 400
    one_sale_record = record.fetch_one_sale_record(recordId)
    if one_sale_record:
        return jsonify({"Your_sale_record": one_sale_record,
                        'message': 'One sale record viewed'}), 200
    return jsonify({'message': 'No sale record found with that id'}), 404
        