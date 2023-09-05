#  tedad khoto , tedad kelemeh , tedad horoof
with open('fileio.txt','r') as file:
    lines = file.readlines() # sakht list ke har khat file yek item on mishe
print(lines)   
print(len(lines)) # len miad tedad ozv ke hamen tedad khoto hast neshan mide

print('lineavval : ',lines[0])
print('line akhar : ',lines[-1])