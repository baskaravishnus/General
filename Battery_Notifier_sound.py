import psutil
from plyer import notification
import time
from playsound import playsound


# from psutil we will import the
# sensors_battery class and with
# that we have the battery remaining
while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    if(percent>99):     #Here,Set the percentage as you want
        notification.notify(
            title="Battery Percentage",
            message=str(percent)+"% Battery remaining",
            timeout=10
        )
        playsound("sound.wav")
        break
    time.sleep(120) 
    continue
