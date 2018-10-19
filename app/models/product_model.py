''' Object class for the product model '''
class Product():

    def __init__(self):

        ''' contructor to initialise the product list that 
            contains all the attributes of that product '''
        self.all_products = []
    
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
        self.all_products.append(product)
        return product

    def view_all_products(self):

        ''' this method returns all the added products in the list '''
        if len(self.all_products) > 0:
            return [product for product in self.all_products]
        return 'No products found'
