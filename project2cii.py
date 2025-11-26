# # # #student Name: Olorode Feyisayomi
# # # # # Part 2: Implement login system
# # # def login_system():
# # # #     #  Define valid credentials
# # #     VALID_USERNAME = "student123"
# # #     VALID_PASSWORD = "pass123"
# # #     attempt = 3 #No of attempts
# # #     #WELCOME MESSAGE and user input
# # #     print("Welcome to the Secure Login System!")    
# # #     username = input("Enter Username:")
# # #     password = input("Enter Password:")
# # #     #input validation 
# # #     if username and password .isalnum():
# # #        print("The Login details contains only letters and numbers!")
# # #     else:
# # #        print("The Login details contains invalid characters.")
# # # # Duration of the login system
# # #     while attempt >0:
# # #      attempt -= 1     
# # # #conditions to be satisfied
# # #      if username == VALID_USERNAME and password == VALID_PASSWORD:
# # #         print(f"Acess Granted! Welcome {VALID_USERNAME}!")
# # #         break #stops the enire loop
# # #      elif username !=  VALID_USERNAME or password == VALID_PASSWORD:
# # #         print (f"Incorrect Username. {attempt} attempts remaining.")
# # #         username = input("Enter Username:") #if  the first condition wasn't satisfied 
# # #         # goes ahead to check next condition 
# # #      else :
# # #         print(f"Incorrect password. {attempt} attempts remaining.")
# # #         password = input("Enter Password:") #if both conditions weren't satisfied perform this
      
# # #     if attempt == 0: #performs this after running out of attempt
# # #      print("Account locked! Too many failed attempts\nPlease contact administrator.")
    
# # # login_system()
# # x =int(input("Enter a number "))
# # # def factorial(x ,fact=1):
   
# # #    for i in range(1,x+1):
# # #         fact *= i
# # #    return fact
# # # result=factorial(x)
# # # print(result)  



# # # Custom Exceptions
# # # Create two custom exceptions here: e.g., InvalidInputError and DivisionByZeroError
# # class InvalidInputError(Exception):
# #     pass
# # # Basic Operations
# # # Write functions for add, subtract, multiply, and divide here

# # def addition(x,y):
# #     return x + y
# # def subtraction(x,y):
# #     return x - y
# # def multiplication(x,y):
# #     return x * y
# # def division(x,y):
# #     return x/y
# # # Advanced Operations
# # # Write functions for power, square root, and factorial (use recursion for factorial)

# # def power(base,exponent=3):
# #     return base ** exponent
# # def root(base,exponent = 0.5):
# #      return base ** exponent
# # def factorial(x):
# #     if x == 1:
# #        return 1
# #     else:
# #       return x * factorial(x-1)
    
# # # History Function
# # # Write a function to keep track of the last 5 calculations using *args

# # # Save Calculations
# # # Placeholder: Write a function to save calculations to a file using **kwargs



# # def calculator():
# #     print('''Welcome to Function Calculator
# # 1. Basic Operations
# # 2. Advanced Operations
# # 3. View History
# # 4. Save to File
# # 5. Exit
# # ''')
# #     user_input = int(input("select operation:"))
# #     if user_input == 1:
# #                 print('''Baisc Operations:
# #             1.addition
# #             2.subtraction
# #             3.division
# #             4.multiplication
# #             ''')
# #                 operation =int(input("Select Baisc operation(1-4):"))
# #                 x = float(input("Enter First number:"))
# #                 y = float(input("Enter Second number:"))
# #                 if operation == 1:
# #                    result = addition(x,y)
# #                 elif operation ==2:
# #                     result = subtraction(x,y)
# #                 elif operation == 3:
# #                     result = multiplication(x,y)
# #                 elif operation == 4:
# #                     result = division(x,y)
# #                 print(f"Result: {result}")
# #    #      except ValueError:
# #    #          print("Invalid input. Type a number")
# #    #  else:
# #    #      end        
    
# # """
# #     Main program for the calculator.
# #     Display a menu and call the appropriate functions based on user input.
# #     """
# #    # pass  # Replace with the main calculator logic

# # #if __name__ == "__main__":
# # calculator()
# # from newsapi import NewsApiClient
# # newsapi = NewsApiClient(api_key='ad82bd4fd4fc4061b2122ae119eabc7f')
# import requests
# response = requests.get('https://newsapi.org/v2/everything?q=apple&from=2025-01-26&to=2025-01-26&sortBy=popularity&apiKey=ad82bd4fd4fc4061b2122ae119eabc7f', auth=('olorodefeyisayomi', 'feyisayo'))
# #  = newsapi.get_top_headlines(q='bitcoin',
# #                                            sources = 'bbc-news,the-verge',
# #                                            category ='business',
# #                                            language='en',
# #                                            country='us')
# # all_articles = newsapi.get_everything(q='bitcoin',
# #                                        sources='bbc-news,the-verge',
# #                                        domains='bbc.co.uk,techcrunch.com',
# #                                        from_param='2017-12-01',
# #                                        to='2017-12-12',
# #                                        language='en',
# #                                        sort_by='relevancy',
# #                                        page=2)
# # sources = newsapi.get_sources()


# print(response.status_code)
print([3,5,5,4])
print("hell" + " " +"vde")