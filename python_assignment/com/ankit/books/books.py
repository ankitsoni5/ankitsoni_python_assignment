class Book:
    bdata=[]
    def __init__(self,bid=None,title=None,pages=0,price=0.0):
        self.bid=bid
        self.title=title
        self.pages=pages
        self.price=price
   
    def get_details(self):
        return 'Book Id: {bid}\nBook Name: {title}\nBook Pages: {pages}\nBook Price: {price}'.format(bid=self.bid,title=self.title,pages=self.pages,price=self.price)
    
    def add_data(self):
        Book.bdata.append(self)
         
    def get_data(self):
        return Book.bdata
    
    def remove_data(self):
        Book.bdata.remove(self)