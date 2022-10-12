import csv
import pyinputplus as pyip
import pickle

#Testers
test_plan_one = [["monday plan",0,0,0,0,0],[["microwave mac and cheese",500,25,60,25,10]]]
test_plan_two = [["monday plan",0,0,0,0,0],[[["boom boom chicken",0,0,0,0,0],[["ham",3.0,"grams",70.0,15.0,10.0,10.0,9.0],["ham",3.0,"grams",70.0,15.0,10.0,10.0,9.0]]],
                                            ["microwave mac and cheese",500,25,60,25,10],
                                            ["microwave mac and cheese",500,25,60,25,10],
                                            [["boom boom chicken",0,0,0,0,0],[["ham",3.0,"grams",70.0,15.0,10.0,10.0,9.0],["ham",3.0,"grams",70.0,15.0,10.0,10.0,9.0]]]

                                            ]]

test_recipe = [["boom boom chicken",0,0,0,0,0],[["ham",3.0,"grams",70.0,15.0,10.0,10.0,9.0],["ham",3.0,"grams",70.0,15.0,10.0,10.0,9.0]]]
test_premade = ["microwave mac and cheese",500,25,60,25,10]

#Varibales
units_list= ["tbsps", "tsps", "cups", "grams", "lbs", "oz", "Liters", "other"]


#Classes
class Ingredient:
    def __init__(self,ing):
        try:
            self.name = ing[0]
            self.ing_amount = ing[1]
            self.unit = ing[2]
            self.ing_cal = ing[3]
            self.ing_pro = ing[4]
            self.ing_carb = ing[5]
            self.ing_fats = ing[6]
            self.ing_sugar = ing[7]
            self.full_ing = [self.name,self.ing_amount,self.unit,self.ing_cal,self.ing_pro,self.ing_carb,self.ing_fats,self.ing_sugar]
        except: print("Something is Wrong with Ingredient Data")

    def quantity(self, ning):
        try:
            self.ing_name = ning[0]
            self.unit = ning[2]
            ing_cal = float(ning[3])
            ing_pro = float(ning[4])
            ing_carb = float(ning[5])
            ing_fats = float(ning[6])
            ing_sugar = float(ning[7])

            self.ing_amount = float(input(f"How Many {self.unit} Are You Adding?\n"))

            serv = float(ning[1])
            fac = self.ing_amount / serv
            self.new_cal = round((ing_cal * fac), 2)
            self.new_pro = round((ing_pro * fac), 2)
            self.new_carb = round((ing_carb * fac), 2)
            self.new_fats = round((ing_fats * fac), 2)
            self.new_sugar = round((ing_sugar * fac), 2)

            self.up_ing = [self.ing_name,self.ing_amount,self.unit,self.new_cal,self.new_pro,self.new_carb,self.new_fats,self.new_sugar]
        except: print("Something is wrong with Ingredient Data")

    def print_ing(self):
        try:
            print(f"-{self.ing_amount} {self.unit} of {self.name}\n"
                  f"    {self.ing_cal} Calories\n"
                  f"    {self.ing_pro} G of Protein\n"
                  f"    {self.ing_carb} G of Carbs \n"
                  f"    {self.ing_fats} G of Fats \n"
                  f"    {self.ing_sugar} G of Sugar \n"
                  )
        except: print("Could Not Print, Something is Wrong with Ingredient Data")

