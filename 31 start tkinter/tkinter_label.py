from tkinter import *
import time 

bardia = Tk()
bardia.geometry('800x600')
bardia.title('Bardia')
bardia.config(bg='green')

# sakht label
# fg --> heman rang font hast
lbl = Label(bardia,text='bardia',fg='red',font=50)
# padx --> faseleh az samt chap
# pady --> faseleh az samt bala
# lbl.pack(padx = 200 , pady=100)

username = Label(bardia,text='UserName:',fg='yellow',font=1,bg='green')
username.pack(padx = 20 , ipady=10)
password = Label(bardia,text='Password: ',fg='yellow',font=1,bg='green')
password.pack(padx = 20 , ipady=20)



bardia.mainloop()