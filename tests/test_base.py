import unittest
from app import app
import json

class MainTesting(unittest.TestCase):

    ''' using daummy data and passing it through the api endpoints or routes '''
    add_product = json.dumps(dict(product_name="Sugar", quantity="5", unit_price="4000", category="necessity"),)
    wrong_fields = json.dumps(dict(product="Sugar", quantity="5", unit_price="4000", category="necessity"),)
    empty_name = json.dumps(dict(product_name="", quantity="5", unit_price="4000", category="necessity"),)
    wrong_name = json.dumps(dict(product_name=" ", quantity="5", unit_price="4000", category="necessity"),)
    empty_price = json.dumps(dict(product_name="Sugar", quantity="5", unit_price="", category="necessity"),)
    wrong_price = json.dumps(dict(product_name="Sugar", quantity="5", unit_price="40iuy00", category="necessity"),)
    empty_quantity = json.dumps(dict(product_name="Sugar", quantity="", unit_price="4000", category="necessity"),)
    wrong_quantity = json.dumps(dict(product_name="Sugar", quantity="c", unit_price="4000", category="necessity"),)
    empty_category = json.dumps(dict(product_name="Sugar", quantity="5", unit_price="4000", category=""),)
    wrong_category= json.dumps(dict(product_name="Sugar", quantity="5", unit_price="4000", category="basi55c"),)

    

    def setUp(self):

        '''initialising the test client'''
        self.app = app.test_client(self)


if __name__ == '__main__':
    unittest.main()