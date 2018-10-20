import unittest
from tests.test_base import MainTesting
from app import app
import json


class TestingSales(MainTesting):

    def test_for_wrong_url(self):

        ''' test for wrong url '''
        response = self.app.post('/api/v1/sal', data = MainTesting.create_sale,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Please put a valid URL")
        self.assertEqual(response.status_code, 405)


    # def test_for_method_not_allowed(self):

    #     ''' test for method not allowed '''
    #     response = self.app.post('/api/v1/sales/67878', data = MainTesting.create_sale,
    #                             content_type="application/json")
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "Method not allowed")
    #     self.assertEqual(response.status_code, 405)


    def test_for_adding_product_with_invalid_fields(self):

        '''test for invalid fields'''
        response = self.app.post('/api/v1/sales', data = MainTesting.wrong_sale_fields,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The key or value fields are invalid or missing, please check")
        self.assertEqual(response.status_code, 403)


    def test_for_adding_product_with_empty_product_name(self):

        '''test for empty values'''
        response = self.app.post('/api/v1/sales', data = MainTesting.empty_product_name,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Product name is missing")
        self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_wrong_product_name(self):

        '''test for wrong values'''
        response = self.app.post('/api/v1/sales', data = MainTesting.wrong_product_name,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Product should be either one word with more than 5 characters or two words and in characters")
        self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_empty_amount(self):

        '''test for empty values'''
        response = self.app.post('/api/v1/sales', data = MainTesting.empty_amount,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The amount paid is missing")
        self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_zero_amount(self):

        '''test for empty values'''
        response = self.app.post('/api/v1/sales', data = MainTesting.zero_amount,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The amount paid should be more than 0")
        self.assertEqual(response.status_code, 400)


    # def test_for_adding_product_with_wrong_amount(self):

    #     '''test for wrong values'''
    #     response = self.app.post('/api/v1/sales', data = MainTesting.wrong_amount,
    #                             content_type="application/json")
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "The amount paid should have no spaces and be in numbers")
    #     self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_empty_quantity(self):

        '''test for empty values'''
        response = self.app.post('/api/v1/sales', data = MainTesting.empty_sale_quantity,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Quantity is missing")
        self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_zero_quantity(self):

        '''test for zero values'''
        response = self.app.post('/api/v1/sales', data = MainTesting.zero_sale_quantity,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Quantity should be more than 0")
        self.assertEqual(response.status_code, 400)


    # def test_for_adding_product_with_wrong_quantity(self):

    #     '''test for wrong values'''
    #     response = self.app.post('/api/v1/sales', data = MainTesting.wrong_sale_quantity,
    #                             content_type="application/json")
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "Quantity should have no spaces and be in numbers")
    #     self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_empty_attendant(self):

        '''test for empty values'''
        response = self.app.post('/api/v1/sales', data = MainTesting.empty_attendant,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Attendant name is missing")
        self.assertEqual(response.status_code, 400)


    def test_for_adding_product_with_wrong_attendant(self):

        '''test for wrong values'''
        response = self.app.post('/api/v1/sales', data = MainTesting.wrong_attendant,
                                content_type="application/json")
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Attendant name should be more than 3 characters and be in characters")
        self.assertEqual(response.status_code, 400)


    def test_create_sale_record(self):

        ''' test for creating a sale record '''
        response = self.app.post("/api/v1/sales", data = MainTesting.create_sale, 
                                content_type='application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Sale record has been created")
        self.assertEqual(response.status_code, 201)


    # def test_getting_all_sale_records(self):

    #     ''' test for getting all sales records '''
    #     response = self.app.get("/api/v1/sales", content_type='application/json')
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "All sale records viewed")
    #     self.assertEqual(response.status_code, 200)


    # def test_getting_one_product_with_invalid_id(self):

    #     ''' test for getting one product '''
    #     response = self.app.get("/api/v1/sales/aa", content_type='application/json')
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "Input should be an interger")
    #     self.assertEqual(response.status_code, 400)


    # def test_getting_one_product_with_wrong_id(self):

    #     ''' test for getting one product '''
    #     response = self.app.get("/api/v1/sales/034566778899", content_type='application/json')
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "No product found with that id")
    #     self.assertEqual(response.status_code, 404)


    # def test_getting_one_product(self):

    #     ''' test for getting one product '''
    #     response = self.app.get("/api/v1/sales/23454", content_type='application/json')
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "One product viewed")
    #     self.assertEqual(response.status_code, 200)
    