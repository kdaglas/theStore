''' Object class for the sale record model '''
class SaleRecord():

    def __init__(self):

        ''' contructor to initialise the sale record list that 
            contains all the attributes of that sale '''
        self.the_records = []
    

    def create_record(self, recordId, product_name, quantity, pay_amount, attendant, today):

        ''' the create record method converts the data to a dictionary and then 
            returns that format of the record class '''
        record = {
            'recordId' : recordId,
            'product_name' : product_name,
            'quantity': quantity,
            'pay_amount': pay_amount,
            'attendant' : attendant,
            'today' : today
        }
        self.the_records.append(record)
        return record


    def fetch_all_the_sales(self):

        ''' this method returns all the created sale records in the list '''
        if len(self.the_records) > 0:
            return self.the_records
        return False
