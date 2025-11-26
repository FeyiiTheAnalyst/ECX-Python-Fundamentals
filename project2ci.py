
#Student Name: Olorode Feyiasyomi


def print_numbers(n):
    for i in range(n): 
        if i == 10: #added extra = to make it a comparison
            break # stops the program if the condition is satisfied
        if i % 2 == 0:
           continue #skips to the next iteration if the condition is satisfied
        elif i % 3 == 0:
           pass # Has no effect
        else:
            print(i)
        
        
print_numbers(15)







# # Part 1: Debug this function
# def print_numbers(n):
#     # TODO: Fix all issues in this function
#     # Add comments explaining your fixes
#     for i in range(n):
#         if i % 2 == 0:
#             continue
#         elif i % 3 == 0:
#             pass
#         else:
#             print(i)
#         if i = 10:
#             break


# # Part 2: Implement login system
# def login_system():
#     # TODO: Define valid credentials
#     VALID_USERNAME = "student123"
#     VALID_PASSWORD = "__________"

#     # TODO: Initialize attempt counter

#     # TODO: Implement login logic with 3 attempts

#     # TODO: Add appropriate feedback messages


# # Test your code
# if __name__ == "__main__":
#     print("Testing Part 1:")
#     print_numbers(15)

#     print("\nTesting Part 2:")
#     login_system()