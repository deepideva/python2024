target=int(input("Enter Number between 0 and 1000 :"))
'''
even_sum=0
for number in range (2, target+1, 2):
    #print(number)
    even_sum += number
print(even_sum)
'''


# Another method
even_sum=0
for number in range (1, target+1): 
    if number % 2 ==0:
        even_sum += number    
print(even_sum)

