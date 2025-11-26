# # Part 2: Implement login system
def login_system():
#     #  Define valid credentials
    VALID_USERNAME = "student123"
    VALID_PASSWORD = "pass123"
    attempt = 3 #No of attempts
    #WELCOME MESSAGE and user input
    print("Welcome to the Secure Login System!")    
    username = input("Enter Username:")
    password = input("Enter Password:")
    #input validation 
    if username and password .isalnum() or (username == VALID_USERNAME and password == VALID_PASSWORD):

            print("The Login details contains only letters and numbers!")
    else:
            print("The Login details contains invalid characters.")

    while attempt >0:
    #  password = input("Enter Password:")
     attempt -= 1     

     if username == VALID_USERNAME and password == VALID_PASSWORD:
        print(f"Acess Granted! Welcome {VALID_USERNAME}!")
        break
     elif username !=  VALID_USERNAME or password == VALID_PASSWORD:
        print (f"Incorrect Username. {attempt} attempts remaining.")
        username = input("Enter Username:")
     else :
        print(f"Incorrect password. {attempt} attempts remaining.")
        password = input("Enter Password:")
      
    if attempt == 0:
     print("Account locked! Too many failed attempts\nPlease contact administrator.")
    
#     # TODO: Initialize attempt counter

#     # TODO: Implement login logic with 3 attempts

#     # TODO: Add appropriate feedback messages
login_system()

# # Test your code
# if __name__ == "__main__":
#     print("Testing Part 1:")
#     print_numbers(15)

#     print("\nTesting Part 2:")
#     login_system()