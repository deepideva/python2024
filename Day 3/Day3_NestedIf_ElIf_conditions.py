print("Welcome to the Wonderla")
height=int(input("Waht is your Height in Cms ?"))
bill=0
if height >= 120:
    print("Good To Go")
    age=int(input("What's ur age ?"))
    if age < 12:
        bill=5
        print("Please pay 5 $")
    elif age <= 18:
        bill=7
        print("Please pay 7 $")
    else:
        bill=12
        print("Please pay 12 $")
    want_photo= input("Do you wnat Photo taken? : Y or N ( 3 Dollars extra )")
    if want_photo=="Y":
        bill+=3
    print(f"Your Final Bill is {bill}")
else:
    print("Get Out of Amuzement park")
