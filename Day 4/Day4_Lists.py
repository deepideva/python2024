team_list = ["Ganesh","Rani","Suruthi","Sureka","Swathi","Mano"]
print(team_list[0])
print(team_list[-1])
team_list[0]="Ganeshbabu"
print(team_list[0])
team_list.append("Jawahar")
team_list.extend(["Muthu","Sidha"])

#get input and see the person
team_in=int(input("Enter the number to see (1 to 6): "))
print(team_list[team_in])
print(team_list)