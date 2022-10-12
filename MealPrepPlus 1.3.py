import csv
import pyinputplus as pyip
ing_list=[]
meals_file =[]
units_list= ["tbsps", "tsps", "cups", "grams", "lbs", "oz", "Liters", "other"]

#ingredient (name, amount per serving, unit of serving, calories, protein, carbs, fats, sugar)
with open("Ingredients.csv", "r") as file:
    read = csv.reader(file)
    for row in read:
        ing_list.append(row)

with open("Meallist.csv", "r") as file:
    read = csv.reader(file)
    for row in read:
        meals_file.append(row)
class Ingredient:
    def __init__(self, name, amount, unit, cal, pro, fats, carb, sugar):
        self.name = name
        self.amount = amount
        self.unit = unit
        self.cal = cal
        self.pro = pro
        self.carb=carb
        self.fats=fats
        self.sugar=sugar

    def save(self):
        print("Saved!")
        ing_list.append([self.name,self.amount, self.unit, self.cal, self.pro, self.carb, self.fats, self.sugar])
        with open("Ingredients.csv", "w",  newline="") as file:
            write=csv.writer(file)
            for item in ing_list: write.writerow(item)
        # csv_file.append(self.name, self.cal, self.pro)


def new_ing():  # update
    while True:
        check=[]
        for i in range(len(ing_list)):
            check.append(ing_list[i][0])
        while True:
            name= input("Ingredient Name\n")
            if name in check:
                print(f"{name} is already in the list")
            else:
                break

        unit = pyip.inputMenu(units_list, "Unit of Measurment for Serving Size\n", numbered=True,)
        if unit == "other":
            unit=input("Name of Unit\n")
        amount = pyip.inputFloat(f"Amount of {unit} per Serving\n")
        cal = pyip.inputFloat("Calories per serving\n")
        pro = pyip.inputFloat("Grams of Protein per Serving\n")
        carb= pyip.inputFloat("Grams of Carbs per serving\n")
        fats =pyip.inputFloat("Grams of Fats per serving\n")
        sugar=pyip.inputFloat("Grams of Sugar per serving\n")


        #ing = Ingredient(name, cal, pro)
        print(f"\n{name}\n"
              f"Serving Size: {amount} {unit}\n"
              f"{cal} Calories per Serving\n"
              f"{pro} G of Protein per Serving\n"
              f"{carb} G of Carbs per Serving\n"
              f"{fats} G of Fats per Serving\n"
              f"{sugar}G of Sugar per Serving\n"
                )

        save = pyip.inputYesNo("would you like to save?\n")
        if save == "yes":
            cl_ing=Ingredient(name, amount, unit, cal, pro, carb, fats, sugar)
            cl_ing.save()
        if save == "no":
            print("not saved")
        cont = pyip.inputYesNo("Add another?\n")
        if cont == "yes":
            pass
        if cont == "no":
            break


def search_ing():
    search = input("ingredient name\n")
    for i in range(len(ing_list)):
        if ing_list[i][0] == search:
            s_ing=ing_list[i]





#Meals
class Meal:
    def __init__(self, name, cal, pro, carb, fats, sugar, ingredients):  # make  child class
        self.name = name
        self.cal = cal
        self.pro = pro
        self.carb = carb
        self.fats = fats
        self.sugar = sugar
        self.ings = ingredients
    def save(self):
        full_meal=[self.name,0,0,0,0,0,self.ings] #FIXXXX
        with open("Meallist.csv", "w") as file:
            writer = csv.writer(file)
            for item in meals_file: writer.writerow(item)


    def print(self):
        print(f"{self.name}")
        for i in range(len(self.ings)):
            print(f"    {self.ings[i][1]} {self.ings[i][2]} of {self.ings[i][0]}")
        print(f"calories: {self.cal} Protein: {self.pro}")

