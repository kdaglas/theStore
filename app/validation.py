import re


class Validator():

    @classmethod
    def validate_product_inputs(cls, product_name, unit_price, quantity, category):

        ''' method to validate the data of the product from the store owner input '''
        if product_name == '':
            return "Product name is missing"
        elif not re.search(r"^([a-zA-Z\S]+\s)*[a-zA-Z\S]+$", product_name):
            return "Product should be either one or two words and in characters"
        elif unit_price == '':
            return "Price is missing"
        elif not re.search(r"^[0-9]+$", unit_price):
            return "The price should be in numbers"
        elif quantity == '':
            return "Quantity is missing"
        elif not re.search(r"^[0-9]+$", quantity):
            return "Quantity should be in numbers"
        elif category == '':
            return "Category is missing"
        elif not re.search(r"^[a-zA-Z]+$", category):
            return "Category should be in characters"
        else:
            return True
