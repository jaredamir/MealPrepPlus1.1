import csv
import pyinputplus as pyip
import tkinter as tk

"""
class Meal:
    def __init__(self, name):
        self.name = name

    def newmeal(self):
        meal_list = []
        ingredient_file = []
        with open("Ingredients.csv", "r") as file:
            read = csv.reader(file)
            for row in read:
                ingredient_file.append(row)

    def search(self):
        meal_file = []
        flag=0
        with open("Meallist.csv", "r") as file:
            read = csv.reader(file)
            for row in read:
                meal_file.append(row)
        for i in range(len(meal_file)):
            if self.name== meal_file[i][0][0]:
                print(meal_file[i][0][0])
                flag+=1
        if flag==0: print("Meal Not Found ")


#Menu
def new():
    name = input("Meal Name\n")
    cl_meal = Meal(name)
    cl_meal.newmeal()

def open_meal():
    name = input("Meal Name\n")
    cl_meal = Meal(name)
    cl_meal.search()

open_meal()
"""
test_meal = [["boom  boom chicken", 0, 0, 0, 0, 0],
             [["ham", 3.0, "grams", 70.0, 15.0, 10.0, 10.0, 9.0], ["ham", 3.0, "grams", 70.0, 15.0, 10.0, 10.0, 9.0]]]


class RecipeMeal:
    intial_cal = 0
    intial_pro = 0
    intial_carb = 0
    intial_fats = 0
    intial_sugar = 0

    def __init__(self, meal):

        self.meal = meal
        self.meal_info = meal[0]
        self.ings = meal[1]

        for i in range(len(self.ings)):
            intial_cal += float(self.ings[i][3])
            intial_pro += float(self.ings[i][4])
            intial_carb += float(self.ings[i][5])
            intial_fats += float(self.ings[i][6])
            intial_sugar += float(self.ings[i][7])

        self.cal = intial_cal
        self.pro = intial_pro
        self.carb = intial_carb
        self.fats = intial_fats
        self.sugar = intial_sugar


tx = RecipeMeal(test_meal)
print(tx.meal)