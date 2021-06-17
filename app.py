import tkinter
import tkinter.messagebox as tk
from tkinter.font import Font
from tkinter import *
from easygui import *
from turtle import *
import random


root = Tk()
root.wm_attributes("-fullscreen", '1')
root.title("Leave Management System")


MainLabel = Label(root, text="Leave Management System", bd=12, relief=GROOVE, fg="White", bg="blue",font=("Calibri", 36, "bold"), pady=3)
MainLabel.pack(fill=X)

LoginBtn = Button(root, text='Employee login', bd=12, relief=GROOVE, fg="blue", bg="yellow", font=("Calibri", 26, "bold"), pady=3)
LoginBtn.pack(fill=X)

ExitBtn = Button(root, text='Exit', command=root.destroy, bd=12, relief=GROOVE, fg="red", bg="yellow", font=("Calibri", 30, "bold"), pady=3)
ExitBtn.pack(fill=X)
MainLabel.pack()
LoginBtn.pack()
ExitBtn.pack()

root.mainloop()