def new_meal():
    meals_file = []
    full_meal= []

    with open("Meallist.csv", "r") as file:
        read = csv.reader(file)
        for row in read:
            meals_file.append(row)
    print(meals_file)
    meal_list = []
    meal_ings=[]
    meal_name = input("Meal Name\n")
    meal_list.append([meal_name,0,0,0,0,0])
    while True:
        search = input("ingredient name\n")
        for i in range(len(ing_list)):
            if ing_list[i][0] == search:
                ning = ing_list[i]
                name = ning[0]
                unit = ning[2]
                cal = float(ning[3])
                pro = float(ning[4])
                carb = float(ning[5])
                fats = float(ning[6])
                sugar = float(ning[7])


                ing_amount = float(input(f"How Many {unit} Are You Adding?\n"))
                serv = float(ning[1])
                fac = ing_amount / serv
                new_cal = cal * fac
                new_pro = pro * fac
                new_carb = carb * fac
                new_fats = fats * fac
                new_sugar = sugar * fac
                print(f"{ing_amount} {unit}\nCalories: {new_cal} Protein: {new_pro} Carbs: {new_carb} Fats: {new_fats} Sugar: {new_sugar}")
                up_ing = [name,ing_amount,unit,new_cal,new_pro,new_carb,new_fats,new_sugar]
                print(up_ing)
                add = pyip.inputYesNo("would you like to add? (y/n)\n")
                if add == "yes":
                    meal_ings.append(up_ing)
                    meal_list.append(up_ing)
                    print(meal_list)
                    cont= pyip.inputYesNo("Add Another Ingredient?\n")
                    if cont=="yes":
                        pass
                    if cont=="no":
                        save_meal=pyip.inputYesNo("Would you Like to save Meal?\n")
                        if save_meal =="yes":
                            full_meal.append(meal_list)
                            print(full_meal)
                            meals_file.append(full_meal)
                            print(meals_file)
                            with open("Meallist.csv", "w") as file:
                                writer=csv.writer(file)
                                for item in meals_file: writer.writerow(item)
                            print("Saved!")
                            break
                        if save_meal=="no":
                            print("Not Saved")
                            break
                if add == "no":
                    print("not added")

new_meal()
test_meal = [
    [['chicken and rice', 0, 0, 0], ['chicken', 150.0, 'grams', 300.0, 60.0], ['rice', 0.5, 'cups', 100.0, 7.5]],
    [['ham sandwich', 0, 0, 0], ['ham', 30.0, 'grams', 225.0, 25.5], ['bread', 2.0, 'slices', 200.0, 30.0]]
]


real_test_meals = [['chicken and rice',0,0,0],['chicken',150.0,'grams',300.0,60.0,80.0,20.0,2.0],['rice',0.5,'cups',100.0,7.5,20.0,10.0,15.0]]

def open_meal():
    cal = 0
    pro = 0
    carb = 0
    fats = 0
    sugar = 0
    ing_list = []
    meallist = []
    with open("Meallist.csv", "r") as file:
        read = csv.reader(file)
        for row in read: meallist.append(row)
        print(meallist)
    search = input("meal name?\n")
    for i in range(len(meallist)):
        #print(meallist[i][0][0])
        if search == meallist[i][0][0]:
            op_meal = meallist[i]
            name = meallist[i][0][0]  # need to open and append to a list upon running
            lex = (len(op_meal))

            # cal
            for i in range(lex):
                if i == 0:
                    pass
                else:
                    cal += float(op_meal[-i][3])
            # pro
            for i in range(lex):
                if i == 0:
                    pass
                else:
                    pro += float(op_meal[-i][4])
            #carb
            for i in range(lex):
                if i == 0:
                    pass
                else:
                    carb += float(op_meal[-i][5])
            #sugar
            for i in range(lex):
                if i == 0:
                    pass
                else:
                    fats += float(op_meal[-i][5])
            # fats
            for i in range(lex):
                if i == 0:
                    pass
                else:
                    sugar += float(op_meal[-i][6])
            # class
            for i in range(lex):
                if i == 0:
                    pass
                else:
                    ing_list.append([op_meal[-i][0], op_meal[-i][1], op_meal[-i][2]])
            print(ing_list)
            global cl_meal
            cl_meal = Meal(name, cal, pro, carb, fats, sugar, ing_list)
            cl_meal.print()


while True:
    #Menu
    menu_select = pyip.inputNum(min=1, max=3, prompt="(1) Add Ingredient\n(2) Add Meal\n(3) New Meal Plan\n")
    if menu_select == 1:
        new_ing()
    if menu_select == 2:
        new_meal()
    if menu_select == 3:
        print("test")