class New_Ingredient:
    def __init__(self):
        try:
            ing_file = []
            with open("Ingredients.csv", "r") as file:
                read = csv.reader(file)
                for row in read:
                    ing_file.append(row)

            while True:
                check = []
                for i in range(len(ing_file)):
                    check.append(ing_file[i][0])
                while True:
                    self.name = input("Ingredient Name\n")
                    if self.name in check:
                        print(f"{self.name} is already in the list")
                    else:
                        check.clear()
                        break

                self.unit = pyip.inputMenu(units_list, "Unit of Measurment for Serving Size\n", numbered=True, )
                if self.unit == "other":
                    self.unit = input("Name of Unit (If Unit is an Item, Use Plural)\n")
                self.amount = pyip.inputFloat(f"Amount of {self.unit} per Serving\n")
                self.cal = pyip.inputFloat("Calories per serving\n")
                self.pro = pyip.inputFloat("Grams of Protein per Serving\n")
                self.carb = pyip.inputFloat("Grams of Carbs per serving\n")
                self.fats = pyip.inputFloat("Grams of Fats per serving\n")
                self.sugar = pyip.inputFloat("Grams of Sugar per serving\n")

                # ing = Ingredient(name, cal, pro)
                print(f"\n{self.name}\n"
                      f"Serving Size: {self.amount} {self.unit}\n"
                      f"    {self.cal} Calories per Serving\n"
                      f"    {self.pro} G of Protein per Serving\n"
                      f"    {self.carb} G of Carbs per Serving\n"
                      f"    {self.fats} G of Fats per Serving\n"
                      f"    {self.sugar} G of Sugar per Serving\n"
                      )
                self.full_ing = [self.name, self.amount, self.unit, self.cal, self.pro, self.carb, self.fats, self.sugar]
                save = pyip.inputYesNo("would you like to save Ingredient?\n")
                if save == "yes":
                    ing_file.append(self.full_ing)
                    with open("Ingredients.csv", "w") as file:
                        writer = csv.writer(file)
                        for item in ing_file: writer.writerow(item)
                    print("Saved!")
                    break
                if save == "no":
                    print("Not Saved")
                    break
        except: print("Something Went Wrong With the New Ingredient")

