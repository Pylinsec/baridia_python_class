colors = ['red\n','blue\n','yellow\n','white\n','green\n']
with open('color.txt','w') as file:
    file.writelines(colors)


file = open('color.txt','r')
# print(file.read())  
# print(type(t))

l = file.readlines() # bargardand list ke ba in tosif har ozv list yek line dar file txt  mast
print(l)
t = file.read()
print(t)
file.close()