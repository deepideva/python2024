#input list of Student scores
student_scores=input("Enter numbers as much you need with 1 space: ").split()
print(student_scores)
''' output will be 
Enter numbers as much you need with 1 space1 2 3 4 5 6 
['1', '2', '3', '4', '5', '6']
'''
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
# to find high score
highest_score=0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")


'''
Detailed Iteration:
Initial highest_score = 0
Iteration 1: score = 1 (1 > 0, so highest_score becomes 1)
Iteration 2: score = 5 (5 > 1, so highest_score becomes 5)
Iteration 3: score = 6 (6 > 5, so highest_score becomes 6)
Iteration 4: score = 4 (4 is not greater than 6, so highest_score remains 6)
Iteration 5: score = 2 (2 is not greater than 6, so highest_score remains 6)
Iteration 6: score = 3 (3 is not greater than 6, so highest_score remains 6)
'''
