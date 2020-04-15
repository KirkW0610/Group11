from Inventory import Inventory
from mainmenu import View


class Controller:
    def __init__(self):
        self.Inventory = Inventory()
        self.view = View(self)

    def main(self):
        self.view.main()


if __name__ == '__main__':
    tester = Controller()
    tester.main()
