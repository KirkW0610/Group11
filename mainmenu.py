# main menu works perfectly
# failed to properly implement mvc

import tkinter as tk
from Inventory import Inventory
from tkinter import font  as tkfont


class View(tk.Tk):
    PAD = 50

    def __init__(self, controller):
        super().__init__()

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.button_font = tkfont.Font(family='Helvetica', size=12, weight="bold")

        self.title("Restaurant App")

        self.controller = controller

        self.value_var = tk.StringVar()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {"StartPage": StartPage(parent=container, controller=self),
                       "Order": Order(parent=container, controller=self),
                       "inventory_view": inventory_view(parent=container, controller=self),
                       "PageThree": PageThree(parent=container, controller=self),
                       "Checkout": Checkout(parent=container, controller=self)}

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["Order"].grid(row=0, column=0, sticky="nsew")
        self.frames["inventory_view"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree"].grid(row=0, column=0, sticky="nsew")
        self.frames["Checkout"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def inv_button_click_1(self, item):
        myInv = Inventory()
        myInv.addItem("chicken", 45)
        myInv.__str__()

    def inv_button_click_2(self, item):
        myInv = Inventory()
        myInv.addItem("carrots", 15)
        myInv.__str__()

    def inv_button_click_3(self, item):
        myInv = Inventory()
        myInv.addItem("pasta", 22)
        myInv.__str__()

    def main(self):
        self.mainloop()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black", bd=220)
        self.controller = controller
        label = tk.Label(self, text="Main Menu", fg='#FFFFFF', bg="black", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Order", padx=33, pady=10, font=controller.button_font, bg='#FFA500',
                            command=lambda: controller.show_frame("Order"))
        button2 = tk.Button(self, text="Inventory", padx=20, pady=10, font=controller.button_font, bg='#FFA500',
                            command=lambda: controller.show_frame("inventory_view"))
        button3 = tk.Button(self, text="Overview", padx=20, pady=10, font=controller.button_font, bg='#FFA500',
                            command=lambda: controller.show_frame("PageThree"))
        button4 = tk.Button(self, text="Checkout", padx=20, pady=10, font=controller.button_font, bg='#FFA500',
                            command=lambda: controller.show_frame("Checkout"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


class Order(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black", bd=220)
        self.controller = controller
        label = tk.Label(self, text="Order", fg='#FFFFFF', bg="black", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button_3 = tk.Button(self, text="Go back to Main Menu", padx=20, pady=10, font=controller.button_font,
                             command=lambda: controller.show_frame("StartPage"))
        button_3.pack()


class inventory_view(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__()
        tk.Frame.__init__(self, parent, bg="black", bd=220)
        self.controller = controller
        label = tk.Label(self, text="Inventory", fg='#FFFFFF', bg="black", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        btn_1 = tk.Button(
            self, bg='#FFA500',
            fg='#FFFFFF', text='Add Chicken', padx=20, pady=10, font=controller.button_font, command=(
                lambda button='Add Chicken': self.controller.inv_button_click_1(button)
            )
        )

        btn_2 = tk.Button(
            self, bg='#FFA500',
            fg='#FFFFFF', text='Add Carrots', padx=20, pady=10, font=controller.button_font, command=(
                lambda button='Add Carrots': self.controller.inv_button_click_2(button)
            )
        )

        btn_3 = tk.Button(
            self, text="Go back to Main Menu", padx=20, pady=10, font=controller.button_font,
            command=lambda: controller.show_frame("StartPage")
        )

        btn_1.pack()
        btn_2.pack()
        btn_3.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black", bd=220)
        self.controller = controller
        label = tk.Label(self, text="Overview", fg='#FFFFFF', bg="black", font=controller.title_font)
        label.pack(side="top", fill="x")
        button_3 = tk.Button(self, text="Go back to Main Menu", padx=20, pady=10, font=controller.button_font,
                             command=lambda: controller.show_frame("StartPage"))
        button_3.pack()


class Checkout(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black", bd=220)
        self.controller = controller
        label = tk.Label(self, text="Checkout", fg='#FFFFFF', bg="black", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button_3 = tk.Button(self, text="Go back to Main Menu", padx=20, pady=10, font=controller.button_font,
                             command=lambda: controller.show_frame("StartPage"))
        button_3.pack()
