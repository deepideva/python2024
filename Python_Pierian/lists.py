mylist=["One","Two","Three","Four","Five"]
print(mylist)
print(mylist[1])
print(mylist[2:])
deepilist=[1,2,3,4,5]
print(mylist + deepilist)
print(mylist[1] + "    " + str(deepilist[1]))
mylist.append("Six")
print(mylist)
print("Six added in Mylist, now see how to delete using POP")
mylist.pop()
print(mylist) # Last value Six is Poped out / deleted
#Save the popped item
popped_item=mylist.pop()
print("Your Popped Item is ", popped_item)
# To pop particular place
mylist.pop(1)
print(mylist)