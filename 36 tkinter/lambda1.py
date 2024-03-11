# anonymous function 
# x = lambda argument: expression
# mesal 1

# x = lambda:print('Bardia Kamaei')
# x()

# mesal 2
# x = lambda a,b: a + b
# print(x(3,4))

# mesal 3
# name = lambda lname:print(f"your last name is {lname}")

# name('Kamaei')


# mesal4
def sum(a,b):
    # print(a ** b)
    return (a**b)

# x = sum(3,4)
# print(x)
y = lambda a ,b:sum(a,b)
z = y(2,3)
print(z)