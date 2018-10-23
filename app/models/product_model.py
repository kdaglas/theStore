''' Object class for the product model '''
class Product():

    def __init__(self):

        ''' contructor to initialise the product list that 
            contains all the attributes of that product '''
        self.the_products = []

    
    def add_product(self, productId, product_name, unit_price, quantity, category):

        ''' the add product method converts the data to a dictionary and then 
            returns that format of the product class '''
        self.productId = productId
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.category = category
        product = {
            'productId' : self.productId,
            'product_name' : self.product_name,
            'unit_price' : self.unit_price,
            'quantity' : self.quantity,
            'category' : self.category
        }
        self.the_products.append(product)
        return product


    def view_all_the_products(self):

        ''' this method returns all the added products in the list '''
        if len(self.the_products) > 0:
            return self.the_products
        return False

    
    def view_one_product(self, productId):

        ''' this method returns one product in the list '''
        if int(productId) > 0:
            if len(self.the_products) > 0:
                for product in self.the_products:
                    if product.get('productId') == int(productId):
                        return product
                return False
            return False
        return False


    def same_product(self, product_name):

        ''' this method returns product in the list by its name'''
        for product in self.the_products:
            if product.get('product_name') == product_name:
                return True
        return False
