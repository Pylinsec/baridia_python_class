import random # tesadofi 

# random.random()  --> addadi bin 0 ta 1 barmigardanad
# print(random.random())
# for i in range(100):
#     print(random.random())


# ===========================================================================
# random.randint(a,b)--> addadi tesadofi bin a,b barmigardand 
# for i in range(30):
#     print(random.randint(-10,20)) 

#==================================================================================

# random.randrange(start,end,step) # addadi bar asas game step be soorat tesadofi barmigardand 

# for i in range(10):
#     print(random.randrange(10,30,4),end=' ') # 10 ,13,16,19,22,25,28

# ===================================================================================
# random.choice(list,tuple)
color_l = ['red','blue','white','green','orange','black','pink'] # list
color = ('red','blue','white','green','orange','black','pink') # tuple

# print(random.choice(color))
# random.shuffle(list) darham kardan item haye dakhel list , rikhtan dakhel hamem list avalio
# print(color_l)
# new = random.shuffle(color_l)
# print(color_l)

# ======================================================
# how to make random float digit --> random.uniform(start,end)
print(random.uniform(2,7))