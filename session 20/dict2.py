bardia1 = {'lastname':'kamaei','name':'bardia','age':15}
# access
# keys --> temam ozv haye qabl az ':'
# values --> harch bad az ':'

# chap keys
print(bardia1.keys())
print(bardia1.values())

# access
print(bardia1['name'])
print(bardia1['lastname'])
print(bardia1['age'])
print(bardia1.get('name'))
print(bardia1.get('lastname'))
print(bardia1.get('age'))

# for rooye keys()
for item in bardia1.keys():
    print(item ,end=' ')

print()
#  for rooye values()
for item in bardia1.values():
    print(item ,end=' ')