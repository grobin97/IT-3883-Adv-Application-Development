# Program Name: Assignment2.py
# Course: IT3883/Section 01
# Student Name: Gavin Robinson
# Assignment Number: 2
# Due Date: 10/02/2026
# Purpose: The purpose of this program is to read an input file with names and grades, calculate the average,
#          and return the names and averages sorted from highest to lowest.
# List Specific resources used to complete the assignment.

results = [] # List will be used to store the name and averages

with open("Assignment2/Assignment2input.txt") as file: # Opens the input file

    for line in file: # Loops through each line in the input file
        part = line.split() # Creates a list of each piece of data seperated by a space
        name = part[0]  # First part of each line is the name
        scores = (float(score) for score in part[1:]) # The rest are scores stored as floats

        total = 0
        length = 0
        for i in scores: # Adds the scores from each line together
            total += i
            length += 1 # A length value in cases where the amount of scores differ

        average = total / length # Calculates the average
        average = round(average, 2) # Rounds to two decimal places
    
        results.append((name, average)) # Adds the name and their average to a new list

def get_average(results): # Function to return the average result
    return results[1]

results.sort(key = get_average, reverse = True) # Sorts the list from highest to lowest average

for name, average in results: # Prints the results
    print(name, average)