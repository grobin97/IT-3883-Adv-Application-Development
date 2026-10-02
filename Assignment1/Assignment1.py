# Program Name: Assignment1.py
# Course: IT3883/Section 01
# Student Name: Gavin Robinson
# Assignment Number: Assignment 1
# Due Date: 09/22/2026
# Purpose: The purpose of this program is to have a string variable that can be viewed or editied by the user.
# List Specific resources used to complete the assignment.

input_buffer = "" # Starting variable. Kept empty for user to make changes.

while True: # Keeps the program running until option 4 is selected.
    (print("\nMenu: Please input a number 1-4.\n1. Append data to the input buffer."
    "\n2. Clear the input buffer.\n3. Display the input buffer.\n4. Exit the program.\n"))
    selection = input("Selection: ") # Selection input from the user.

    if(selection == "1"): # Option 1: Adds the inputed string to the input_buffer variable.
        new_append = input("Please enter a string: ")
        input_buffer += new_append

    elif(selection == "2"): # Option 2: Clears the input_buffer variable.
        input_buffer = ""
        print("\nThe input buffer has been cleared.")

    elif(selection == "3"): # Option 3: Displays the input_buffer variable.
        print("\n" + input_buffer)

    elif(selection == "4"): # Option 4: Quits the program.
        print("\nGoodbye.")
        break

    else: # Informs user if selection was invalid instead of just restarting the menu.
        print("\nInvalid selection. Please select a number between 1-4.")