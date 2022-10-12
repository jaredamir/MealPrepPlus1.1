import csv
import pyinputplus as pyip
# welcome: make new meal plan, read previous one[edit a meal, search for a meal]
# need to add a sub section for ingridents in meal
# need to add a section for goals

#VARIABLES
sum_calories = 0
sum_protein = 0
sum_carbs = 0
sum_fats = 0
meallist=[]
todaylist=[]

name_header = "Name"
calories_header = 'Calories'
protein_header = "Protein"
carbs_header = "Carbs"
fats_header = "Fats"


#FUNCTIONS

def SumMacros():
    try:
        sum_calories = 0
        sum_protein = 0
        sum_carbs = 0
        sum_fats = 0
        for i in range(len(meallist)):
            sum_calories += int(meallist[i][1])
            sum_protein += int(meallist[i][2])
            sum_carbs += int(meallist[i][3])
            sum_fats += int(meallist[i][4])
        print("Total: Calories: " + str(sum_calories) + " Protein: " + str(sum_protein) + " Carbs: " + str(sum_carbs) + " Fats: " + str(sum_fats))
    except: print("Could Not Calculate Macros")

def header():
    print([name_header, calories_header, protein_header, carbs_header, fats_header])

def Printlist():
    header()
    for item in meallist: print(item)

def newmealsheet():
    try:
        with open("MealSheet.csv",'r+') as file:
            mealsheet = csv.writer(file)
            while True:
                meal_name = input('Meal Name\n')
                if meal_name == "-1": break
                calories = pyip.inputInt('Total Calories\n')
                if calories == -1: break
                protein = pyip.inputInt('Grams of Protein\n')
                if protein == -1: break
                carbs = pyip.inputInt('Grams of Carbs\n')
                if carbs == -1: break
                fats = pyip.inputInt('Grams of fats\n')
                if fats == -1: break
                meallist.append([meal_name, calories, protein, carbs, fats])
                Printlist()
                SumMacros()

            while True:
                save = pyip.inputYesNo("Would You Like To Save? (Y/N)\n")
                print(save)
                if save == "yes":
                    for item in meallist:
                        mealsheet.writerow(item)
                    print("Changes Saved Thank You!")
                    meallist.clear()
                    break
                if save == "no":
                    print('Changes Not Saved')
                    meallist.clear()
                    break

    except: print("Something Went Wrong :(")

def OpenMealSheet():
    try:
        with open("MealSheet.csv", "r+") as file:
            mealsheet = csv.reader(file)
            for row in mealsheet: meallist.append(row)
            header()
            for item in meallist: print(item)
            SumMacros()
            meallist.clear()

    except: print("A Problem Occurred While Opening the Sheet")

def EditMeal():
    try:
        with open("MealSheet.csv", "r+") as file:
            mealsheetread = csv.reader(file)
            for row in mealsheetread: meallist.append(row)
            header()
            for i in range(len(meallist)): print(str(i+1) + ": " + str(meallist[i]))
            SumMacros()
            while True:
                editmeal_choice = pyip.inputInt(prompt="Which Meal Would You Like To Edit? (Enter -1 To Stop)\n", max=(len(meallist)))
                if editmeal_choice == -1: break
                meal_name = input('Meal Name\n')
                if meal_name == '-1': break
                calories = pyip.inputInt('Total Calories\n')
                if calories == -1: break
                protein = pyip.inputInt('Grams of Protein\n')
                if protein == -1: break
                carbs = pyip.inputInt('Grams of Carbs\n')
                if carbs == -1: break
                fats = pyip.inputInt('Grams of fats\n')
                if fats == -1: break
                meallist[editmeal_choice-1] = [meal_name, calories, protein, carbs, fats]
                for i in range(len(meallist)): print(str(i + 1) + ": " + str(meallist[i]))
                SumMacros()
            while True:
                editsave = pyip.inputYesNo("Would You Like to Save? (Y/N)\n")
                if editsave == "yes":
                    with open("MealSheet.csv", "w") as file:
                        mealsheetwrite = csv.writer(file)
                        for item in meallist:
                            mealsheetwrite.writerow(item)
                    meallist.clear()
                    print("Changes Saved!")
                    break
                if editsave == "no":
                    print("Changes Not Saved")
                    break
            meallist.clear()
    except: print("Something Went Wrong :(\n")

def AteToday():
    print('What Did You Eat Today?')
    while True:
        meal_name = input('Meal Name\n')
        if meal_name == "-1": break
        calories = pyip.inputInt('Total Calories\n')
        if calories == -1: break
        protein = pyip.inputInt('Grams of Protein\n')
        if protein == -1: break
        carbs = pyip.inputInt('Grams of Carbs\n')
        if carbs == -1: break
        fats = pyip.inputInt('Grams of fats\n')
        if fats == -1: break
        todaylist.append([meal_name, calories, protein, carbs, fats])


class Meal:
    def __init__(self, name, ingrdients, macros):
        self.name = name
        self.ingrdients = ingrdients
        self.macros = macros

    def calc_macros(self):
        pass
