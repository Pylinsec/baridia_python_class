with open('fileio.txt','r') as havij:
    text = havij.read()
    print(text.capitalize())
text_upper = text.upper()
# print(text_upper)    

with open ('bardia.txt','w')as file:
    file.write(text_upper) # string mikhad
    