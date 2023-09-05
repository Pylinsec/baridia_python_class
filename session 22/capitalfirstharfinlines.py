file = open('fileio.txt','r') 
lines = file.readlines()
for line in lines:
    print(line.capitalize()) # harf aval temam khat ha ba capitalize bozorg mishe
    print(line.title())  # harf aval temam kelemat bozorg mishe
file.close()