"""
Author : Abhinav Muley
Date thu 12:9:2021 :: 07:54:00
"""


from pygame import mixer
import time
from time import localtime, strftime

# if strftime("%I:%M:%S", localtime())
if (int(strftime("%H"))>=7 and  ((strftime("%p"))=="AM") and int(strftime("%H"))<12) or int(strftime("%H"))>=12 and  ((strftime("%p"))=="PM") and int(strftime("%H"))<18:

    while True:
        time.sleep(3)##-->time is zero it will rang after 30 minutes
        mixer.init()
        mixer.music.load("C:\\Users\\ASUS\\Desktop\\python\\Infraction-Weekend-Main-Version-pr.mp3")##-->>path of music for to take care of eyes
        mixer.music.play()
        print("'s' to stop and 'e' to exit from this notifier..!!")
        a=input("time to take care of eyes")
        
        if a=='s':
            mixer.music.stop()
        if a=='e':
            break

        time.sleep(4)##-->time is zero it will rang after 45 minutes for to drink water
        mixer.init()
        mixer.music.load("C:\\Users\\ASUS\\Desktop\\python\\Infraction-The-Tempo-Main-Version-pr.mp3")##-->>path of music for to drink water
        mixer.music.play()
        print("'s' to stop and 'e' to exit from this notifier..!!")
        a=input("time to drink 400ml of water")

        if a=='s':
            mixer.music.stop()
        if a=='e':
            break
        
        time.sleep(6)#-->time is zero it will rang after 60 minutes for to drink water
        mixer.init()
        mixer.music.load("C:\\Users\\ASUS\\Desktop\\python\\Standard recording 5.mp3")##-->>path of music to notify for bodyworkout time
        mixer.music.play()
        print("'s' to stop and 'e' to exit from this notifier..!!")
        a=input("time to workout")

        if a=='s':
            mixer.music.stop()
        if a=='e':
            break
else:
    print("Time for reminder starts from 9AM-5PM")           
