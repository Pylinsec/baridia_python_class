from tkinter import *
import time 

bardia = Tk()
bardia.geometry('800x600')
bardia.title('Bardia')
colors = ['red','green','blue','gray','pink','black']
for color in colors:
    time.sleep(2) # maks be andazeh 2 sanieh
    bardia.config(background=color)
    bardia.update()


bardia.mainloop()