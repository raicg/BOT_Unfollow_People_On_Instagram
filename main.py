unfollow = 20 #CHANGE HERE HOW MANY PEOPLE YOU WILL UNFOLLOW
import pyautogui
import time
import pyperclip
import random

pyautogui.PAUSE = 1 #Set up a 1 second pause after each PyAutoGUI call
find = "find.png" #image to search on screen (needs to be on the same directory as the main.py) 
find2 = "find2.png" #image to search on screen (needs to be on the same directory as the main.py) 

def main():
    i = 0
    pyautogui.hotkey('alt', 'tab', interval=0.1) #alt+tab to switch to instagram screen
    time.sleep(1) #sleep for 1 second

    for n in range (0,unfollow):
        try:
            found = pyautogui.locateOnScreen(find) #search for: image="find" on the screen
            pyautogui.click(found[0] + 10, found[1] +5, 1, 0.2) #click on image found
            time.sleep(1) #sleep for 1 second

            if i == 0: #this will work only once, because instagram somehow protect it, but
                #this button will be on the same place on screen every time, so we need it to locate only once
                found2 = pyautogui.locateOnScreen(find2) #search for: image="find2" on the screen
                i = 1 #to prevent it from running more than once

            pyautogui.click(found2[0] + 10, found2[1] +5, 1, 0.2) #click on image found2
            time.sleep(random.randrange(6,15)/10) #sleep random time

        except IOError: #if image="find" is not found (needs to be on the same directory as the main.py)
            print('Image not found')
            break

        except: #if image="find" is not found on screen
            pyautogui.scroll(-5) #scroll screen
            pass

    pyautogui.hotkey('alt', 'tab', interval=0.1) #alt+tab to switch to main.py screen
    print("%d people were unfollowed" % (n+1)) #how many people were unfollowed

main()