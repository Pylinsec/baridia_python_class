import os

# windows --> C:\Windows\System32\cmd.exe 
# linux --> /m/pythonClass/bardia/24

name= 'bardia'
lname = 'kemaei'
age = '15'

# bardia/kemaei/15
# os.path.join(name,lname,age) --> format
path = os.path.join(name,lname,age)
print(path)
os.makedirs('bardia\\kemaei\\15')