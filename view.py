import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    PAD = 50
    buttons = [
        'Add Chicken',
        'Add Carrots',
        'Add Pasta',
        'Check chicken quantity'
    ]

    def __init__(self, controller):
        super().__init__()

        self.title("Inv GUI test")

        self.controller = controller

        self.value_var = tk.StringVar()

        self._make_main_frame()

        self._make_buttons()

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()

        frm = ttk.Frame(outer_frm)
        frm.pack()

        for item in self.buttons:
            frm = ttk.Frame(outer_frm)
            frm.pack()

            btn = ttk.Button(
                frm, text=item, command=(
                    lambda button=item: self.controller.on_button_click(button)
                )
            )

            btn.pack()

