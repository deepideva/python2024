#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Easy Level
'''
password=""
#Imagin user give 4 for Letters
for char in range(1,nr_letters+1):
    password+= random.choice(letters)
for char in range(1,nr_symbols + 1):
    password+= random.choice(symbols)
for char in range(1,nr_letters + 1):
    password+= random.choice(numbers)
print("Your Password is :",password)
'''
pwd_list=[]
#Imagin user give 4 for Letters
for char in range(1,nr_letters+1):
    #pwd_list+= random.choice(letters)
    #can also use append
    pwd_list.append(random.choice(letters))
for char in range(1,nr_symbols + 1):
    pwd_list+= random.choice(symbols)
for char in range(1,nr_letters + 1):
    pwd_list+= random.choice(numbers)
print("Your Password is :",pwd_list)  # Will display just added all 
random.shuffle(pwd_list)
print("Your Password is :",pwd_list) # Will display Shuffled letters
# Now Output shows in List, We need to change and give just Characters
final_pwd=""
for i in pwd_list:
    final_pwd+=i
print(f"Your Password is : {final_pwd}" )

    