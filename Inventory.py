#Used to create an Inventory Item Object
#Not that necessary (except for the toString) in this case, but could be useful depending on how we decide to impliment
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

#Manages inventory using dictionary
#Also saves inventory to a text file in place of using a database, since we don't currently have that implimented
class Inventory:
    def __init__(self):
        #Reads/creates a text file to save the inventory to
        self.currInv = open("Inventory.txt","w+")
        self.currInvList = {}
        tempList = self.currInv.read.split()
        #Puts the inventory into a dictionary
        for i in range(len(tempList)):
            self.currInvList[tempList[i]] = tempList[i+1]
            i += 1

    #Adds items/quanities to the dictionary and also to the text file
    def addItem(self,name,quanity):
        newItem = InvItem(name,quanity)
        self.currInv.write(newItem.__str__())
        self.currInvList[name] = quanity

    #Prints the quantity of a specific item
    def currQuantity(self,name):
        print(name+"\t"+self.currInvList[name])

    #Prints whole inventory
    def printInv(self):
        i = 1 
        for x in self.currInvList:
            print(i+"."+" "+x+"\t"+self.currInvList[x])
            i += 1
