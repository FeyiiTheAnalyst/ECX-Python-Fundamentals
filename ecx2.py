#Olorode Feyisayo
print("Temperature Converter")#displays the string as an output
temp_in_celsius=input("Temperature in °C:" ) #user is required to respond to input question which is stored in variable temp_in_celsius as a string
temp_in_celsius=int(temp_in_celsius) #converts value inputed into an integer
temp_in_faren=int((temp_in_celsius * 1.8) + 32) #stores temp_in_faren as 32 + (temp_in celsius multiplied by 1.8) as an integer
print(f"The temperature equivalent of {temp_in_celsius} °C in Farenheit is {temp_in_faren} °F. \nThanks for using my little program!") #displays the string concatenated with the f-string function,then display the string after\n on a new line