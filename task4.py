#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
You will need to use a logical statement that checks to see if any of the names
matches the input name.  Don't be surprised if there are many and/or connectors.

(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""
name = input("enter your name: ")
'''
VIPNames = ("Guile","Blanka","Christine","Carol","Richard","Daniel","Chun-Li")
VIPNamesLowCase = ("guile","blanka","christine","carol","richard","daniel","chun-li")

if name in VIPNames or name in VIPNamesLowCase:
    print(f"Hi {name}! You are a VIP!")
else:
    print('You are not a VIP.')

'''

if name == "Guile" or name == "guile" or name == "Blanka" or name == "blanka" or name == "Christine" or name == "christine" or name == "Carol" or name == "carol" or name == "Richard" or name == "richard" or name == "Daniel" or name == "daniel" or name == "Chun-Li" or name == "chun-li":
    print(f"Hi {name}! You are a VIP!")
else:
    print("You are not a VIP.")