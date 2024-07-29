# Fstring is , We can call multiple variables, no need to define String, int or Boolean for each variables, lets see
score=0
height=1.8
iswinning=True

print("Your Score is "+ str(score) + " " +str(height) + " " + str(iswinning))
print("Above Output is Regular process\n")
print("\n")
#Above is normal method, As alternate we can use F string like below...... just put f before double or single quotes
print("Now try same using F string")
print(f"Your Score is {score}, Your Height is {height}, Your Winning status is {iswinning}")

