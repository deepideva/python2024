
print("Welcome to the Wonderla")
height=int(input("Waht is your Height in Cms ?"))
if height >= 120:
    print("Good To Go")
    age=int(input("What's ur age ?"))
    if age < 12:
        print("Please pay 5 $")
    elif age <= 18:
        print("Please pay 7 $")
    else:
        print("Please pay 12 $")
else:
    print("Get Out of Amuzement park")
