from tkinter import *

root = Tk()
root.geometry('800x600')
root.title('enable or disable')
bool = BooleanVar()
bool.set(True)
# change background
# relief -->     FLAT      RAISED       SUNKEN       GROOVE            RIDGE

# functions
def change_disabled():
    if bool.get():
        btn2.config(text='disabled',fg='black')
        btn2.config(state='disabled')
        bool.set(False)
    else:
         btn2.config(state='normal',fg='black')   
         bool.set(True)

root.config(bg='pink',bd=20,relief=GROOVE,)
# state --> active , normal , disabled
# activebackground  --> avaz kardan rang hengam negah dashtan click rooye an
# activeforground --> avaz kardan rang font hengam negah dashtan click rooye on
btn1 = Button(root,text='button1',height=5,width=20,bg='red',activebackground='green',bd = 5 ,relief=GROOVE,state='normal')
btn1.pack(side='left',padx=20)

btn2 = Button(root,text='button1',height=5,width=20,bg='green',activeforeground='black',bd = 5 ,relief=GROOVE,state='normal')
btn2.pack(side='right',padx=20)


# call btn 
btn1.config(command=change_disabled)





root.mainloop()