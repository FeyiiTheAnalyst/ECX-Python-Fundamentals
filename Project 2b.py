# Student Name: Olorode Feyisayomi

# Welcome message

def heartrate(pulse):
    if pulse < 60:
        print("Bradycardia")
    elif pulse > 100:
        print("Tachycardia")
    else :
        print("Normal")


pulse = [55,75,80]
for i in pulse:
    heartrate(i)
# print("Welcome to the Multiplication Table Generator!")

# # TODO: Get input from user and convert to integer
# number = int(input("Enter a number:"))

# # TODO: Print header for multiplication table
# print(f"\nMultiplication Table for {number}:")
# # # TODO: Create a loop that runs from 1 to 25
# for value in range(1, 26, +1):
#     # stores answer of multiplication into variable result 
#     result = value * number
#     # # TODO: Use string formatting to align all numbers properly
#     print(f"{value:<4} X  {number:<7} ={result:>10}")
# # Display completion message
# print("\nThe End")
