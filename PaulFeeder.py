import pyautogui
import emoji
import time
import pyperclip

i = True
n = 0
#makes emoji string
emoji = emoji.emojize(":bug:") + emoji.emojize(":bug:") + emoji.emojize(":bug:")

#gives time for user to get back to window (3 seconds)
time.sleep(3)

while i:
    #tells you how many times emogi has been printed in terminal
    n += 1
    print("Paul has been fed: ")
    print(n)
    print(" ")
    
    #copy and pastes emoji every 60 seconds
    pyperclip.copy(emoji)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(60)
