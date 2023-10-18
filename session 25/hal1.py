import os 
# # print(os.path.exists('bardia'))
# if not os.path.exists('bardia'):
#     os.mkdir('bardia')
# else:
#     pass   


# ************************************ sakht 50 folder

for i in range(1,51):
    print(f"bardia/{i}")
    if not os.path.exists(f"bardia/{i}"):
        os.mkdir(f"bardia/{i}")

# ******************* sakht file a ta z
chars = 'abcdefghijklmnopqrstuvwxyz'
for i in chars:
    with open (f"bardia/1/{i}.txt",'w') as f:
        f.write(f"bardia/1/{i}.txt")