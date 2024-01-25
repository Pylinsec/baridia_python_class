from tkinter import *
import time 

bardia = Tk()
bardia.title('Bardia')
for i in range(10,1000,50):
    bardia.geometry(f'{i}x{i}')
    time.sleep(.5)
    bardia.update()


bardia.mainloop()