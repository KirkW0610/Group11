##Object for retrieving and storing data. Connects to a (currently local) mySQL database.
##Function names and signatures should be final.
##Instantiate one of these objects to connect to a database, then use the functions within
##To modify the data stored in the database.
##WARNING: USE .CLOSE() ON THIS OBJECT BEFORE THE PROGRAM CLOSES OR YOU INSTANTIATE ANOTHER
##SIMILAR OBJECT
from Order import Item
from Order import Order
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import csv
import mysql.connector

class OrderIOLink:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='program',
                                          password = 'WR7RovyDbtLEpuvBPhVi',
                                          host = '127.0.0.1',
                                          database = 'ordersystem')

            self.cursor = self.cnx.cursor(buffered=True)

        except:
            print("An error has occured in the OrderIOLink connection process.")
            self.cursor.close()
            self.cnx.close()

    def close(self):
        self.cursor.close()
        self.cnx.close()

    def getOrder(self, oid):

        ##Construct Empty Order
        querystep = "SELECT * from orderlist WHERE orderid = " + str(oid)

        self.cursor.execute(querystep)

        response = self.cursor.fetchall()

        r = response[0]

        orderout = Order(r[1], r[0])

        if(r[2] == 0):
            orderout.setActive(False)
            
        if(r[3] == 1):
            orderout.setWorking(True)

        ##Construct Item Set
        querystep = "SELECT * from itemslist WHERE OwnerOrder = " + str(oid)

        self.cursor.execute(querystep)

        response = self.cursor.fetchall()

        for r in response:
            ri = Item(r[1], r[3], r[2], r[4])
            orderout.addItem(ri)
            
        return orderout

    def addOrder(self, o):
        ##Adds order to database, and then passes back its orderID.
        ##Use this with newly created orders that have not been comitted yet.

        querystep = ("INSERT INTO orderlist (recipient, active, working) VALUES " +
                    "(%s, %s, %s)")

        

        data = (o.recipient, o.active, o.working)

        self.cursor.execute(querystep, data)
        freshid = self.cursor.lastrowid

        for i in o.items:
            querystep = ("INSERT INTO itemslist VALUES (%s, %s, %s, %s, %s)")
            data = (str(freshid), i.name, str(i.qty), str(i.price), i.request)

            self.cursor.execute(querystep, data)

        self.cnx.commit()

    def removeOrder(self, oid):
        
        ##Remove Order From Database. Not something we want to be doing a whole lot.
        ##Consider Setting the "active" status of an order to "False" instead,
        ##so data can be preserved for later analysis. Order "Age of Death" will be
        ##implemented later.

        ##Start by deleting all "children" items of the order.
        querystep = "DELETE FROM itemslist WHERE OwnerOrder = " + str(oid)
        
        self.cursor.execute(querystep)

        querystep = "DELETE FROM orderlist WHERE orderid = " + str(oid)

        self.cursor.execute(querystep)

        self.cnx.commit()

    def updateOrder(self, o):
        ##UPDATES an order already in the orderlist with information from the order
        ##passed in. Use getOrder to construct the order first, then modify that
        ##object to pass in here.

        querystep = ("UPDATE orderlist SET recipient = %s, active = %s, working = %s" +
                     " WHERE orderid = %s")

        data = (o.recipient, o.active, o.working, o.orderID)

        self.cursor.execute(querystep, data)

        querystep = "DELETE FROM itemslist WHERE OwnerOrder = " + str(o.orderID)

        self.cursor.execute(querystep)

        for i in o.items:
            querystep = ("INSERT INTO itemslist VALUES (%s, %s, %s, %s, %s)")
            
            data = (o.orderID, i.name, str(i.qty), str(i.price), i.request)

            self.cursor.execute(querystep, data)

        self.cnx.commit()
    

###################################################
try:
    link = OrderIOLink()
    o1 = link.getOrder(18)
    o1.recipient = "Craig"
    i1 = Item("hamburger", 1.55, 33, "all mustard")
    o1.items[0] = i1
    link.updateOrder(o1)
    print(link.getOrder(18))
finally:
    link.close()
