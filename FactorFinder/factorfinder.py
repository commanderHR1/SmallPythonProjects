import math
import sys

while True: # Main program loop
    # Gets input
    print("Enter a positive whole number to factor (or QUIT):")
    response = input("> ")
    if (response.lower() == "quit"):
        sys.exit()
    
    # Tests input
    if not (response.isDecimal() and int(response) > 0):
        continue
    number = int(response)
    
    factors = []
    
    # Find the factors of input number
    