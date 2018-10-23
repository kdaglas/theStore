import unittest
from tests.test_base import MainTesting
from app import app
import json


class TestingProducts(MainTesting):

    def test_for_wrong_url(self):

        ''' test for wrong url '''
        response = self.app.post('/api/v1/prod', data = MainTesting.add_product,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Please put a valid URL")
        self.assertEqual(response.status_code, 405)


    def test_for_method_not_allowed(self):

        ''' test for method not allowed '''
        response = self.app.post('/api/v1/products/67878', data = MainTesting.add_product,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Method not allowed")
        self.assertEqual(response.status_code, 405)


    def test_for_adding_product_with_invalid_fields(self):

        '''test for invalid fields'''
        response = self.app.post('/api/v1/products', data = MainTesting.wrong_fields,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The key or value fields are invalid or missing, please check")
        self.assertEqual(response.status_code, 403)


    def test_for_adding_product_with_empty_name(self):

        '''test for empty values'''
        response = self.app.post('/api/v1/products', data = MainTesting.empty_name,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Product name is missing")
        self.assertEqual(response.status_code, 400)


    # def test_for_adding_product_with_wrong_name(self):

    #     '''test for wrong values'''
    #     response = self.app.post('/api/v1/products', data = MainTesting.wrong_name,
    #                             content_type="application/json")
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "Product name should be one word with more than 5 characters or two words and be in characters")
    #     self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_empty_price(self):

        '''test for empty values'''
        response = self.app.post('/api/v1/products', data = MainTesting.empty_price,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Unit_price is missing")
        self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_zero_price(self):

        '''test for empty values'''
        response = self.app.post('/api/v1/products', data = MainTesting.zero_price,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Unit_price should be more than 0")
        self.assertEqual(response.status_code, 400)


    # def test_for_adding_product_with_wrong_price(self):

    #     '''test for wrong values'''
    #     response = self.app.post('/api/v1/products', data = MainTesting.wrong_price,
    #                             content_type="application/json")
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "Unit_price should have no spaces, be 3 or more integers and be in numbers")
    #     self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_empty_quantity(self):

        '''test for empty values'''
        response = self.app.post('/api/v1/products', data = MainTesting.empty_quantity,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Quantity is missing")
        self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_zero_quantity(self):

        '''test for zero values'''
        response = self.app.post('/api/v1/products', data = MainTesting.zero_quantity,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Quantity should be more than 0")
        self.assertEqual(response.status_code, 400)


    # def test_for_adding_product_with_wrong_quantity(self):

    #     '''test for wrong values'''
    #     response = self.app.post('/api/v1/products', data = MainTesting.wrong_quantity,
    #                             content_type="application/json")
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "Quantity should have no spaces and be in numbers")
    #     self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_empty_category(self):

        '''test for empty values'''
        response = self.app.post('/api/v1/products', data = MainTesting.empty_category,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Category is missing")
        self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_wrong_category(self):

        '''test for wrong values'''
        response = self.app.post('/api/v1/products', data = MainTesting.wrong_category,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Category should be 5 or more characters and be in characters")
        self.assertEqual(response.status_code, 400)


    def test_add_product(self):

        ''' test for adding a product '''
        response = self.app.post("/api/v1/products", data = MainTesting.add_product, 
                                content_type='application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Product has been added")
        self.assertEqual(response.status_code, 201)


    def test_getting_all_products(self):

        ''' test for getting all products '''
        response = self.app.get("/api/v1/products", content_type='application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "All products viewed")
        self.assertEqual(response.status_code, 200)


    def test_getting_one_product_with_invalid_id(self):

        ''' test for getting one product '''
        response = self.app.get("/api/v1/products/aa", content_type='application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Input should be an integer")
        self.assertEqual(response.status_code, 400)


    def test_getting_one_product_with_wrong_id(self):

        ''' test for getting one product '''
        response = self.app.get("/api/v1/products/034566778899", content_type='application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "No product found with that id")
        self.assertEqual(response.status_code, 404)


    # def test_getting_one_product(self):

    #     ''' test for getting one product '''
    #     response = self.app.get("/api/v1/products/23454", content_type='application/json')
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "One product viewed")
    #     self.assertEqual(response.status_code, 200)
    