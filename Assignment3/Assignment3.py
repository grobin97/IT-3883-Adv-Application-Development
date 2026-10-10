# Program Name: Assignment3.py
# Course: IT3883/Section 01
# Student Name: Gavin Robinson
# Assignment Number: Assignment 3
# Due Date: 10/10/2026
# Purpose: The purpose of this program is to create a GUI to convert Miles per Gallon to Kilometers per Liter.
# List Specific resources used to complete the assignment.

# Imports the tkinter library and gives it the shorter name tk.
import tkinter as tk

# Creates a function that converts mpg to kpl. 
def convert():
    try:
        mpg = float(mpg_entry.get())
        kpl = mpg * 0.425143707
        answer_label.config(text=round(kpl, 2))

    # Keeps the answer blank until a number that can be converted is entered.
    except ValueError:
        answer_label.config(text="")

# Creates the GUI window, adds a title to the window, and sets the size.
window = tk.Tk()
window.title("Miles per Gallon to Kilometers per Liter Converter")
window.geometry("500x360")

# Creates a lable to tell the user what value to input.
window_label = tk.Label(window, text="Miles per Gallon:")
window_label.pack()

# Creates a text entry box where the user can type in an input.
mpg_entry = tk.Entry(window)
mpg_entry.pack()

# Creates a lable for the output in kpl.
window_label = tk.Label(window, text="Kilometers per Liter:")
window_label.pack()

# Creates an empty lable where the output will be dislplayed.
answer_label = tk.Label(window, text="")
answer_label.pack()

# Runs the convert function everytime the program detects a key being released.
mpg_entry.bind("<KeyRelease>", lambda event: convert())

# Keeps the GUI window open and waits for input.
window.mainloop()