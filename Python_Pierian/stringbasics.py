mystring="Ganeshbabu"
number=123
'''
print(mystring[0])
print(mystring[-1])
print(mystring[2])
print(mystring[2:])
print(mystring[:2])
print(mystring[2:5])
print(mystring[::])
print(mystring[::3])
'''
print(mystring)
print(mystring[3:7:2]) 
''' Above line, 3 is the starting place, 7 is the place to end, 2 is step to jump
    So answer will be ""eh"" '''
print(mystring[::-1]) 
print(mystring + " Welcome to Chennai")
print(mystring.upper())
print(mystring.lower())
print(mystring.split('a'))
print(mystring,'{}'.format('Welcome'))
print(mystring,'{}'.format('fast','eat','very'))
print(mystring,'{} {}'.format('fast','eat','very'))
print(mystring,'{} {} {}'.format('fast','eat','very'))
print(mystring,'{1} {2} {0}'.format('fast','eat','very'))
print(mystring,'{1} {1} {0}'.format('fast','eat','very'))
print(mystring,'{e} {v} {f}'.format(f='fast',e='eat',v='very'))
