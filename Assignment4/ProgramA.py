# Program Name: ProgramA.py
# Course: IT3883/Section 01
# Student Name: Gavin Robinson
# Assignment Number: Assignment 4
# Due Date: 11/06/2026
# Purpose: Take a string from a user input to send to ProgramB and then listens for the response and prints what was recived.
# List Specific resources used to complete the assignment.

import socket

# Create a TCP socket
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Connect to Program B
s.connect(("127.0.0.1", 50000))

# Takes input from the user and stores it as a variable
message = input("Enter a string: ")

# Encode and sends the message
byte_array = message.encode('utf-8')
s.sendall(byte_array)

# Prints the response from Program B
print(s.recv(256).decode('utf-8'))

# Closes the connection
s.close()