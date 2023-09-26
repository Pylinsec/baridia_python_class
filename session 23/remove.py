import os

#============ hazf file dar mesir dade shode =========================
# os.remove('test/bardia.txt')

# mesal 1 -->  sakht 20 file txt dakhel folder test
# for i in range(1,21):
#     # sakht
#     # with open('test/'+ str(i),'w') :
#     with open(f'test/{i}','w') :
#         pass
# 



# ============================== os.rmdir()===========================
# os.rmdir('path') # hazf folder be shart khali boodand 
# os.rmdir('test1/test2')


# ======================================== os.removedirs(path)=================
# hazf folder haye too dar too  be shart khali boodan az file 
os.removedirs('test1/test2/test3/1.txt')