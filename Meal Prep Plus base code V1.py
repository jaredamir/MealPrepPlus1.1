import csv


# welcome: make new meal plan, read previous one[edit a meal, search for a meal]
# need to add a sub section for ingridents in meal
# need to add a section for goals

print("Welcome to Meal Planner")
i = 1
while i < 100000000:
    choice_1 = input('(1) Make A New Meal Plan ' '\n' '(2) Open Existing Planner ' '\n' '(3) Quit' '\n')
    if choice_1 == "1":
        print('Enter Meal Details')

        with open('MealPlan - Sheet1V2.csv',
                  'w+') as file:  # 'w+' is to write to the file (this creates and overwrites a filee)
            Meals = csv.writer(file)  # .writer instead of reader
            Meals.writerow(["meal_name", "calories", "protein", "carbs", "fats"])  # making the headers

            numMeals = int(input('How Many Meals?: '))
            for i in range(numMeals):
                meal_name = input('Meal ' + str(i + 1) + ' Name: ')  # str(i + 1) increases the number after each loop
                calories = input('Total Calories: ')
                protein = input('Grams of Protein: ')
                carbs = input('Grams of Carbs: ')
                fats = input('Grams of fats: ')
                # MAKE FAILSAFE FOR NON INT INPUTS

                Meals.writerow([meal_name, calories, protein, carbs, fats])

            print('Thank You!, Saving Details...')




    elif choice_1 == '2':
        print('loading Meal Plan')

        MealList = []
        with open('MealPlan - Sheet1V2.csv', 'r') as file:
            Meals = csv.reader(file)
            for row in Meals:
                MealList.append(row)  # using empty variable to make a 2d list
        # in this layout, theres a list inside a list so for[0][1], [0] gets the section in positon 0 and [1] gets the second item in that section
        print('Meal Plan')
        for i in range(len(MealList)):
            print('Meal ' + str(i) + ': ' + str(MealList[i]))

        # Summing Macros
        sum_calories = 0
        sum_protein = 0
        sum_carbs = 0
        sum_fats = 0
        for i in range(1, len(MealList)):
            sum_calories += int(MealList[i][1])
            sum_protein += int(MealList[i][2])
            sum_carbs += int(MealList[i][3])
            sum_fats += int(MealList[i][4])
        print("Total: " + "Calories " + str(sum_calories) + " Protein " + str(sum_protein) + " Carbs " + str(
            sum_carbs) + " Fats " + str(sum_fats))

        # Main Menu
        while i < 100000000:
            edit_choice = input('(1) Edit Meal' '\n' '(2) Add Meal to List \n' '(3) Close & Return to Main Menu''\n')

            # Edit Meals
            if edit_choice == '1':
                editMeal = int(input('Which Meal Would You like to Change? ' + "1-" + str(len(MealList) - 1) + '\n'))

                for i in range(len(MealList[0])):
                    newMeal = input('Enter New Meal Details for ' + str(MealList[0][i]) + '\n')
                    MealList[editMeal][i] = newMeal

                print('New Meal Details')
                for i in range(len(MealList)):
                    print('Meal ' + str(i) + ' :' + str(MealList[i]))
                while i < 100000000:
                    changesMealPlan = input('Would You Like to Save This Meal? Y/N \n').lower()
                    # ADD SUMS!!!!!
                    if changesMealPlan == ('y'):
                        with open('MealPlan - Sheet1V2.csv', 'w+') as file:
                            Meals = csv.writer(file)
                            for i in range(len(MealList)):
                                Meals.writerow(MealList[i])
                        print('Changes Saved')
                        break
                    elif changesMealPlan == ('n'):
                        print('Okay Changes Not Saved')
                        break
                    else:
                        print('Please Type y or n')

            # Adding to List

            elif edit_choice == '2':
                with open('MealPlan - Sheet1V2.csv',
                          'a') as file:  # 'w+' is to write to the file (this creates and overwrites a filee)
                    Meals = csv.writer(file)  # .writer instead of reader

                    numNewMeals = int(input('How Many Meals Are You Adding?: \n'))
                    for i in range(numNewMeals):
                        meal_name = input(
                            'Meal ' + str(i + 1) + ' Name: ')  # str(i + 1) increases the number after each loop
                        calories = input('Total Calories: ')
                        protein = input('Grams of Protein: ')
                        carbs = input('Grams of Carbs: ')
                        fats = input('Grams of fats: ')

                        # FIX

                        save_NewMeal = input('Would You Like to Save New list? Y/N\n').lower()
                        while i < 100000:
                            if save_NewMeal == 'y':
                                Meals.writerow([meal_name, calories, protein, carbs, fats])
                                print('New Meal Added, Thank You!')
                                break

                            elif save_NewMeal == 'n':
                                print('Cancelling New Meal')
                                break

                            else:
                                print('Invalid Input')

                """"        
                for i in range(len(MealList[0])):
                    addedMeal = input(str(MealList[0][i+1]) + '\n')
                with open('MealPlan - Sheet1V2.csv', 'a') as file:
                    Meals = csv.writer(file)
                    Meals.writerow(MealList[i+1])
                """

            elif edit_choice == '3':
                print('Closing')
                break

            else:
                print('Invalid input')




    elif choice_1 == '3':
        print('Closing Program, Thank You')
        break


    else:
        print('Invalid Input')

# for column in Meals + 1, sum

