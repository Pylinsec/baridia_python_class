import os

# os.rename(name alan,new name) change name file , and folder 
# os.rename('bardia1','QOLI')

# mesal jehat rename file 
'''
if os.path.exists('QOLI\\123.txt'):
    os.rename('QOLI\\123.txt','QOLI\\333.txt')
else:
    print('masir voojood nedarad')    

'''
# SOAL:  agar bekham move koname bayad chikar konam
if os.path.exists('QOLI\\333.txt'):
    os.rename('qoli\\333.txt','bardia\\havij.txt')
else:
    print('masir voojood nedarad')    
