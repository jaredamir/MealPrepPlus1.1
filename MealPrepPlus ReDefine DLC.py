#Section for admin to add and delete meals
import csv
import pyinputplus as pyip
import pickle

#Variables
redefine_meal_file = []

#Classes
class Meal:
    def __init__(self, meal):
        if type(meal) != list: print("Incorrect Data Type")
        else:
            if len(meal) != 6: print("Meal Data Missing Element Or Is Corrupted")
            else:
                self.name = meal[0]
                self.cal = meal[1]
                self.pro = meal[2]
                self.carb = meal[3]
                self.fats = meal[4]
                self.sugar = meal[5]
                self.data = [self.name,self.cal,self.pro,self.carb,self.fats,self.sugar]

    def print_meal(self):
        print(f"{self.name}\n"
                f"{self.cal} Calories  {self.pro} G of Protein  {self.carb} G of Carbs  {self.fats} G of Fats  {self.sugar} G of Sugar")

class New_Meal:
    def __init__(self):
        try:
            with open("ReDefine Meals.csv", "r") as file:
                read = csv.reader(file)
                for row in read: redefine_meal_file.append(row)
            print("Opening CSV")
            meal_names = []
            for i in range(len(redefine_meal_file)):
                meal_names.append(redefine_meal_file[i][0])
            while True:
                self.name=pyip.inputStr("Meal Name\n")
                if self.name in meal_names:
                    print("Meal Already In System")
                else:
                    meal_names.clear()
                    break
        except:
            print("No CSV")
            self.name = pyip.inputStr("Meal Name\n")
        self.cal = pyip.inputFloat("Total Calories\n")
        self.pro = pyip.inputFloat("Grams of Protein\n")
        self.carb = pyip.inputFloat("Grams of Carbs\n")
        self.fats = pyip.inputFloat("Grams of Fats\n")
        self.sugar = pyip.inputFloat("Grams of Sugar\n")
        self.meal_info = [self.name,self.cal,self.pro,self.carb,self.fats,self.sugar]
        print(f"{self.name}\n"
              f"{self.cal} Calories  {self.pro} G of Protein  {self.carb} G of Carbs  {self.fats} G of Fats  {self.sugar} G of Sugar")
        save_meal = pyip.inputYesNo("Would You Like To Save?\n")
        if save_meal == "yes":
            redefine_meal_file.append(self.meal_info)
            with open("ReDefine Meals.csv", "w") as file:
                write = csv.writer(file)
                for item in redefine_meal_file: write.writerow(item)
            redefine_meal_file.clear()
            print("Meal Saved!")
        if save_meal == "no":
            print("Meal Not Saved")
            redefine_meal_file.clear()

class Plan:
    def __init__(self, plan):
        self.initial_cal = 0
        self.initial_pro = 0
        self.initial_carb = 0
        self.initial_fats = 0
        self.initial_sugar = 0
        if type(plan[0]) == str and type(plan[1]) == list:
            for i in range(len(plan[1])): ###
                if type(plan[1][i]) != list:
                    print("Corrupted or Incorrect Data Type")
                    break
                else:
                    self.name = plan[0]
                    self.meal_plan_list = plan[1]
                    self.length = len(self.meal_plan_list)
                    try:
                        for i in range(len(self.meal_plan_list)):
                            self.initial_cal += float(self.meal_plan_list[i][1])
                            self.initial_pro += float(self.meal_plan_list[i][2])
                            self.initial_carb += float(self.meal_plan_list[i][3])
                            self.initial_fats += float(self.meal_plan_list[i][4])
                            self.initial_sugar += float(self.meal_plan_list[i][5])
                    except:
                        print("One of the Meals In List Is Corrupted Or Is An Incorrect Data Type")

                    self.cal = self.initial_cal
                    self.pro = self.initial_pro
                    self.carb = self.initial_carb
                    self.fats = self.initial_fats
                    self.sugar = self.initial_sugar
                    break
        else:
            print("Corrupted or Incorrect Data Type")

    def print_plan(self):
        print(f"{self.name}")
        for i in range(self.length):
            cl_meal= Meal(self.meal_plan_list[i])
            cl_meal.print_meal()
        print(f"\n{self.cal} Total Calories  {self.pro} G of Protein  {self.carb} G of Carbs  {self.fats} G of Fats  {self.sugar} G of Sugar")

