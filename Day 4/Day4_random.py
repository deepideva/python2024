import random
random_int = random.randint(10,20)
#random() to create float numbers between 0 to 1 by default
#random_float = random.random()
#I need any float numbers for 2 to 5, How to define ? follow below.. No direct definition , we need to Multiple and get only
random_float = random.random()*5
print(random_int)
print(random_float)

# likewise, we can print Love calculation
random_love=random.randint(1,100)
print(f"Your Love score if {random_love}")