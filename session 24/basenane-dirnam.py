import os 

# path= 'bardia\\kemaei\\15.mp3' --> dirname=bardia\\kemaei\\  basenmae=15.mp3
path= 'bardia\\kemaei\\15.mp3'
print(path[-4::])

print(os.path.basename(path))
print(os.path.dirname(path))

# print masir feli yani jaei ke hastim
print(os.getcwd())  # curerent working directory


# os.path.isfile() --.> agar masir adress file bood true mishod
# os.path.isdir()--> agar masir directory bood true mishod

path1 = 'bardia\\kemaei\\15'
path2= 'e.txt'

print(os.path.isfile(path1))
print(os.path.isdir(path1))

print(os.path.isfile(path2))
print(os.path.isdir(path2))