class NewPlan:
    def __init__(self):
        redefine_plan_file = []
        try:
            with open("ReDefine Meals.csv", "r") as file:
                read = csv.reader(file)
                for row in read: redefine_meal_file.append(row)
            print("Opening Meals File")
        except:
            print("No Meals Available")
            return None
        try:
            with open("Redefine Plans.pickle", "rb") as file:
                redefine_plan_file = pickle.load(file)
                file.close()
        except:
            print("No PKL File")
        plan_names = []
        for i in range(len(redefine_plan_file)):
            plan_names.append(redefine_plan_file[i][0])
        if plan_names!=[]:
            while True:
                self.name = pyip.inputStr("Name of Meal Plan\n")
                if self.name in plan_names:
                    print("Name Already Used By Another Plan")
                else:
                    break
        else:
            self.name = pyip.inputStr("Name of Meal Plan\n")

        self.meals = []
        #try:
        meal_names = []
        for i in range(len(redefine_meal_file)):
            meal_names.append(redefine_meal_file[i][0])
        while True:
            meal_search = pyip.inputMenu(meal_names, numbered=True, prompt="Add A Meal\n")
            for i in range(len(redefine_meal_file)):
                try:
                    if redefine_meal_file[i][0] == meal_search:
                        meal_index = i
                        cl_meal = Meal(redefine_meal_file[meal_index])
                        cl_meal.print_meal()
                        add_to_plan = pyip.inputYesNo("Add To Plan?\n")
                        if add_to_plan == "yes":
                            self.meals.append(redefine_meal_file[meal_index])
                        if add_to_plan == "no":
                            print("Not Added")
                        break
                except:
                    print("Something Went Wrong. Could Not Add Plan")
            print(self.meals)
            add_another = pyip.inputYesNo("Add Another?\n")
            if add_another == "yes":
                pass
            if add_another == "no":
                break
        #except: print("Something Went Wrong")

        if self.meals == []:
            print("Meal Plan Has No Meals Added. Please Try Again")
            return None
        else:
            self.full_plan = [self.name, self.meals]
            cl_plan = Plan(self.full_plan)
            cl_plan.print_plan()
            save = pyip.inputYesNo("Save Meal Plan?\n")
            if save == "yes":
                try:
                    redefine_plan_file.append(self.full_plan)
                    with open("Redefine Plans.pickle", "wb") as file:
                        pickle.dump(redefine_plan_file, file)
                        file.close()
                except: print("Something Went Wrong. Could Not Save")
            if save == "no":
                print("Not Saved")
                return None

class User:
    def __init__(self, user_info):
        #format: [name, cal, pro, carb, fats, sugar, history_file]
        if type(user_info) != list:
            print("Wrong Data type")
            return None
        if len(user_info) != 7:
            print("User Info Incomplete or Corrupted")
            return None


        self.name = user_info[0]
        self.cal_goal = user_info[1]
        self.pro_goal = user_info[2]
        self.carb_goal = user_info[3]
        self.fats_goal = user_info[4]
        self.sugar_goal = user_info[5]
        self.history_file = user_info[6]

    def compare(self, plan):

        self.cal_compare = self.cal_goal - plan.cal
        self.pro_compare = self.pro_goal - plan.pro
        self.carb_compare = self.carb_goal - plan.carb
        self.fats_compare = self.fats_goal - plan.fats
        self.sugar_compare = self.sugar_goal - plan.sugar

        if self.cal_compare >= 10:
            print(f"Your Meal Plan is {self.cal_compare} Calories Under Your Daily Calorie Goal")
        if self.pro_compare >= 10:
            print(f"Your Meal Plan is {self.pro_compare} Grams Under Your Daily Protein Goal")
        if self.carb_compare >= 10:
            print(f"Your Meal Plan is {self.carb_compare} Grams Under Your Daily Carbs Goal")
        if self.fats_compare >= 10:
            print(f"Your Meal Plan is {self.fats_compare} Grams Under Your Daily Fats Goal")


        if self.cal_compare <= -10:
            print(f"Your Meal Plan is {self.cal_compare * -1} Calories Over Your Daily Recommended Calorie Range")
        if self.pro_compare <= -10:
            print(f"Your Meal Plan is {self.pro_compare} Grams Over Your Daily Recommended Protein Range")
        if self.carb_compare <= -10:
            print(f"Your Meal Plan is {self.carb_compare * -1} Grams Over Your Daily Recommended Carb Range")
        if self.fats_compare <= -10:
            print(f"Your Meal Plan is {self.fats_compare * -1} Grams Over Your Daily Recommended Calorie Range")
        if self.sugar_compare <= -10:
            print(f"Your Meal Plan is {self.sugar_compare * -1} Grams Over Your Daily Recommended Sugar Range")

