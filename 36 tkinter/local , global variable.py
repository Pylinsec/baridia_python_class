#  global , local
# global --> hameja ghabel dastresi hast
# local --> dakhel function 

a = 34
def test():
    # local
    a = 4
    return a


print(a)
a = 444
print(test())
print(a)