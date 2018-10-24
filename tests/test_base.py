import unittest
from app import app
import json

class MainTesting(unittest.TestCase):

    ''' using daummy data and passing it through the api endpoints or routes '''
    wrong_fields = json.dumps(dict(product="Sugar", quantity="5", unit_price="4000", category="necessity"),)
    # add_empty_product = json.dumps(dict(product_name="", quantity="", unit_price="", category=""),)
    empty_name = json.dumps(dict(product_name="", quantity="5", unit_price="4000", category="necessity"),)
    wrong_name = json.dumps(dict(product_name="Sug765ar", quantity="5", unit_price="4000", category="necessity"),)
    empty_price = json.dumps(dict(product_name="Sugar", quantity="5", unit_price="", category="necessity"),)
    zero_price = json.dumps(dict(product_name="Sugar", quantity="5", unit_price="0", category="necessity"),)
    wrong_price = json.dumps(dict(product_name="Sugar", quantity="5", unit_price="40iuy00", category="necessity"),)
    empty_quantity = json.dumps(dict(product_name="Sugar", quantity="", unit_price="4000", category="necessity"),)
    zero_quantity = json.dumps(dict(product_name="Sugar", quantity="0", unit_price="4000", category="necessity"),)
    wrong_quantity = json.dumps(dict(product_name="Sugar", quantity="c", unit_price="4000", category="necessity"),)
    empty_category = json.dumps(dict(product_name="Sugar", quantity="5", unit_price="4000", category=""),)
    wrong_category= json.dumps(dict(product_name="Sugar", quantity="5", unit_price="4000", category="basi55c"),)
    add_product = json.dumps(dict(product_name="Sugar", quantity="5", unit_price="4000", category="necessity"),)

    wrong_sale_fields = json.dumps(dict(product="", quantity="5", pay_amount="4000", attendant="douglas"),)
    empty_product_name = json.dumps(dict(product_name="", quantity="5", pay_amount="4000", attendant="douglas"),)
    wrong_product_name = json.dumps(dict(product_name=" ", quantity="5", pay_amount="4000", attendant="douglas"),)
    empty_amount = json.dumps(dict(product_name="Sugar", quantity="5", pay_amount="", attendant="douglas"),)
    zero_amount = json.dumps(dict(product_name="Sugar", quantity="5", pay_amount="0", attendant="douglas"),)
    wrong_amount = json.dumps(dict(product_name="Sugar", quantity="5", pay_amount="40iuy00", attendant="douglas"),)
    empty_sale_quantity = json.dumps(dict(product_name="Sugar", quantity="", pay_amount="4000", attendant="douglas"),)
    zero_sale_quantity = json.dumps(dict(product_name="Sugar", quantity="0", pay_amount="4000", attendant="douglas"),)
    wrong_sale_quantity = json.dumps(dict(product_name="Sugar", quantity="vn", pay_amount="4000", attendant="douglas"),)
    empty_attendant = json.dumps(dict(product_name="Sugar", quantity="5", pay_amount="4000", attendant=""),)
    wrong_attendant= json.dumps(dict(product_name="Sugar", quantity="5", pay_amount="4000", attendant="doug678las"),)
    create_sale = json.dumps(dict(product_name="Sugar", quantity="5", pay_amount="4000", attendant="douglas"),)
    create_sale_record = json.dumps(dict(recordId="23454", product_name="Sugar", quantity="5", pay_amount="4000", attendant="douglas"),)


    def setUp(self):

        '''initialising the test client'''
        self.app = app.test_client(self)


if __name__ == '__main__':
    unittest.main()