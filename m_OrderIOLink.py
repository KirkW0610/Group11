##Object for retrieving and storing data. Connects to a mySQL database.
##Function names and signatures are final.
##Instantiate one of these objects to connect to a database, then use the functions within
##To modify the data stored in the database.
##WARNING: USE .CLOSE() ON THIS OBJECT BEFORE THE PROGRAM CLOSES OR YOU INSTANTIATE ANOTHER
##SIMILAR OBJECT
from Order import Item
from Order import Order
from InvItem import InvItem
import mysql.connector

class OrderIOLink:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='program',
                    password = 'WR7RovyDbtLEpuvBPhVi',
                    host = 'ordersysteminstance.cfas0wvwh98j.us-east-2.rds.amazonaws.com',
                    database = 'ordersystem')
            
            self.cursor = self.cnx.cursor(buffered=True)

        except:
            print("An error has occured in the OrderIOLink connection process.")
            self.cursor.close()
            self.cnx.close()
            return

    def close(self):
        self.cursor.close()
        self.cnx.close()

    def getOrder(self, oid):

        ##Construct Empty Order
        querystep = "SELECT * from orderlist WHERE orderid = " + str(oid)

        self.cursor.execute(querystep)

        response = self.cursor.fetchall()

        r = response[0]

        if(len(response) == 0):
            print("No orders by that ID.")
            return

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

    def getAllActiveOrders(self):
        ##returns a list of all active orders.

        output = []

        querystep = "SELECT orderid from orderlist WHERE active = 1"

        self.cursor.execute(querystep)

        response = self.cursor.fetchall()

        for r in response:
            output.append(self.getOrder(r[0]))

        return output
        
    def checkWork(self, o):
        ##Checks if the order has working set to True. Helper function to make sure
        ##No orders get updated while kitchenside is working on them.

        querystep = "SELECT working FROM orderlist WHERE orderid = " + str(o.orderID)

        self.cursor.execute(querystep)

        response = self.cursor.fetchall()

        r = response[0]

        if(r[0] == 0):
            return False

        else:
            return True

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
        ##object to pass in here. Restricted to use while order is not being worked.

        if(self.checkWork(o) == True):
            print("Order is already being worked on, and cannot be updated any longer.")
            return
        

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

    def updateOrderWorkingState(self, o):
        ##Allows a user to update an order's working state. This is for use in the
        ##kitchen, and to rectify possible errors in marking an order.

        if(o.working == True):
            v = 1

        else:
            v = 0

        querystep = ("UPDATE orderlist SET working = %s WHERE orderid = %s")

        data = (v, o.orderID)

        self.cursor.execute(querystep, data)

        self.cnx.commit()

    def getInvItem(self, name):
        ##retrieves an InvItem object by name.
        
        querystep = ("SELECT * from inventory WHERE iname = %s")

        data = (name, )

        self.cursor.execute(querystep, data)

        response = self.cursor.fetchall()

        if(len(response) == 0):
            print("No results by that name.")
            return

        r = response[0]

        ri = InvItem(r[1], r[2], r[0]);

        return ri;


    def addInvItem(self, inv):
        ##Add an item to the inventory. NOTE:: pass in an InvItem object!
        querystep = ("INSERT INTO inventory (iname, quantity) VALUES (%s, %s)")

        data = (inv.getName(), inv.getQuantity())
        try:
            self.cursor.execute(querystep, data)

        except mysql.connector.IntegrityError as err:
            return "Already Exists!"

        self.cnx.commit()

    def removeInvItem(self, inv):
        ##Remove an item from the inventory. NOTE:: pass in an InvItem object!

        querystep = ("DELETE FROM inventory WHERE iname = %s")

        data = (inv.getName(), )

        self.cursor.execute(querystep, data)
    
        self.cnx.commit()

    def updateInvItem(self, inv):
        ##Update any inventory item. All fields can be changed except for the ID, which is
        ##used to identify the item in the database.

        querystep = ("UPDATE inventory SET iname = %s, quantity = %s WHERE idinventory = %s")

        data = (inv.getName(), inv.getQuantity(), inv.getID())

        self.cursor.execute(querystep, data)

        self.cnx.commit()
        
###################################################
try:
    link = OrderIOLink()
    o1 = Order("Daniel")
    i1 = Item("Hot Dog", 1.20, 2, "No mustard.")
    i2 = Item("Soda", .75, 1)
    o1.addItem(i1)
    o1.addItem(i2)
    link.addOrder(o1)
    o1 = link.getAllActiveOrders()
    for o in o1:
        print(o)
finally:
    link.close()
