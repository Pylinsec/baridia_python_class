import os


path1 = 'bardia\\kemaei\\15'
path2 = 'bardia\\kemaei\\16'
# os.path.exists(path) --> agar in masir bood true mishe agar nebood false mishe 
print(os.path.exists(path1))
print(os.path.exists(path2))

# mesal 1
if os.path.exists('bardia1'):
    print('folder khaste shode voojood darad')
else:
    os.mkdir('bardia1')