from tkinter import *

root = Tk()
root.geometry('1000x800')
root.title('Frame')
root.config(bg = 'black')

# IntVar  --> adad migire
# StringVar --> string 
# BooleanVar  --> True , False 
flag = BooleanVar()
flag.set(True)
# flag.set(True) --> gherat dadan meghdar 
# flag.get() --> gereftan value 

# baba
# main_frame = Frame(root,bg='lightgreen',width=940,height=740)
# main_frame.pack(padx=30,pady=30)


# function
def change_color():
    f = flag.get()
    if f:
        root.config(bg='blue')
        flag.set(False)
    else:
        root.config(bg='black')    
        flag.set(True)

def chap():
    print(flag.get())
    root.title('bardia')
# btn = Button(root,text='Click me',bg='red',width=20,height=10,font=10,command=change_color)
# btn.pack(padx=30,pady=30)
btn = Button(root,text='Click me',bg='red',width=20,height=10,font=10,command=chap)
btn.pack(padx=30,pady=30)



root.mainloop()
