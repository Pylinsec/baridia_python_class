# module 
import os
# sakhtan folder ---> makdir --> make directory
# os.mkdir('name')
# os.mkdir('qoli') # dar jaye ke hastam folder besaz
# . --> hamin ja  , .. --> yani ye folder eqabtar ya baba , 
# os.mkdir('../HHHHHHH/RRRRR')
# --------------------------------------------------------
# os.mkdirs(path)
# os.makedirs('qoli1/qoli2/qoli3/qoli4/qoli5') # mkdirs --> temam folder ye masir dar soorat  neboodan misaze
if not os.path.exists('test'):
    os.mkdir('test')

# check voojod f
print(os.path.exists('test/bardia.txt'))
# =================//=========\\====================
# sakht file dar folder pedar
with open ('../bardia.txt','w') as file:
    pass

# sahkt file dar folder badi
with open ('test/bardia.txt','w') as file:
    pass