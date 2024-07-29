# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
#print(names)
# 🚨 Remember to remove the print statement above when you submit.
names = names_string.split(", ")

import random

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
a = (names[random_choice])
print(f"{a} is going to buy the meal today!")


#Above code is perfectly worked in Aquarium