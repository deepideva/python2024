"""
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
"""
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
lifetime=int(90)
bal_life=lifetime-int(age)
bal_weeks= int(bal_life) * 52
#print(f"Your Balance Years are: {bal_life}, Your Balance Weeks are {bal_weeks}")
print(f"You have {bal_weeks} weeks left.")