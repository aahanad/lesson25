from tkinter import*
screen=Tk()
import random
from time import strftime
from tkinter import messagebox
import time
screen.geometry("600x150")
screen.title("timer⏰")
screen.config(bg="pale turquoise")
hours=StringVar()
mins=StringVar()
seconds=StringVar()
hours.set("00")
mins.set("00")
seconds.set("00")
def stopwatch():
    try:
        temp=int(min.get())*60+ int(hour.get())*3600+int(sec.get())
    except:
        messagebox.showerror("showerror","404 not found😕😟😾😡💔😓☹😥😔")
    while temp> -1:
        mnts,secs=divmod(temp,60)
        hrs=0
        if mnts>60:
            hrs,mnts=divmod(mnts,60)
        hours.set("{:02d}".format(hrs))
        mins.set("{:02d}".format(mnts))
        seconds.set("{:02d}".format(secs))
        screen.update()
        time.sleep(1)
        if temp ==0:
            messagebox.showinfo("Time Countdown⌛","Time's Up⏳")
        temp-=1
hour=Entry(screen,bg="SlateBlue2",font=("SimSun",12,"bold"),textvariable=hours)
hour.grid(row=1,column=1,padx=50,pady=20)
min=Entry(screen,bg="SlateBlue2",font=("SimSun",12,"bold"),textvariable=mins)
min.grid(row=1,column=2,padx=60,pady=20)
sec=Entry(screen,bg="SlateBlue2",font=("SimSun",12,"bold"),textvariable=seconds)
sec.grid(row=1,column=3,padx=85,pady=20)
submit=Button(screen,text="SUBMIT",bg="SlateBlue2",font=("simsun",13,"bold"),command=stopwatch)
submit.grid(row=2,column=3,padx=85,pady=45)

screen.mainloop()
