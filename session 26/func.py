
#  vaghti ke ersal dadeha besoorat dictionary hast va ma tadadshanb nemidanim 

# ** --> yani daryaft parametr be soorat dictionary hast , *-->  0 ya bishtar , 
def chap(name,age,lname,**qoli): # **kwargs --> yanni daryaft bishtar 
    print(name,lname,age)
    for item in qoli.values():
        print(item)
    


chap(name='bardia',lname='kamaei',age=16,school='shohada',car='kia',address='ahvaz')    
# chap(lname='kamaei',age=16,name='bardia',car='kia',school='shohada')    