import psutil
import time
from tkinter import *

# from psutil we will import the
# sensors_battery class and with
# that we have the battery remaining    
while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    if(percent>99): #Here,Set the percentage as you want
        root = Tk()
        root.title("Battery Percentage")
        a = Label(root, text =str(percent)+"% Battery remaining",font=("Times New Roman", 90),bg="yellow",fg="red")  #Here,Set the colours as you want
        a.pack() 
        root.wm_attributes("-topmost", 1)
        root.mainloop()
        break
    time.sleep(120)
    
