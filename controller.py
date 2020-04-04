from Inventory import Inventory
from view import View


class Controller:
    def __init__(self):
        self.Inventory = Inventory()
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_button_click(self, item):
        myInv = Inventory()
        if item == 'Add Chicken':
            myInv.addItem("chicken", 45)
            myInv.__str__()
        elif item == 'Add Carrots':
            myInv.addItem("carrots", 15)
            myInv.__str__()
        elif item == 'Add Pasta':
            myInv.addItem("pasta", 22)
            myInv.__str__()
        # elif btn_1 == 'Check chicken quantity':
        # myInv.currQuantity("chicken")


if __name__ == '__main__':
    tester = Controller()
    tester.main()
