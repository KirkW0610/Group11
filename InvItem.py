class InvItem:
    def __init__(self,n,q):
        self.name = n
        self.quanity = q

    def getName(self):
        return self.name
    
    def getQuanity(self):
        return self.quanity
    
    def __str__(self):
        str = +self.name+self.quanity+"\n"
        return str