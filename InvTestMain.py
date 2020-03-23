from Inventory import Inventory

myInv = Inventory()
myInv.addItem("chicken",45)
myInv.addItem("carrots",15)
myInv.addItem("pasta",18)

myInv.currQuantity("chicken")

myInv.__str__()