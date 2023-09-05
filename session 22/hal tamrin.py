alefba = 'abcdefghijklmnopqrstuvwxyz'
for item in alefba:
    with open(f"{item}.txt",'w') as file:
        file.write(f"{item.upper()}")