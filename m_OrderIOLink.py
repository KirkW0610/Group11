##Object for retrieving and storing data. Currently implemented to use a .csv file for storage.
##Function names and signatures will likely change over time, but not drastically.
##This applies even when the transition is made to database storage.
from Order import Item
from Order import Order
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import csv

class OrderIO:
    def __init__(self, fn):
        self.filename = fn

    def getNewOrderID(self):
        ##Fetches next historically unused OrderID in the database.
        with open(self.filename, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter="`", quotechar = '|')
            nextnum = -1
            for row in read:
                for i in row:
                    attributes = i.split("`")
                    if(int(attributes[0]) > nextnum):
                        nextnum = int(attributes[0])
            nextnum = nextnum + 1
        return nextnum

    def getOrder(self, oid):
        ##Returns an order of the given ID in the database.
        with open(self.filename, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter="`", quotechar = '|')
            for row in read:
                for i in row:
                    attributes = i.split("`")
                    if (int(attributes[0]) == oid):
                        return self.parseRowItems(i)
            print("Error: No order of id " + str(oid))

    def removeOrder(self, oid):
        ##Removes an order from the database. (Not something we want to be doing)
        ##super often for anything other than testing.)
        desiredsubstring = "|" + str(oid) + "`"
        temp, closeable = mkstemp()
        with fdopen(temp,'w') as newfile:
            with open(self.filename) as oldfile:
                for row in oldfile:
                    if desiredsubstring in row:
                        continue
                    else:
                        newfile.write(row)
        remove(self.filename)
        move(closeable, self.filename)
        return 

    def updateOrder(self, o):
        ##Updates an order. Use getOrder before this, edit that order, then pass
        ##it into this function for proper functionality.
        self.removeOrder(o.orderID)
        self.orderAppend(o)       
                

    def orderAppend(self, o):
        ##Adds an order to the bottom of the database. Only pass orders with
        ##IDs of -1 into this if calling directly. Use updateOrder() for orders
        ##that are already in the list.
        with open(self.filename, 'a', newline='') as csvfile:
            write = csv.writer(csvfile, delimiter = '`', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
            stuffeditems = ""
            if(o.orderID < 0):
                oID = self.getNewOrderID()
            else:
                oID = o.orderID
            
            for i in o.items:
                stuffeditems += '$' + str(i.name) + ';' + str(i.price) + ';' + str(i.qty) + ';' + i.request

            sline = (str(oID) + '`' + str(o.active) + '`' + 
                     str(o.recipient) + '`' + str(o.price) + '`' + str(o.working) + '`' + stuffeditems)
            write.writerow([sline])
            
            return oID

    def orderReadAll(self):
        ##Reads all orders in database. This will not be available once we move
        ##away from File I/O for storage, as we must anticipate truly large
        ##volumes.
        with open(self.filename, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter='`', quotechar = '|')
            orderlist = []
            for row in read:
                for i in row:
                    orderlist.append(self.parseRowItems(i))

            for o in orderlist:
                print(o)

            return orderlist

    def orderReadAllActive(self):
        ##Reads only active orders from database.
        with open(self.filename, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter='`', quotechar = '|')
            orderlist = []
            for row in read:
                for i in row:
                    if i[0] != False:
                        orderlist.append(self.parseRowItems(i))

            for o in orderlist:
                print(o)

            return orderlist

    def parseRowItems(self, rowstring):
        ##Turns a row in the database into an object. This is a helper function.
        ##Use getOrder() for practical purposes.
        foundoid = int(rowstring.split("`")[0])
        oi = Order(rowstring.split("`")[2], foundoid)
        itemstart = rowstring.find('$')
        itemslice = rowstring[itemstart:]
        splits = itemslice.split("$")
        splits.pop(0)
        for i in splits:
            itemattributes = i.split(";")
            item = Item(itemattributes[0], float(itemattributes[1]), int(itemattributes[2]), itemattributes[3])
            oi.addItem(item)
            
        return oi

