import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import sv_ttk

import pyinputplus as pyip
import pickle
import csv

class MainPageTest:
    def __init__(self, master):
        mainframe = ttk.Frame(master=master)
        mainframe.pack()
        lab=ttk.Label(master=mainframe, text="Testing")
        lab.pack()
        ent= ttk.Entry(master=mainframe)
        ent.pack()
        rad = ttk.Radiobutton(master=mainframe, text="Testing")
        rad.pack()
        check = ttk.Checkbutton(master=mainframe, text="Testing2")
        check.pack()
        ttk.Spinbox()

        quit = ttk.Button(master=mainframe, text="quit", command=self.quitting, width=20)
        quit.pack()


        #tree view
        tree = ttk.Treeview(master=mainframe, height=10)
        tree.insert('', tk.END, values=("test1", "test2", "test3"))

        tree.pack()
        #in  tree, make each item clickable to enter edit/delete
        scroll = ttk.Scrollbar(master=mainframe, orient="vertical")
        scroll.pack()

    def quitting(self):
        root.quit()


class NewMealPage:
    def __init__(self, master):
        pass



#root=ThemedTk(theme='aqua')

#equilux yaru radience breeze aqua
#print(root.get_themes())

#Styling
root=tk.Tk()
root.title("Meal Prep Plus")
sv_ttk.set_theme("")  # Set light theme  # Set dark theme

sv_ttk.use_light_theme()  # Set light theme  # Set dark theme
  # Toggle between dark and light theme

#https://github.com/rdbende/Sun-Valley-ttk-theme
print(sv_ttk.get_theme())

root.geometry("1100x700")
root.minsize(width=700, height=500)
#style = ttk.Style(root)
#style.theme_use('aqua')

MainPageTest(root)

root.mainloop()


#ideas:
    #MatPLot animation, bar going over/ under for each macro (canvaas)
    #loading animation
    #maybe clickable circles for each plan (hollow thin circle with name in middle (hover over ani, bigger)
    #either grow and change colors, or draw outline

