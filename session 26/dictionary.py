test = {'school': 'shohada', 'car': 'kia', 'address': 'ahvaz'}

print(test.keys()) # list az item haye qabl az :
print(test.values()) # list az item haye bad az :
print(test['school']) # chap meqdar item moshakhas 


# chap keys 
for item in test.keys():
    print(item , end=' ')

print()
# chap values     
for item in test.values():
    print(item,end=' ')
    
print()
for a,b in test.items():
    print(f'{a}-->{b}')   