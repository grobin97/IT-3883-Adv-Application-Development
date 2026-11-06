# Program Name: ProgramB.py
# Course: IT3883/Section 01
# Student Name: Gavin Robinson
# Assignment Number: Assignment 4
# Due Date: 11/06/2026
# Purpose: Listens for a string from ProgramA, takes the recived string and converts it to all uppercase and sends it back.
# List Specific resources used to complete the assignment.

import socket

# Create a TCP socket
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Assign an IP address and port
s.bind(("127.0.0.1", 50000))

# Listen for a connection
s.listen()

# Accept a connection
conn, addr = s.accept()

# Receive the message and convert bytes to text
data = conn.recv(256)
message = data.decode('utf-8')

# Convert the message to all upper case letters
message = message.upper()

# Sends the uppercase message back
conn.sendall(message.encode())

# Close the connection
s.close()