test_user = ["Jared", 1500, 140, 400, 90, 60, "fake directory"]
test_plan = ["Monday", [["penne alla vodka", 560, 25, 30, 9, 2], ["vodka tacos", 500, 19, 40, 15, 10], ["pulled steak", 450, 29, 31, 10, 5]]]
test_plan_two = ["Monday", [["penne alla vodka", 400, 25, 30, 9, 2], ["vodka tacos", 500, 19, 40, 15, 10], ["pulled steak", 450, 29, 31, 10, 5], ["penne alla vodka", 400, 25, 30, 9, 2], ["penne alla vodka", 400, 25, 30, 9, 2], ["penne alla vodka", 400, 25, 30, 9, 2]]]


us = User(test_user)
plan = Plan(test_plan)
us.compare(plan)



#Functions
def search_meal():
    with open("ReDefine Meals.csv", "r") as file:
        read = csv.reader(file)
        for row in read: redefine_meal_file.append(row)
    print("Opening CSV")
    meal_names = []
    for i in range(len(redefine_meal_file)):
        meal_names.append(redefine_meal_file[i][0])
    search = pyip.inputMenu(meal_names, numbered=True, prompt="Choose A Meal\n")
    meal_names.clear()
    for i in range(len(redefine_meal_file)):
        if redefine_meal_file[i][0] == search:
            meal_index = i
            break
    cl_meal = Meal(redefine_meal_file[meal_index])
    cl_meal.print_meal()

def search_plan():
    try:
        with open("Redefine Plans.pickle", "rb") as file:
            redefine_plan_file = pickle.load(file)
            file.close()
    except:
        print("No PKL File")
        return None
    try:
        plan_names = []
        for i in range(len(redefine_plan_file)):
            plan_names.append(redefine_plan_file[i][0])
        search = pyip.inputMenu(plan_names, numbered=True, prompt="")
        for i in range(len(redefine_plan_file)):
            if redefine_plan_file[i][0]==search:
                plan_index = i
                break
        cl_plan = Plan(redefine_plan_file[plan_index])
        cl_plan.print_plan()

    except:
        print("Something Went Wrong")


test_meal = ["penne alla vodka", 400, 25, 30, 9, 2]
test_meal_two = ["vodka tacos", 500, 19, 40, 15, 10]
test_meal_three = ["pulled steak", 450, 29, 31, 10, 5]
test_plan = ["Monday", [["penne alla vodka", 400, 25, 30, 9, 2], ["vodka tacos", 500, 19, 40, 15, 10], ["pulled steak", 450, 29, 31, 10, 5]]]
test_failed_plan = ["Monday", [["penne alla vodka", 500, 25, 35, 9, 2], ["vodka tacos", 500, 19, 40, 15, 10], ["pulled steak", 450, 29, 31, 10, 10]]]
test_failed_meal = 30

def plan_file_check():
    with open("Redefine Plans.pickle", "rb") as file:
        redefine_plan_file = pickle.load(file)
        file.close()
    print(redefine_plan_file)



