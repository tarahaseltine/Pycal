import re # Adding this at the top of the file to utilize regex later on in the file

print("Welcome to Pycal!") # This welcomes the user to the calculator
print("Type 'quit' to exit\n") # Prompts the user to type 'quit' if they want to exit the calculator and then ends with creating a new line

previous = 0 # This indicated that our math will star at 0
run = True # This sets the variable 'run' to the bolean True

def performMath(): # Defining a class to perform our mathamatic equation
    global run # This allows us to use the global variable run and previous within our class
    global previous
    equation = input("Enter equation:") # We are asking the user for their own input and saving whatever they type to the variable 'equation'
    if equation == 'quit': # This block states thaf if the user types quit, the run boolean then changes to False and the program stops running
        run = False
    else: # If the user types anything other than quit, this block of code will run
        equation2 = re.sub('[a-zA-Z,.:()" "]', '', equation) # Using regex, we are sating whatever that if equation has any of the letters or characters mentioned in the first '', it will be replaced by what is in the second '', then its being saved into the vailable equation2
        previous = eval(equation2) # We are then evaluating equation2 and saving that answer under previous

        print("you typed", previous) # Then we are printing the value of previous

while run: # As long as the program is running, coninue to run the performMath() block of code. 
    performMath()
