# test for sales....

# def test_for_create_a_record_with_wrong_amount(self):

#     '''test for wrong values'''
#     response = self.app.post('/api/v1/sales', data = MainTesting.wrong_amount,
#                             content_type="application/json")
#     reply = json.loads(response.data)
#     self.assertEqual(reply["message"], "The amount paid should have no spaces and be in numbers")
#     self.assertEqual(response.status_code, 400)


# def test_for_create_a_record_with_wrong_quantity(self):

#     '''test for wrong values'''
#     response = self.app.post('/api/v1/sales', data = MainTesting.wrong_sale_quantity,
#                             content_type="application/json")
#     reply = json.loads(response.data)
#     self.assertEqual(reply["message"], "Quantity should have no spaces and be in numbers")
#     self.assertEqual(response.status_code, 400)










# test for products....

# def test_for_adding_product_with_wrong_price(self):

#     '''test for wrong values'''
#     response = self.app.post('/api/v1/products', data = MainTesting.wrong_price,
#                             content_type="application/json")
#     reply = json.loads(response.data)
#     self.assertEqual(reply["message"], "Unit_price should have no spaces, be 3 or more integers and be in numbers")
#     self.assertEqual(response.status_code, 400)


# def test_for_adding_product_with_wrong_quantity(self):

#     '''test for wrong values'''
#     response = self.app.post('/api/v1/products', data = MainTesting.wrong_quantity,
#                             content_type="application/json")
#     reply = json.loads(response.data)
#     self.assertEqual(reply["message"], "Quantity should have no spaces and be in numbers")
#     self.assertEqual(response.status_code, 400)