class NewMeal:
    def __init__(self):
        try:
            with open("Meal_File.pickle", "rb") as file:
                meals_file = pickle.load(file)
                file.close()
            check = []
            for i in range(len(meals_file)):
                if type(meals_file[i][1]) == list:
                    check.append(meals_file[i][0][0])
                else:
                    check.append(meals_file[i][0])
            print(check)
            while True:
                self.name = input("Meal Name\n")
                if self.name in check:
                    print(f"{self.name} is already in the list")
                else:
                    break

            meal_type = pyip.inputMenu(["Recipe", "Pre-Made with Add-ons", "Pre-Made"], numbered=True, prompt="Meal Name\n")
            self.ings = []

            if meal_type == "Recipe":

                self.meal_info = [self.name,0,0,0,0,0]
                ing_file = []
                ing_names=[]
                with open("Ingredients.csv", "r") as file:
                    read = csv.reader(file)
                    for row in read: ing_file.append(row)
                for i in range(len(ing_file)): ing_names.append(ing_file[i][0])

                while True:
                    search = pyip.inputMenu(ing_names, numbered=True, prompt="ingredient name\n")

                    for i in range(len(ing_file)): #maybe  switch out for ingrident class
                        if ing_file[i][0] == search:
                            ning = ing_file[i]
                            cl_uping = Ingredient()
                            cl_uping.quantity(ning)
                            print(f"{cl_uping.ing_amount} {cl_uping.unit} of {cl_uping.ing_name}\n"
                                  f"    {cl_uping.new_cal} Calories per Serving\n"
                                  f"    {cl_uping.new_pro} G of Protein per Serving\n"
                                  f"    {cl_uping.new_carb} G of Carbs per Serving\n"
                                  f"    {cl_uping.new_fats} G of Fats per Serving\n"
                                  f"    {cl_uping.new_sugar} G of Sugar per Serving\n"
                                  )

                            add = pyip.inputYesNo("would you like to add? (y/n)\n")
                            if add == "yes":
                                self.ings.append(cl_uping.up_ing)
                                print(self.ings)
                                cont = pyip.inputYesNo("Add Another Ingredient?\n")
                                if cont == "yes":
                                    pass
                                if cont == "no":
                                    save_meal = pyip.inputYesNo("Would you Like to save Meal?\n")
                                    if save_meal == "yes":
                                        self.full_meal=[list(self.meal_info),list(self.ings)]
                                        print(self.full_meal)

                                        meals_file.append(self.full_meal)
                                        print(meals_file)

                                        with open("Meal_File.pickle", "wb") as file:
                                            pickle.dump(meals_file, file)
                                            file.close()
                                        print("Saved!")

                                        break
                                    if save_meal == "no":
                                        print("Not Saved")
                                        break
                            if add == "no":
                                print("not added")

            if meal_type == "Pre-Made with Add-ons": #rework to work with meal too
                self.cal = pyip.inputFloat("Total Calories\n")
                self.pro = pyip.inputFloat("Total Grams of Protein\n")
                self.carb = pyip.inputFloat("Total Grams of Carbs\n")
                self.fats = pyip.inputFloat("Total Grams of Fats\n")
                self.sugar = pyip.inputFloat("Total Grams of Sugar\n")
                self.meal_info = [self.name,self.cal,self.pro,self.carb,self.fats,self.sugar]

                ing_file = []
                ing_names = []
                with open("Ingredients.csv", "r") as file:
                    read = csv.reader(file)
                    for row in read: ing_file.append(row)
                for i in range(len(ing_file)): ing_names.append(ing_file[i][0])

                while True:
                    search = pyip.inputMenu(ing_names, numbered=True, prompt="ingredient name\n")

                    for i in range(len(ing_file)):
                        if ing_file[i][0] == search:
                            ning = ing_file[i]
                            cl_uping = Ingredient()
                            cl_uping.quantity(ning)
                            print(f"{cl_uping.ing_amount} {cl_uping.unit} of {cl_uping.ing_name}\n"
                                  f"    {cl_uping.new_cal} Calories\n"
                                  f"    {cl_uping.new_pro} G of Protein\n"
                                  f"    {cl_uping.new_carb} G of Carbs \n"
                                  f"    {cl_uping.new_fats} G of Fats \n"
                                  f"    {cl_uping.new_sugar} G of Sugar \n"
                                  )

                            add = pyip.inputYesNo("would you like to add? (y/n)\n")
                            if add == "yes":
                                self.ings.append(cl_uping.up_ing)
                                print(self.ings)
                                cont = pyip.inputYesNo("Add Another Ingredient?\n")
                                if cont == "yes":
                                    pass
                                if cont == "no":
                                    save_meal = pyip.inputYesNo("Would you Like to save Meal?\n")
                                    if save_meal == "yes":
                                        self.full_meal = [self.meal_info,self.ings]


                                        meals_file.append(self.full_meal)

                                        with open("Meal_File.pickle", "wb") as file:
                                            pickle.dump(meals_file, file)
                                            file.close()
                                        print("Saved!")

                                        break
                                    if save_meal == "no":
                                        print("Not Saved")
                                        break
                            if add == "no":
                                print("not added")

            if meal_type == "Pre-Made":
                self.cal = pyip.inputFloat("Total Calories\n")
                self.pro = pyip.inputFloat("Total Grams of Protein\n")
                self.carb = pyip.inputFloat("Total Grams of Carbs\n")
                self.fats = pyip.inputFloat("Total Grams of Fats\n")
                self.sugar = pyip.inputFloat("Total Grams of Sugar\n")
                self.meal_info = [self.name,self.cal,self.pro,self.carb,self.fats,self.sugar]
                save_meal = pyip.inputYesNo("Would you Like to save Meal?\n")
                if save_meal == "yes":
                    self.full_meal = self.meal_info

                    meals_file.append(self.full_meal)

                    with open("Meal_File.pickle", "wb") as file:
                        pickle.dump(meals_file, file)
                        file.close()
                    print("Saved!")


                if save_meal == "no":
                    print("Not Saved")
        except: print("Something Went Wrong with the New Meal")

