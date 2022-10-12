#Section for admin to add and delete meals
import csv
import pyinputplus as pyip
import pickle
from tkinter import *
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import sv_ttk
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image


#tkinter variables



#TK Classes
"""
class MainPageTest:
    def __init__(self, master):
        mainframe = ttk.Frame(master=master, bg="blue")

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
        lis = tk.Listbox()
        #tree view
        tree = ttk.Treeview(master=mainframe, height=10)
        tree.insert('', tk.END, values=("test1", "test2", "test3"))

        tree.pack()
        #in  tree, make each item clickable to enter edit/delete

        quit = ttk.Button(master=mainframe, text="quit", command=self.quitting, width=20)
        quit.pack()
    def quitting(self):
        root.quit()
"""

class UserPage:
    def __init__(self):
        self.name = "hello"
        #netflix style

class NewPlanPage:

    def __init__(self, master):
        img = Image.open("My project.png")
        #ImageTk.PhotoImage(file="RedefineLogo.jpeg")
        resized=img.resize((100,100), Image.ANTIALIAS)
        logo_pic = ImageTk.PhotoImage(resized)

        #img.resize((50,50))

        #Frames
        self.mainframe = tk.Frame(master=master, width=100, height=1000)
        left_frame = tk.Frame(master=self.mainframe)
        right_frame = tk.Frame(master=self.mainframe, height=200) #highlightbackground="black", highlightthickness=2)
        right_frame.pack_propagate(0)
        right_frame.rowconfigure(2,weight=1)
        right_frame.columnconfigure(4,weight=1)
        right_search_frame = tk.Frame(master=self.mainframe)


        #Widgets
        header=tk.Button(master=self.mainframe, image=logo_pic)
        plan_name = ttk.Label(master=self.mainframe, text="Plan Name")
        plan_name_entry = ttk.Entry(master=self.mainframe)
        search_bar = ttk.Entry(master=right_search_frame, width=62)

        cal_label = ttk.Button(master=right_frame, width=10, text="Calories")
        pro_label = ttk.Button(master=right_frame, width=10, text="Protein")
        carb_label = ttk.Button(master=right_frame, width=10, text="Carbs")
        fats_label = ttk.Button(master=right_frame, width=10, text="Fats")
        sugar_label = ttk.Button(master=right_frame, width=10, text="Sugar")

        cal_num = ttk.Label(master=right_frame, text="0")
        pro_num  = ttk.Label(master=right_frame, text="0")
        carb_num  = ttk.Label(master=right_frame, text="0")
        fats_num  = ttk.Label(master=right_frame, text="0")
        sugar_num  = ttk.Label(master=right_frame, text="0")

        #search_tree
        search_tree = ttk.Treeview(master=right_search_frame)
        search_tree.column("#0", width=400)
        search_tree.heading("#0", text="Search", anchor=CENTER)

        #Meal Tree
        tree=ttk.Treeview(master=left_frame, height=10)
        #tree["column"]=("ReDefine Meals")
        tree.column("#0", width=400)
        #tree.column("ReDefine Meals", anchor=CENTER, width=120)

        tree.heading("#0", text="ReDefine Meals", anchor=CENTER)
        #tree.heading("ReDefine Meals", text="Redefine Meals", anchor=W)


        tree.insert(parent="", index="end", iid=0, text="Smores Overnight Oats")





        #Pack
        self.mainframe.pack(fill=BOTH, expand=1)
        header.pack(pady=20)
        plan_name.pack()
        plan_name_entry.pack()
        left_frame.pack(side="left")

        right_search_frame.pack(padx=40, pady=40)
        search_bar.pack()
        search_tree.pack()

        right_frame.pack(padx=40)
        cal_label.grid(column=0, row=1, sticky="n", padx=5, pady= 10)
        pro_label.grid(column=1, row=1, sticky="n", padx=5, pady= 10)
        carb_label.grid(column=2, row=1, sticky="n", padx=5, pady= 10)
        fats_label.grid(column=3, row=1, sticky="n", padx=5, pady= 10)
        sugar_label.grid(column=4, row=1, sticky="n", padx=5, pady= 10)
        cal_num.grid(column=0, row=2, sticky="n", padx=5)
        pro_num.grid(column=1, row=2, sticky="n", padx=5)
        carb_num.grid(column=2, row=2, sticky="n", padx=5)
        fats_num.grid(column=3, row=2, sticky="n", padx=5)
        sugar_num.grid(column=4, row=2, sticky="n", padx=5)

        tree.pack(padx=40)

    #def item_selected(event):
        #selected_indices = left_list.curselection()





#root=ThemedTk(theme='aqua')

#equilux yaru radience breeze aqua
#print(root.get_themes())

#Styling
root=tk.Tk()
root.title("Meal Prep Plus")
sv_ttk.set_theme("light")  # Set light theme  # Set dark theme

sv_ttk.use_light_theme()  # Set light theme  # Set dark theme
  # Toggle between dark and light theme

#https://github.com/rdbende/Sun-Valley-ttk-theme


root.geometry("1100x700")
root.minsize(width=700, height=500)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=3)
#style = ttk.Style(root)
#style.theme_use('aqua')

NewPlanPage(root)

root.mainloop()


#ideas:
    #MatPLot animation, bar going over/ under for each macro (canvaas)
    #loading animation
    #maybe clickable circles for each plan (hollow thin circle with name in middle (hover over ani, bigger)
    #either grow and change colors, or draw outline
    #clicking on a meall replacaes text box with meal info
    #leaaf asa icon
