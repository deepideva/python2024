# print(8/3)
# By using Round, we can round off the value
#print(round(8/3))
#Also, we can use just int and round it
# print(int(8/3))
# above output is just 2

#To do specific rounding, try below
print(round(8 / 3 ,2))
print(round(8 / 3 ,4))
print(round(8 / 3 ,7))

#we can use // also instead putting round function
print(8//3)

#Storing variable and re using , 
result = 4/2
#now in above script result value should be 2.... Instead calling result again , we can use like below
result /=2
print(result) #This output will be 1.0, Like wise we can use all below
"""
result +=2
result -=2
result *=2
result /=2
Lets see another example
"""
score=0 #default score is 0
score+=1
print("Your Score is :",score)   # Output- Your Score is : 1



