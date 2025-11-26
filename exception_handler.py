# #Student Name: Olorode Feyisayomi
# # Custom Exceptions
# # Create at least two custom exceptions, e.g., FileNotFoundErrorCustom and InvalidInputError
# class InvalidInputError(Exception):
#     pass
# class FileNotFoundErrorCustom(Exception):
#     pass

# # Demonstrate File Handling
# # Write a function to handle file reading (use a try-except block)
# def read_file(file_name):
#     """
#     Reads the content of a file. Creates the file if it doesn't exist.
#     """
#     try:
#         with open(file_name, "r") as file:
#             content = file.read()
#             print("File content:")
#             print(content)
#     except FileNotFoundError:
#         print("Error: File not found. Creating a new file...")
#         with open(file_name, "w") as file:
#             file.write("This is a new file created by the program.\n")
#         raise FileNotFoundErrorCustom(f"{file_name} was not found. A new file has been created.")


# # Demonstrate Calculations
# # Write a function to perform calculations with input validation (use try-except and assert)
# def calculation():
#     num1 = input("Enter the first number:")
#     try:
#         num1 = float(num1)
#     except:
#         raise InvalidInputError("Invalid input. Please enter a number.")
#     num2 = input("Enter the second number:")
#     try:
#         num2 = float(num2)
#     except:
#         raise InvalidInputError("Invalid input. Please enter a number.")
#     try:
#         operator = input("Enter an operator (+, -, *, /): ")
#         if operator not in ["+", "-", "*","/"]:
#             raise InvalidInputError("Invalid operator. Please enter one of +, -, *, /.")
    
#         if operator == "+":
#             result = num1 + num2
#         elif operator == "-":
#             result = num1 - num2
#         elif operator == "*":
#             result = num1 * num2
#         elif operator == "/":
#             assert num2 != 0 ,"Cannot divide by zero"
#             result = num1/num2
#         assert result is not None, "Calculation failed due to an unknown error."
#         print(f"Result: {result}")
#     except InvalidInputError as e:
#         print(f"Error: {e}")
#     except ZeroDivisionError as e:
#         print(f"Error: {e}")
#     except AssertionError as e:
#         print(f"AssertionError: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")



# def main():
#     """
#     Main program for exception handling demo.
#     Call functions to demonstrate various exception scenarios.
#     """
#     print("Exception Handling Demo")
#     print("1. File Handling")
#     print("2. Perform Calculations")
#     print("3. Exit")
    
#     while True:
#         try:
#             choice = input("Enter your choice: ")
#             if choice == "1":
#                 file_name = input("Enter the file name to read: ")
#                 read_file(file_name)
#             elif choice == "2":
#                 calculation()
#             elif choice == "3":
#                 print("Exiting the program.")
#                 break
#             else:
#                 print("Invalid choice. Please select 1, 2, or 3.")
#         except FileNotFoundErrorCustom as e:
#             print(f"Custom Exception: {e}")
#         except Exception as e:
#             print(f"An unexpected error occurred in the main program: {e}")
#         finally:
#             print("Returning to the main menu...")

#     pass  # Replace with the main exception handling logic

# if __name__ == "__main__":
#     main()
#file = open("example.txt","r")
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: An I/O error occurred while reading the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")