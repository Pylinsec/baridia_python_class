import os 

list_file = os.listdir('bardia2')
print(list_file)
for i in list_file:
    # print(f"bardia2/{i}")
    if os.path.isdir(f"bardia2/{i}"):
        os.rmdir(f"bardia2/{i}")
    else:
        os.remove(f"bardia2/{i}")    