class Meal:
    def __init__(self, meal):
        try:
            self.meal = meal
            self.check = type(self.meal[1])
            if self.check == list:
                self.meal_info = meal[0]
                self.initial_cal = self.meal_info[1]
                self.initial_pro = self.meal_info[2]
                self.initial_carb = self.meal_info[3]
                self.initial_fats = self.meal_info[4]
                self.initial_sugar = self.meal_info[5]
                self.ings = meal[1]

                for i in range(len(self.ings)):
                    self.initial_cal += float(self.ings[i][3])
                    self.initial_pro += float(self.ings[i][4])
                    self.initial_carb += float(self.ings[i][5])
                    self.initial_fats += float(self.ings[i][6])
                    self.initial_sugar += float(self.ings[i][7])

                self.name = self.meal_info[0]
                self.cal = self.initial_cal
                self.pro = self.initial_pro
                self.carb = self.initial_carb
                self.fats = self.initial_fats
                self.sugar = self.initial_sugar


            else:
                self.name = meal[0]
                self.cal = meal[1]
                self.pro = meal[2]
                self.carb = meal[3]
                self.fats = meal[4]
                self.sugar = meal[5]
                # print("premade")
        except: print("Something Wrong with Meal Data")
    def printmeal(self):
        #try:
        print(f"{self.name}")
        if self.check == list:
            if self.meal_info[1] > 0:
                print(
                    f"{self.meal_info[1]} Calories  {self.meal_info[2]} G of Protein  {self.meal_info[3]} G of Carbs  {self.meal_info[4]} G of Fats  {self.meal_info[5]} G of Sugar")

            for i in range(len(self.ings)):
                ing=Ingredient(self.ings[i])
                ing.print_ing()
        print(f"{self.cal} Calories  {self.pro} G of Protein  {self.carb} G of Carbs  {self.pro} G of Fats  {self.pro} G of Sugar")

        #except: print("Something Went Wrong. Could Not Print Meal")

class User:
    def __init__(self):
        pass
    def new_user(self):
        self.user_name = input("What is your name")
        self.weight = pyip.inputFloat("What Is your weight")

        #work on meal list, and meal plan first

class Meal_Plan:
    def __init__(self, plan):
        try:
            #Structure [[plan info],[[meal,[meal],[etc]]]
            #plan_info = [name,macros]
            self.plan = plan
            self.plan_info = plan[0]
            self.meals= plan[1]

            self.name=self.plan_info[0]
            self.cal = self.plan_info[1]
            self.pro = self.plan_info[2]
            self.carb = self.plan_info[3]
            self.fats = self.plan_info[4]
            self.sugar = self.plan_info[5]


            for i in range(len(self.meals)):
                cl_meal = Meal(self.meals[i])
                self.cal += cl_meal.cal
                self.pro += cl_meal.pro
                self.carb += cl_meal.carb
                self.fats += cl_meal.fats
                self.sugar += cl_meal.sugar
        except: print("Something Went Wrong. Could Not Make New Plan")

    def print_plan(self):
        try:
            print(self.name)

            for i in range(len(self.meals)):
                cl_meal=Meal(self.meals[i])
                cl_meal.printmeal()

            print(f"{self.cal} Calories  {self.pro} G of Protein  {self.carb} G of Carbs  {self.fats} G of Fats  {self.sugar} G of Sugar")
        except: print("Something Went Wrong. Could Not Print Plan")

