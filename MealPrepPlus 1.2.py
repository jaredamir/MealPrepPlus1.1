import csv
import pyinputplus as pyip

ing_list_temp= []
meals_list = []
ing_names = []
new_meal_list= ["", 0, 0, 0, 0, 0]
meal_recipe = []
new_recipies = []
macro_sum = []

#ingredient info per serving (name, SS unit{**use input plus menu**}, calories, protein, carbs, fats, sugar)


def print_ing():
    with open("./Ingredients.csv", "r") as file:
        ing = csv.reader(file)
        for row in ing: ing_list_temp.append(row)
        #Neatly Printing Ingredients
        for i in range(len(ing_list_temp)):
            print(
            f"{ing_list_temp[i][0]} {ing_list_temp[i][1]} {ing_list_temp[i][2]} {ing_list_temp[i][3]} {ing_list_temp[i][4]} {ing_list_temp[i][5]} {ing_list_temp[i][6]}"
        )

def add_ingredient():
    with open("./Ingredients.csv", "r") as file:
        ing = csv.reader(file)
        for row in ing: ing_list_temp.append(row)
        #print(ing_list_temp)

        while True:
            name = pyip.inputStr("Name\n")
            unit = pyip.inputMenu(["tbsp", "tsp", "cups", "grams", "lbs", "oz", "item"], "Unit of Measurement of Serving Size\n")
            if unit=="item": num_unit = 1
            else: num_unit = pyip.inputFloat(f"Amount of {unit} per Serving\n")
            cal = pyip.inputFloat("Calories Per Serving\n")
            pro = pyip.inputFloat("Grams of Protein Per Serving\n")
            carb = pyip.inputFloat("Grams of Carbs Per Serving\n")
            fats = pyip.inputFloat("Grams of Fat Per Serving\n")
            sugar = pyip.inputFloat("Grams of Sugar Per Serving\n")

            ing_list_temp[-1]=[name, num_unit, unit, cal, pro, carb, fats, sugar] #FIX REPEATS (for ele
            #maybe add for i in range to show all  new ingredients
            print(
                f"{ing_list_temp[-1][0]}\nServing Size {ing_list_temp[-1][1]} {ing_list_temp[-1][2]}  {ing_list_temp[-1][3]} Calories  {ing_list_temp[-1][4]}g Protein  {ing_list_temp[-1][5]}g Carbs  {ing_list_temp[-1][6]}g Fats  {ing_list_temp[-1][7]}g Sugar"
            )
            print(ing_list_temp)
            sav = pyip.inputYesNo("Would You Like To Save New Ingredients?\n")
            if sav == "yes":  #FIXXXXXX
                with open("Ingredients.csv", "w", newline="") as file:
                    wt = csv.writer(file)
                    for item in ing_list_temp: wt.writerow(item)
                    ing_list_temp.clear()
                """
                with open("Ingredients.csv", "a") as file:
                    wt = csv.writer(file)
                    wt.writerow(["end"])
                    ing_list_temp.clear()
                """
            if sav == "no":
                print("Changes Not Saved")
                ing_list_temp.clear()
                break
            cont = pyip.inputYesNo("Would You Like to Add Another?\n")
            if cont == "yes":
                ing_list_temp.clear()
                pass
            if cont == "no":
                ing_list_temp.clear()
                break #FIXXXX

        #MAKE PRINTT LOOK NICER
ingredient_list = []
def search_ing():
    with open("Ingredients.csv", "r") as file:
        read = csv.reader(file)
        for row in read: ing_list_temp.append(row)
        for i in range(len(list)): ingredient_list.append(list[i][0])
        ing = pyip.inputMenu(ingredient_list, prompt="Which Ingredient Would You Like To Choose?\n") #Change to ele in ele
        ing_list_temp.clear()


def premade():
    print("Enter -1 at anytime to quit")
    while True:
        meal_name = input("Meal Name\n")
        if meal_name == "-1": break
        else: new_meal_list[0] = meal_name
        cal = pyip.inputFloat("Calories Per Serving\n")
        if cal== -1: break
        else: new_meal_list[1] = cal
        pro = pyip.inputFloat("Grams of Protein Per Serving\n")
        if pro == -1: break
        else: new_meal_list[2] = pro
        carb = pyip.inputFloat("Grams of Carbs Per Serving\n")
        if carb == -1: break
        else: new_meal_list[3] = carb
        fats = pyip.inputFloat("Grams of Fat Per Serving\n")
        if fats == -1: break
        else: new_meal_list[4] = fats
        sugar = pyip.inputFloat("Grams of Sugar Per Serving\n")
        if sugar == -1: break
        else: new_meal_list[5] = sugar
        print(new_meal_list)
        break



def recipe(): #**BREAD  AND BUTTER RIGHT HERE***
    with open("./Ingredients.csv", "r") as file:
        ing_read = csv.reader(file)
        for row in ing_read: ing_list_temp.append(row)
        print("Enter -1 at any point to stop")
        while True:
            meal_name = input("Meal Name\n")
            if meal_name == "-1": break
            else: meal_recipe.append(meal_name)

            while True:
                while True:
                    for i in range(len(ing_list_temp)): ing_names.append(ing_list_temp[i][0])
                    search = pyip.inputMenu(ing_names, numbered=True, prompt="Ingredient name\n")
                    if search == "-1": break
                    for i in range(len(ing_list_temp)):
                        if ing_list_temp[i][0].lower() == search.lower():
                            ing = ing_list_temp[i]
                            print(f"{ing[0]}\nCalories {ing[3]}g Protein {ing[4]}g Carbs {ing[5]}g Fats {ing[6]}g Sugar") #ADD SERVING SIZE
                            meas_amount = pyip.inputFloat("Amount without unit\n")
                            meas_unit= pyip.inputMenu(["tbsp", "tsp", "cup", "grams", "lbs", "oz", "item"], "Unit\n")
                            print(f"{meas_amount} {meas_unit} of {ing[0]}")
                            add = pyip.inputYesNo("\nAdd Ingredient\n")
                            if add == "yes": meal_recipe.append([ing[0], meas_amount, meas_unit])

                            print("\n" + meal_recipe[0])
                            for i in range(len(meal_recipe)):
                                if i == 0: pass
                                else: print(f"{meal_recipe[i][1]} {meal_recipe[i][2]} of {meal_recipe[i][0]}\n")
                            break
                        if ing_list_temp[i] == "":
                            print("Ingredient Not found")

            ing_list_temp.clear()
            break
def new_meal():
    ml = pyip.inputMenu(["Recipe", "Pre-Made", "Pre-Made With Other Ingredients"], prompt="What Type of Meal Are You Adding\n")
    if ml == "Recipe":
        meal_name = input("Meal Name\n")
        new_meal_list[0] = meal_name
        print(new_meal_list)

        #ADDING ING THEN SUMMING MACROS TO ADD TO [0]
        #ADDING ALL OF THIS INTO A NEW LIST TO BE APPENDED TO MEALS LIST
    if ml == "Pre-Made":
        premade()
    if ml == "Pre-Made With Other Ingredients":
        premade()


#find a way to make it so meals can be made from scratch, be derivatives from others, and be made whole
recipe()

#ADD CALORIE GOALS
