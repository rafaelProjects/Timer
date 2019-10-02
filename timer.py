import time
from tkinter import *
import random

seconds =0
minutes=0
hours=0

def counter():
    global seconds
    global minutes
    global hours
    if(minutes == 59):
        hours+=1
        minutes=0
    elif(seconds == 59):
        minutes += 1
        seconds=0
    else:
        seconds+=1
    l.config(text="Hours: {}\n Minutes: {} \n Seconds: {}".format(hours, minutes, seconds), bg="black", fg='green2')
    root.after(1000, counter)


root = Tk()
root.configure(background='black')
root.title("Timer")
root.geometry('200x600') #Width x Height
m = Label(text="\n \n Minimalist Timer by Rafael \n ---------------------------------",  bg="black", fg="green2")
m.pack()
l = Label(text="Hours: 0\n Minutes: 0 \n Seconds: 0", bg="black", fg="green2")
l.pack(fill="none", expand=True)

root.after(1000, counter)

root.mainloop()
