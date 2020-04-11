class InvItem:
    def __init__(self,n,q,i = -1):
        self.name = n
        self.quantity = q
        self.id = i  ##Let the backend handle this field.

    def getName(self):
        return self.name
    
    def getQuantity(self):
        return self.quantity

    def getID(self):
        return self.id
    
    def __str__(self):
        string = str(self.name)+str(self.quantity)+"\n"
        return string
