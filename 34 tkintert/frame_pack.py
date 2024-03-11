from tkinter import *

root = Tk()
root.geometry('1000x800')
root.title('Frame')
root.config(bg = 'black')

# baba
main_frame = Frame(root,bg='lightblue',width=1000,height=780)
main_frame.pack()

# bache
frame1 = Frame(main_frame,bg='green',width=980,height=130)
frame1.pack()
frame2 = Frame(main_frame,bg='orange',width=980,height=250)
frame2.pack()
frame3 = Frame(main_frame,bg='blue',width=980,height=380)
frame3.pack()

# frame3 bache 
frame3_left = Frame(frame3,bg='yellow',width=400,height=380)
frame3_left.pack(side='left')
frame3_right = Frame(frame3,bg='pink',width=400,height=380)
frame3_right.pack(side='right')

# frame3_right bache
frame3_right_top = Frame(frame3_right,bg='red',width=580,height=180)
frame3_right_top.pack()
frame3_right_bot = Frame(frame3_right,bg='green',width=580,height=200)
frame3_right_bot.pack()
# user_lbl = Label(frame3_right_top,text='UserName',fg='black')
# user_lbl.pack()
# user_lbl = Label(frame3_right_bot,text='PassWord',fg='black')
# user_lbl.pack()

root.mainloop()
