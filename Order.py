class Item:
    def __init__(self, n, p, q, sreq = "NSR"):
        self.name = n
        self.price = p
        self.qty = q
        self.request = sreq

class Order:
    def __init__(self, rec, oID = -1):
        self.orderID = oID
        self.recipient = rec
        self.price = 0
        self.items = []
        self.working = False
        self.active = True

    def __str__(self):
        items = ""
        for i in self.items:
            items += ("\t" + "Item: " + i.name + "\n" +
                     "\t" + "Price: " + str(i.price) + "\n" +
                     "\t" + "Quantity: " + str(i.qty) + "\n" +
                     "\t" + "Special Requests: " + i.request + "\n" +
                     "\t" + "+++++++++++" + "\n")
                     
        out = ("Order ID: " + str(self.orderID) + "\n" +
              "Recipient: " + str(self.recipient) + "\n" +
              "Price: " + str(self.price) + "\n" +
              "Working: " + str(self.working) + "\n" +
              "Active: " +str(self.active) + "\n" +
              "Items: " + "{\n" + items + "}\n")

        return out

    def addItem(self, i):
        self.items.append(i)
        self.price += i.price * i.qty

    def removeItem(self, i):
        self.items.remove(i)
        self.price -= i.price * i.qty

    def getItemIndex(self, i):
        return self.items.index(i)

    def getItem(self, ind):
        return self.items[ind]

    def updateItem(self, i, ind):
        self.items[ind] = i

    def setWorking(self, b):
        self.working = b

    def setActive(self, b):
        self.active = b

    def orderOut(self, ):
        print("ORDER FOR " + str(self.recipient) + ": ")
        for i in self.items:
            print(i.name + ": $%.2f" % (i.price * i.qty), end=" ")
            if(len(i.request)) != 0:
                print("Special Requests: " + i.request)
            else:
                print()
        print("TOTAL = $%.2f" % self.price)
