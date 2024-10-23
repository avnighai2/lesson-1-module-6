# take an input from a user if a user input is more then 1 letter than print the u=input is invalid else write an i condition to check if its a digit or an alphabet 

userinput = input(" Enter a singe character:")

if len(userinput) != 1:
    print("Invalid input. please enter only one character.")
else:
    if userinput.isdigit():
        print(f"{userinput} i a digit")
    elif userinput.isalpha():
        print(f"{userinput} is an alpha")
    else:
        print(f"{userinput} is not a digit or an alphabet")