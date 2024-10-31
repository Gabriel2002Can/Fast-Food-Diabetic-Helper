#Student Name: Luis Gabriel Stedile Portella
#Program Title: Fast Food for Diabetics
#Description: 

'''
The idea of the program is to give the user some fast food brand options, and the menu for these brands. Then the uses chooses which item it
will want and the program will calculate the amount of insulin that the user needs to take. If the user doesn't have a file containing
the insulin carbo ratio, the program will automatically ask for it. In the end of the program it will be prompt to the user a name for
a record file that will remember the items chosen and the nutrition facts for them.
'''

#importing some functions that will be used
import csv

#My function that is located in the root of the final project folder
import functions

def main():

    #Declaring some default variables
    total_insulin = 0
    total_carbo = 0
    highest_carbo = -1

    #Validators for looping purposes
    insulin_value_validator = False
    brand_repetition = False
    searching_validator = False

    #List with all wanted itens
    choosen_items = []

    #3d list of all options (and all data about them) of all brands
    all_options = [[],[],[],[],[],[]]
  
    #Listing brand options and expected outputs
    brand_options = ["McDonald's", "Burguer King", "Wendi's", "KFC", "Taco Bell", "Pizza Hut" ]
    number_options = [0, 1, 2, 3, 4, 5]

    print("\nWelcome! This is the Insulin calculator for fast foods dishes. The brands supported are: McDonald's, Burguer King, Wendi's, KFC, Taco Bell and Pizza Hut.\nThe program will ask you for your Insulin Carbohydrate Ratio (a number that describes the amount of grams of carbohydrates reduced by 1 unit of insulin), and it will keep your value for future use.\nYou will be prompt to select the brand of your dish; and after the number of your item. You can select as many items you wish.\nWhen you are finished the program will calculate the amount of insulin you will need to take for all the food eaten.")

    #File handling for the insulin carbo ratio

    #Will run if there is a insulin carbo ratio file already
    try:
        with open("insulin_ratio/insulin_to_carbohydrate_ration.txt","r") as insulin_file:

            #Is executed if there is no problem with the file
            try:

                #If there is a problem with the value of the file the program will prompt a warning
                insulin_ratio = int(insulin_file.read())
                if insulin_ratio <=0:
                    raise ValueError

            #Will alert with there is a problem with the file's value. If true the deletion of the program is needed! It ends the program right away
            except:
                print("\nYour insulin_to_carbohydrate_ration.txt file is corrupted! Please delete it and input your ratio again!\n")
                return
  
    #Will run if is necessary to create the insulin carbo ratio file
    except FileNotFoundError:
        with open("insulin_ratio/insulin_to_carbohydrate_ration.txt","w") as insulin_file:

            #Will loop until the insulin carbo ratio is a valid value
            while not insulin_value_validator:
                try:
                    insulin_ratio = int(input("\nWhat is your insulin to carbohydrate Ratio? "))
                    
                    #Will alert if there is problem with the value inputed
                    if insulin_ratio <= 0:
                        raise ValueError()
                    
                    #If the value is valid will end the loop and write the value in the file for future reference
                    insulin_file.write(str(insulin_ratio))
                    insulin_value_validator = True

                except ValueError:
                    print("Your value needs to be a positive and integer number!")

    #Opening and organizing options in CSV file
    with open("nutrition_table/FastFoodNutritionMenuV3.csv","r") as file_csv_reader:
        menu_options = csv.reader(file_csv_reader)

        #Dividing the food by brands
        for food in menu_options:
            if food[0] == "McDonald`s":
                all_options[0].append(food)
            elif food[0] == "Burger King":
                all_options[1].append(food)
            elif food[0] == "Wendy`s":
                all_options[2].append(food)
            elif food[0] == "KFC":
                all_options[3].append(food)
            elif food[0] == "Taco Bell":
                all_options[4].append(food)
            elif food[0] == "Pizza Hut":
                all_options[5].append(food)

    print()
    print("-"*150)
    print("-"*150)

    #Starting repetition of brand selection
    while not brand_repetition:
        choice_brand = -1
        brand_repetition = False
        itens_repetition = False

        #Listing the various options of brands for the user to chose from
        print("\nHello! Please, choose your brand!\n")
        print("-"*150)

        for option in brand_options:
            print(f"{brand_options.index(option)+1} - {option}")
        
        print("-"*150)
        print()

        #Looping until the brand name is valid!
        while not choice_brand in number_options:
            try:
                choice_brand = int(input())-1
                if not choice_brand in number_options:
                    raise ValueError()
            except:
                print("\nIt seems the number of the brand is incorrect! Please, choose a valid number: McDonald's (1), Burguer King (2), Wendi's (3), KFC (4), Taco Bell (5) or Pizza Hut (6)!\n")

        print("\n" + "-"*150)

        #Repetition of the itens part
        while not itens_repetition:
            input_validator = False
            counter = 1

            print(f"Here are the menu options for {brand_options[choice_brand]}\n")
            print("-"*150)

            #Listing all the options in the menu 
            for itens in all_options[choice_brand]:
                print(f"{counter} - {itens[1]}")
                counter += 1
            print("-"*150 + "\n")

            #Getting the item (list) wished
            while not input_validator:
                try:

                    #If conditions to fix loops
                    if not searching_validator and not brand_repetition:

                        #Main input function that will guide the action of the program
                        print("What is the number of the dish you will get? (Press 'S' to search for a specific item or keyword. Press 'B' to choose another brand. Type 'LEAVE' to quit the program) ")
                        current_choice = input()

                    #If the input is refering to the number of the Item
                    if current_choice.isdigit():
                        current_choice = int(current_choice)
                        
                        #Making sure the number is valid
                        if current_choice < 1:
                            raise ValueError("The value must be greater than 0!")
                        
                        #Getting and appending the value of the item selected 
                        current_choice = all_options[choice_brand][current_choice-1]
                        choosen_items.append(current_choice)
                        input_validator = True

                    #Fixing looping for the search function (described later)
                    if searching_validator:
                        itens_repetition = False
                        searching_validator = False
                        brand_repetition = False

                    #If the input is not a number (a command letter or a invalid input)
                    else:

                        #Searching option
                        if str.upper(current_choice) == "S":
                            counter_s = 1
                            search = input("\nYou can type a keyword to find the item you want! ")
                            print("\n" + "-"*150)

                            #Listing all menu items that have the desired keyword
                            for search_itens in all_options[choice_brand]:
                                if str.lower(search) in str.lower(search_itens[1]):
                                    print(f"{counter_s} - {search_itens[1]}")
                                
                                counter_s += 1
                            print("-"*150 + "\n")
                            
                            #Fixing looping values
                            brand_repetition = True
                            itens_repetition = True
                            searching_validator = True

                        #Going back to the brand selection 
                        elif str.upper(current_choice) == "B":
                            itens_repetition = True
                            input_validator = True

                        #Ending the program
                        elif str.upper(current_choice) == "LEAVE":
                            brand_repetition = True
                            itens_repetition = True
                            input_validator = True

                        #If the input value is invalid 
                        else:
                            raise TypeError("\nValue not valid! (Choose a number above 0, 'S' to search an Item, 'B' to go back to the brands or type LEAVE to exit the program!)\n")
                
                #Problems handling
                except TypeError as e:
                    print(e)
                except ValueError as e:
                    print(e)
                except:
                    print("Somenthing went wrong with your input! You need to insert the number of the dish you will want.\n")

            print()
    
    #Preparing the record file
    print("Select the name of the file that will record your items and the info about them.")
    destination_name = input()
    print()
    
    #Creating of the record file with desired name
    with open(f"Records/{destination_name}.txt","w") as record_file:
        record_file.write("*"*40)
        print("-"*150)       
        
        #Looping over each item selected earlier
        for each in choosen_items:
            try:

                #Making sure to avoid values being divided by 0
                if float(each[9]) == 0:
                    each[9] = 1

                #Doing some calculations with the insulin and carbo values
                insuline_taken = functions.insulin_calculator(each[9],insulin_ratio)
                total_insulin += insuline_taken
                total_carbo += float(each[9])

                #Getting the item that have the highest amount of carbo
                if float(each[9]) > highest_carbo:
                    highest_carbo = float(each[9])
                    highest_item = each[1]

                #Printing (and writing) informations about the individual items 
                print(f"- {each[1]} ({each[9]}g of carbohydates) from {each[0]}; It is suggested to take {insuline_taken} units of insulin!")
                record_file.write(f"\nItem: {each[1]} from {each[0]}\nCalories {each[2]}\nTotal fat {each[4]}g; Trans fat {each[6]}g\nCholsterol {each[7]}mg; Sodium {each[8]}mg\nCarbohydrates {each[9]}g; Insuline suggested: {insuline_taken} units\n" + "*"*40)
            
            except:
                
                #Error handling
                print(f"Something went wrong with the carbo value of {each[1]}!")
                record_file.write(f"\nSomething went wrong with the carbohydrate value of {each[1]}! (It may have 0g of carbohydrates!)\n")
                record_file.write("*"*40)
            
            print("-"*150) 
        
        #Printing and writing the total amount of carbo and insulin 
        print(f"\nThe total amount of Carbohydrates in this meal is {total_carbo}g. The recommended amount of insuline is {total_insulin} units.\n")
        record_file.write(f"\n\nThe total amount of Carbohydrates in this meal is {total_carbo}g. The recommended amount of insuline is {total_insulin} units.\n\n")

        #Showing the item with the highest amount of carbohydrate

        #Error handling
        try:
            print(f"{highest_item} ({highest_carbo}g of carbohydrate) is the item with the highest amount of carbohydrate, contributing with {functions.percentage_calculator_part_of_total(highest_carbo,total_carbo):.2f}% of the total carbo value.\n")
        except:
            print("Something went wrong with the program!\n")
            return
        
        record_file.write(f"{highest_item} ({highest_carbo}g of carbohydrate) is the item with the highest amount of carbohydrate, contributing with {functions.percentage_calculator_part_of_total(highest_carbo,total_carbo):.2f}% of the total carbo value.\n\n")
        
        #Warning if the carbohydrate amount is too high!
        if total_carbo > 200:
            print(f"Be cautious! The daily recommended amount of carbohydrates is 200g per day! Your quantity was {functions.percentage_calculator_above_recommended(total_carbo):.2f}% more than the daily recommendation!\n")
            record_file.write(f"Be cautious! The daily recommended amount of carbohydrates is 200g per day! Your quantity was {functions.percentage_calculator_above_recommended(total_carbo):.2f}% more than the daily recommendation!")

if __name__ == "__main__":
    main()