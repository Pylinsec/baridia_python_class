with open('fileio.txt','r') as bardia:
    text = bardia.read() # string kon beria dakhel text
    print('tedad horof ' ,len(text))


count =1   
for i in text:
    if i == ' ':
        count += 1
print('tedad kelemat ', count)

print(text.count(' ') + 1)


