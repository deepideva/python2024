#Tip calculator
print("Welcome to the Tip Calculator")
bill=float(input("What was the total bill ? "))
tippercentage=float(input("How much Tip % you like to give ? 10, 12 or 15 % --> "))
people=int(input("How many people to split your Bill"))
#Calculate the Tip
tipamount=(tippercentage/100)*bill
#Add the tip amount to Bill amount
totalbill=bill+float(tipamount)
#To find the share for each person
shareeach=float(totalbill) / people
#final_amount=round(shareeach,2)
final_amount="{:.2f}".format(shareeach)
print(f"Each person should Pay : $ {final_amount}")




#print("What was the total bill ? ",bill)
#print("How much Tip % you like to give ? 10, 12 or 15 % --> ")