class New_Plan:
    def __init__(self):
        try:
            with open("Meal_Plans.pickle", "rb") as file:
                meal_plans_file = pickle.load(file)
                file.close()

            check = []
            for i in range(len(meal_plans_file)):
                check.append(meal_plans_file[i][0][0])
            print(check)
            while True:
                self.name = input("Meal Plan Name\n")
                if self.name in check:
                    print(f"{self.name} is already in the list")
                else:
                    break
            self.plan_info = [self.name,0,0,0,0,0]
            self.cal = 0
            self.pro = 0
            self.carb = 0
            self.fats = 0
            self.sugar = 0
            self.meals = []

            with open("Meal_File.pickle", "rb") as file:
                meals_file = pickle.load(file)
                file.close()

            meals_names = []
            for i in range(len(meals_file)):
                cl_meal = Meal(meals_file[i])
                meals_names.append(cl_meal.name)

            while True:
                search = pyip.inputMenu(meals_names, numbered=True, prompt="Meal Name\n")
                while True:
                    for i in range(len(meals_file)):
                        sm = Meal(meals_file[i])
                        if sm.name == search:
                            meal = Meal(meals_file[i])
                            meal.printmeal()
                    add = pyip.inputYesNo("Add to Plan? (Y/N)\n")
                    if add == "yes":
                        self.meals.append(meal.meal)
                        self.cal = 0
                        self.pro = 0
                        self.carb = 0
                        self.fats = 0
                        self.sugar = 0
                        for i in range(len(self.meals)):
                            cl_meal_macros = Meal(self.meals[i])
                            self.cal += cl_meal_macros.cal
                            self.pro += cl_meal_macros.pro
                            self.carb += cl_meal_macros.carb
                            self.fats += cl_meal_macros.fats
                            self.sugar += cl_meal_macros.sugar
                        print(
                            f"{self.cal} Calories  {self.pro} G of Protein  {self.carb} G of Carbs  {self.pro} G of Fats  {self.pro} G of Sugar")

                        break

                    if add == "no":
                        print("Not Added")
                        break
                contin = pyip.inputYesNo("Add Another Meal? (Y/N)\n")
                if contin == "yes":
                    pass
                if contin == "no":

                    save = pyip.inputYesNo("Save Meal? (Y/N)\n")
                    if save == "yes":
                        self.full_plan = [self.plan_info,self.meals]
                        meal_plans_file.append(self.full_plan)

                        with open("Meal_Plans.pickle", "wb") as file:
                            pickle.dump(meal_plans_file,file)
                            file.close()
                        print("Saved!")
                        break
                    if save == "no":
                        print("Not Saved")
                        break
        except: print("Something Went Wrong While Making New Plan")

#functions
def search_ing():
    #try:
    ing_file = []
    with open("Ingredients.csv", "r") as file:
        read = csv.reader(file)
        for row in read: ing_file.append(row)

    ing_names = []
    for i in range(len(ing_file)): ing_names.append(ing_file[i][0])
    search = pyip.inputMenu(ing_names, numbered=True, prompt="Choose An Ingredient\n")
    for i in range(len(ing_file)):
        if ing_file[i][0]==search:
            ing_index=i
            cl_ing = Ingredient(ing_file[i])
            cl_ing.print_ing()
    ing_action_choices= pyip.inputMenu(["Edit Ingredient", "Delete Ingredient", "Go Back"], numbered=True, prompt="")
    if ing_action_choices == "Edit Ingredient":
        while True:
            ing_edit_choices=pyip.inputMenu(["Name", "Serving Size", "Calories", "Protein", "Carbs", "Fats", "Sugar", "Done"], numbered=True, prompt="Edit\n")
            if ing_edit_choices == "Name":
                check = []
                for i in range(len(ing_file)):
                    check.append(ing_file[i][0])
                while True:
                    cl_ing.name = input("Ingredient Name\n")
                    if cl_ing.name in check:
                        print(f"{cl_ing.name} is already in the list")
                    else:
                        cl_ing.print_ing()
                        check.clear()
                        break

            if ing_edit_choices == "Serving Size":
                cl_ing.unit = pyip.inputMenu(units_list, numbered=True, prompt="unit\n")
                cl_ing.ing_amount=pyip.inputFloat(f"How Many {cl_ing.unit} per Serving\n")
                cl_ing.print_ing()

            if ing_edit_choices == "Calories":
                cl_ing.ing_cal = pyip.inputFloat("Amount of Calories per Serving\n")
                cl_ing.print_ing()

            if ing_edit_choices == "Protein":
                cl_ing.ing_pro = pyip.inputFloat("How Many Grams of Protein Per Serving\n")
                cl_ing.print_ing()

            if ing_edit_choices == "Carbs":
                cl_ing.ing_carb = pyip.inputFloat("How Many Grams of Carbs Per Serving\n")
                cl_ing.print_ing()

            if ing_edit_choices == "Fats":
                cl_ing.ing_fats = pyip.inputFloat("How Many Grams of Fats Per Serving\n")
                cl_ing.print_ing()

            if ing_edit_choices == "Sugar":
                cl_ing.ing_sugar = pyip.inputFloat("How Many Grams of Sugar Per Serving\n")
                cl_ing.print_ing()

            if ing_edit_choices == "Done":
                try:
                    save_ing_edits = pyip.inputYesNo("Would You Like to Save Changes?\n")
                    if save_ing_edits == "yes":
                        edit_updated_ing = [cl_ing.name,cl_ing.ing_amount,cl_ing.unit,cl_ing.ing_cal,cl_ing.ing_pro,cl_ing.ing_carb,cl_ing.ing_fats,cl_ing.ing_sugar]
                        ing_file[ing_index]=edit_updated_ing
                        with open("Ingredients.csv", "w") as file:
                            write=csv.writer(file)
                            for item in ing_file: write.writerow(item)
                        ing_file.clear()
                        print("Ingredient Updated")
                        break
                    if save_ing_edits == "no":
                        print("changes not saved")
                        break
                except: print("Could Not Save Changes")

    if ing_action_choices == "Delete Ingredient":
        delete_choice=pyip.inputYesNo(f"Are You Sure You Want to Delete {cl_ing.name} from File?\n")
        if delete_choice == "yes":
            del(ing_file[ing_index])
            with open("Ingredients.csv", "w") as file:
                write=csv.writer(file)
                for item in ing_file: write.writerow(item)
            ing_file.clear()
            print("Changes Saved")

    if ing_action_choices == "Go Back":
        pass
        
    #except: print("Something Went Wrong With Search")

