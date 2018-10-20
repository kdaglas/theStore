''' Object class for the sale record model '''
class SaleRecord():

    def __init__(self):

        ''' contructor to initialise the sale record list that 
            contains all the attributes of that sale '''
        self.the_records = []
    

    def create_record(self, recordId, product_name, quantity, pay_amount, attendant, today):

        ''' the create record method converts the data to a dictionary and then 
            returns that format of the record class '''
        self.recordId = recordId
        self.product_name = product_name
        self.quantity = quantity
        self.pay_amount = pay_amount
        self.attendant = attendant
        self.today = today
        record = {
            'recordId' : self.recordId,
            'product_name' : self.product_name,
            'quantity': self.quantity,
            'pay_amount': self.pay_amount,
            'attendant' : self.attendant,
            'today' : self.today
        }
        self.the_records.append(record)
        return record
