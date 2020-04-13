# THIS PROGRAM IS INCOMPLETE
# FEEL FREE TO FIX IT
# RUNS JUST LIKE VIEW.PY WITH CONTROLLER.PY




# use dropdown menu


import tkinter as tk
from tkinter import font  as tkfont
from tkinter import ttk


class View(tk.Tk):
    PAD = 50

    def __init__(self, controller):
        super().__init__()

        self.title("Inv GUI test")

        self.controller = controller

        self.value_var = tk.StringVar()

        # self._make_main_frame()

        # self._make_buttons()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {"StartPage": StartPage(parent=container, controller=self),
                       "PageOne": PageOne(parent=container, controller=self),
                       "PageTwo": PageTwo(parent=container, controller=self),
                       "PageThree": PageThree(parent=container, controller=self),
                       "PageFour": PageFour(parent=container, controller=self)}

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageFour"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def main(self):
        self.mainloop()


'''def _make_main_frame(self):
        self.main_frm = tk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_buttons(self):
        frm = tk.Frame(self.main_frm)
        frm.pack()

        btn_1 = tk.Button(
            frm, bg='#FFA500',
            fg='#FFFFFF', text='Add Chicken', command=(
                lambda button='Add Chicken': self.controller.inv_button_click_1(button)
            )
        )

        btn_2 = tk.Button(
            frm, bg='#FFA500',
            fg='#FFFFFF', text='Add Carrots', command=(
                lambda button='Add Carrots': self.controller.inv_button_click_2(button)
            )
        )

        btn_1.pack()
        btn_2.pack()'''


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Main Menu")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Order",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Inventory",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Overview",
                            command=lambda: controller.show_frame("PageThree"))
        button4 = tk.Button(self, text="Checkout",
                            command=lambda: controller.show_frame("PageFour"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Order")
        label.pack(side="top", fill="x", pady=10)
        button_3 = tk.Button(self, text="Go back to Main Menu",
                             command=lambda: controller.show_frame("StartPage"))
        button_3.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Inventory")
        label.pack(side="top", fill="x", pady=10)

        btn_1 = tk.Button(
            self, bg='#FFA500',
            fg='#FFFFFF', text='Add Chicken', command=(
                lambda button='Add Chicken': self.controller.inv_button_click_1(button)
            )
        )

        btn_2 = tk.Button(
            self, bg='#FFA500',
            fg='#FFFFFF', text='Add Carrots', command=(
                lambda button='Add Carrots': self.controller.inv_button_click_2(button)
            )
        )

        btn_3 = tk.Button(
            self, text="Go back to Main Menu",
            command=lambda: controller.show_frame("StartPage")
        )

        btn_1.pack()
        btn_2.pack()
        btn_3.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Overview")
        label.pack(side="top", fill="x", pady=10)
        button_3 = tk.Button(self, text="Go back to Main Menu",
                             command=lambda: controller.show_frame("StartPage"))
        button_3.pack()


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Checkout")
        label.pack(side="top", fill="x", pady=10)
        button_3 = tk.Button(self, text="Go back to Main Menu",
                             command=lambda: controller.show_frame("StartPage"))
        button_3.pack()