def search_meal():
    #try:
    with open("Meal_File.pickle", "rb") as file:
        meals_file = pickle.load(file)
        file.close()
    meal_names=[]
    for i in range(len(meals_file)):
        cl_meal = Meal(meals_file[i])
        meal_names.append(cl_meal.name)
    search = pyip.inputMenu(meal_names,numbered=True,prompt="Meal Name\n")
    for i in range(len(meals_file)):
        cl_meal = Meal(meals_file[i])
        meal_index = i

        if cl_meal.name == search:
            break
    cl_meal.printmeal()
    #except: print("Something Wrong with Meal Data or Meal File")

    meal_action_choices = pyip.inputMenu(["Edit Meal", "Delete Meal", "Go Back"], numbered=True, prompt="")
    if meal_action_choices == "Edit Meal":
        if cl_meal.check == list:
            #Recipe
            if cl_meal.meal[0][1] == 0 and cl_meal.meal[0][2] == 0:
                recipe_edit_options = ["Add Ingredient", "Change Ingredient Amount", "Delete Ingredient"]
                meal_edit_choice = pyip.inputMenu(recipe_edit_options, numbered=True, prompt="**testing recipe\n")
            #Pre-With Addons
            else:
                pre_w_a_edit_options = ["Change Meal Info", "Add Ingredient", "Change Ingredient Amount","Delete Ingredient"]
                meal_edit_choice = pyip.inputMenu(pre_w_a_edit_options, numbered=True, prompt="**testing pre wit adons\n")
            #Pre-Made
        else:
            pre_made_edit_options = ["Meal Name", "Total Calories", "Grams of Protein", "Grams of Carbs", "Grams of Fats", "Grams of Sugar", "Done"]
            while True:
                meal_edit_choice = pyip.inputMenu(pre_made_edit_options, numbered=True, prompt="**testing Editpre made\n")
                if meal_edit_choice == "Meal Name":
                    cl_meal.name = input("Meal Name\n")
                    cl_meal.printmeal()
                if meal_edit_choice == "Total Calories":
                    cl_meal.cal = pyip.inputFloat("Total Calories\n")
                    cl_meal.printmeal()
                if meal_edit_choice == "Grams of Protein":
                    cl_meal.pro = pyip.inputFloat("Grams of Protein\n")
                    cl_meal.printmeal()
                if meal_edit_choice == "Grams of Carbs":
                    cl_meal.carb = pyip.inputFloat("Grams of Carbs\n")
                    cl_meal.printmeal()
                if meal_edit_choice == "Grams of Fats":
                    cl_meal.fats = pyip.inputFloat("Grams of Fats\n")
                    cl_meal.printmeal()
                if meal_edit_choice == "Grams of Sugar":
                    cl_meal.sugar = pyip.inputFloat("Grams of Sugar\n")
                    cl_meal.printmeal()
                if meal_edit_choice == "Done":
                    break
            cl_meal.printmeal()
            save_pre_edits = pyip.inputYesNo("Would You Like To Save Changes\n")
            if save_pre_edits == "yes":
                print("**testing**")
                #try:
                with open("Meal_File.pickle", "rb") as file:
                    meals_file = pickle.load(file)
                    file.close()
                meals_file[meal_index] = [cl_meal.name,cl_meal.cal,cl_meal.pro,cl_meal.carb,cl_meal.fats,cl_meal.sugar]
                with open("Meal_File.pickle", "wb") as file:
                    pickle.dump(meals_file, file)
                    file.close()

                #test check
                with open("Meal_File.pickle", "rb") as file:
                    meals_file = pickle.load(file)
                    file.close()
                    print(meals_file)

                #except: print("Something Went Wrong. Could Not Save Meal")
            if save_pre_edits == "no":
                print("Changes Not Saved")



    if meal_action_choices == "Delete Meal":
        meal_delete_choice = pyip.inputYesNo("Are You Sure You Want to Delete This Meal?\n")
        if meal_delete_choice == "yes":
            del(meals_file[meal_index])
            with open("Meal_File.pickle", "wb") as file:
                pickle.dump(meals_file, file)
                file.close()
            print("Changes Saved")
            #test
            with open("Meal_File.pickle",'rb') as file:
                meals_file = pickle.load(file)
                file.close()
            print(meals_file)

    if meal_action_choices == "Go Back":
        pass

