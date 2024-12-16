import pyautogui
import time

def pointAt(img):
    button_location = pyautogui.locateOnScreen(img, grayscale=True)
    return pyautogui.center(button_location)

while True:
    try:
        time.sleep(60)
        pyautogui.click(pointAt('refresh.png'))
        pyautogui.moveRel(0, 150)
    except pyautogui.ImageNotFoundException:
        print("The button cannot be found.")