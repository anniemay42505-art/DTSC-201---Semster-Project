import tkinter as tk
from tkinter import ttk
from data_loader import df

Desc_Message = ("Welcome to Annie Martz's and Thomas White's Semester Project,"
                " A Muliciple Building Data Viewer for Buildings in Allegany County.")

available_locations = sorted(
    df["location"].dropna().unique()
)

class Application:
    def __init__(self, root):
        self.root = root
        root.title("DTSC 201 Semester Project")
        root.geometry("800x600")

        self.optionmenu1_var = tk.StringVar()
        self.optionmenu1_var.set("Building 1")

        self.optionmenu1 = tk.OptionMenu(root, self.optionmenu1_var, "Option 1", "Option 2", "Option 3")
        self.optionmenu1.place(x=500, y=286, width=150, height=28)

        self.Desc_Message = tk.Text(root)
        self.Desc_Message.place(x=10, y=20, width=780, height=90)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
