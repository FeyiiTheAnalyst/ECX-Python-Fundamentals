1# Student Name:Olorode Feyisayomi
# Create two custom exceptions here: e.g., InvalidInputError and DivisionByZeroError
class InvalidInputError(Exception):
    pass
class DivisionByZero(Exception):
    pass
# Basic Operations
# Write functions for add, subtract, multiply, and divide here

def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
'''If the second argument is 0 it raises a divisionbyZero Error'''
def division(x,y):
    if y == 0:
        raise DivisionByZero("Cannot divide a number by Zero")
    return x/y
# Advanced Operations
# Write functions for power, square root, and factorial (use recursion for factorial)

def power(base,exponent=3):
    return base ** exponent
def root(base,exponent = 0.5):
     '''assert ensures a negative num is not inputed'''
     assert base >= 0,"Cannot find the root of a -ve no "
     return base ** exponent
def factorial(x):
    if x < 0:
        raise InvalidInputError("cannot find factorial of a decimal or negative number")
    if x == 1:
       return 1
    else:
      return x * factorial(x-1)
    
# History Function
# Write a function to keep track of the last 5 calculations using *args
'''creates an empty history list
using the *args parameter to accept all arguments
also using the global keyword so the history_list variable can be called outside the history function
adds each element from the args tuple to the history_list
Prints the Last 5 Calculations'''
history_list = []
def history(*args):
    global history_list
    history_list.extend(args)
    history_list = history_list [-5:]
    
# Save Calculations
# Placeholder: Write a function to save calculations to a file using **kwargs
'''filename="calculations.txt": Sets a default filename if none is provided.
**kwargs: Accepts multiple key-value pairs, which are stored as a dictionary.
file.write(f"{kwargs}\n"): Writes the dictionary (kwargs) to the file as a string.
Print Statement: Informs the user that the calculation has been saved.'''
def save_to_file(filename="calculations.txt", **kwargs):
    with open(filename, "a") as file:
        file.write(f"{kwargs}\n")
    print(f"Calculation saved to {filename}.")



def calculator():
    print('''Welcome to Function Calculator
1. Basic Operations
2. Advanced Operations
3. View History
4. Save to File
5. Exit
''')
    while True:
        try:
            user_input = int(input("select operation:"))
            if user_input < 1 or user_input > 5:
                print("Invalid input. Please choose a valid operation between 1 and 5.")
                continue  # Prompt the user again
            if user_input == 1:
                print('''Baisc Operations:
            1.addition
            2.subtraction
            3.multiplication
            4.division
            ''')
                operation =int(input("Select Baisc operation(1-4):"))
                x = float(input("Enter First number:"))
                y = float(input("Enter Second number:"))
                if operation == 1:
                   result = addition(x,y)
                   print(f"result:{result:.3f}")
                   history(result)
                elif operation ==2:
                    result = subtraction(x,y)
                    print(f"result:{result:.3f}")
                    history(result)
                elif operation == 3:
                    result = multiplication(x,y)
                    print(f"result:{result:.3f}")
                    history(result)
                elif operation == 4:
                    result = division(x,y)
                    print(f"result:{result:.3f}")
                    history(result)
                else:
                    raise InvalidInputError("Invalid Operation Selected")
                
            elif user_input == 2:
                print('''Advanced Operations:
            1.Power
            2.Root
            3.Factorial
            ''')
                operation =int(input("Select Advanced Operations:"))
                if operation == 1:
                    x = float(input("Enter base number:"))
                    y = float(input("Enter exponent number:"))  
                    result= power(x,y)
                    print(f"result:{result:.3f}")
                    history(result)
                
                elif operation == 2:  # Root
                    x = float(input("Enter the number to find the root of: "))
                    if x < 0:
                         raise InvalidInputError("Cannot find the root of a negative number.")
                    result = (lambda x: x ** 0.5)(x)  # Execute the lambda with `x`
                    print(f"Result: {result:.3f}")
                    history(result)
                elif operation == 3:
                    x = int(input("Enter a non-negative integer for factorial:"))
                    result = factorial(x)
                    print(f"result:{result:.3f}")
                    history(result)
                else:
                    raise InvalidInputError("Invalid Operation Selected")
            elif user_input == 3:
                if history_list:  # Check if history is not empty
                    print("Last 5 calculations:")
                for idx, calc in enumerate(history_list, start=1):
                        print(f"{idx}. {calc}")
                else:
                    print("No calculations in history yet.")
                
            elif user_input == 4:
                print("Saving all calculations to file...")
                for calc in history_list:
                    save_to_file(calculation=calc)
                print("All calculations saved.")
            elif user_input == 5:
                print("Exiting calculator.")
                break        
        except ValueError:
            print("Invalid Menu Selection")
        except InvalidInputError as e:
            print(f"Error: {e}")
        except DivisionByZero as e:
            print(f"Error: {e}")

          
    
"""
    Main program for the calculator.
    Display a menu and call the appropriate functions based on user input.
    """
   # pass  # Replace with the main calculator logic

if __name__ == "__main__":
  calculator()