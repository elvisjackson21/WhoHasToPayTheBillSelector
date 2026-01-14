import random

names = []
name = ""
adding_names = True
number_of_names = 1

def name_selection(the_names):
    selected_name = random.choice(the_names)
    the_names.remove(selected_name)
    print(f"{selected_name} is paying the bill!")
    print(', '.join(the_names) + " you all got lucky!")

def has_numbers(input_string):

    return any(char.isdigit() for char in input_string)

print("Let see who is picking up the bill")
while adding_names:
    name = input(f"Type in name {number_of_names}: ")
    if has_numbers(name):
        name = input(f"Invalid input type in name {number_of_names}: ")
    elif not has_numbers(name):
        names.append(name.upper())
    continue_add = input(f"{number_of_names} added would you like to add more? (y/n): ")
    if  continue_add.lower() == "y":
        number_of_names += 1
        adding_names = True
    elif continue_add.lower() == "n":
        print("Lets see who is picking up the bill")
        name_selection(names)
        adding_names = False
    else:
        print("Invalid input, please enter y or n")

