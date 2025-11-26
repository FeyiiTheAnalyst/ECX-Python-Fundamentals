#Student_Name = Olorode Feyisayo
import os
import random
from pprint import pprint
from collections import OrderedDict
import json
import math
'''Gets the CUrrent directory of the python file
creates an empty list called extensions'''
current_directory = os.getcwd()
extensions=[]
'''iterates through the list of items in current directory
if it's a file it joins it the path,directory and filename with the appropriate operator
creates a variable ext'''
for filename in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory,filename)):
        _,ext = os.path.splitext(filename)
        if ext:  # Add extension if it exists
            extensions.append(ext.lstrip('.'))
unique_extensions =set(extensions)
result_dict = {}
'''iterates through the set then assigns a random no to each elemnt 
between the range os 3-123
prints a dictionary with the random no as values'''
for ext in unique_extensions:
    random.seed(ext)
    random_number=random.randint(3,123)
    result_dict[ext]=random_number
random_sum = sum(result_dict.values())
no_of_files = len(os.listdir(current_directory))
if no_of_files > 1:
    log_result = math.log(random_sum,no_of_files)
else:
    log_result = 0

result_dict["result"] = round(log_result, 4)
ordered_result= OrderedDict(result_dict)


print(json.dumps(ordered_result,indent=4))