def search_plan():
    try:
        with open("Meal_Plans.pickle", "rb") as file:
            meal_plans_file=pickle.load(file)
            file.close()
        plans_list=[]
        for i in range(len(meal_plans_file)):
            cl_plan = Meal_Plan(meal_plans_file[i])
            plans_list.append(cl_plan.name)
        search = pyip.inputMenu(plans_list, numbered=True, prompt="Which Plan Would You Like to Open?\n")
        for i in range(len(meal_plans_file)):
            cl_plan = Meal_Plan(meal_plans_file[i])
            if search == cl_plan.name:
                cl_plan=Meal_Plan(meal_plans_file[i])
                cl_plan.print_plan()
    except: print("Something is Wrong with Meal Plan Data or Meal Plan File")

def reset_Meal_Plan_File():
    try:
        with open("Meal_Plans.pickle", "wb") as file:
            x = []
            pickle.dump(x,file)
            file.close()
            print("Plan Reset")
    except: print("Could Not Reset File")

def reset_Meals_File():
    try:
        with open("Meal_File.pickle", "wb") as file:
            x = []
            pickle.dump(x,file)
            file.close()
            print("Meal File Reset")
    except: print("Could Not Reset File")

def admin_files_check():
    try:
        with open("Meal_Plans.pickle","rb") as file:
            meal_plans_file = pickle.load(file)
            file.close()
        print(f"Meal Plan File:\n {meal_plans_file}\n")
    except:
        print("Problem with Meal Plan File")

    try:
        with open("Meal_File.pickle","rb") as file:
            meals_file = pickle.load(file)
            file.close()
        print(f"Meals File:\n {meals_file}\n")
    except:
        print("Problem with Meal Plan File")

#Edit abilities, Delete Abilities
New_Plan()

#monitor file command (check, #of [i], if empty, if anythibg but name and  unit is a float (class)


"""
ideas:
app scanner to immediently put in meals
"""