import pyautogui
import time

# set end date for FW tasks
END_DATE = "20.12.2024 18:00:00"

def pointAt(img):
    button_location = pyautogui.locateOnScreen(img, grayscale=True)
    return pyautogui.center(button_location)

time.sleep(2)

# Collect all instances of the button
buttons = [button for button in pyautogui.locateAllOnScreen('dropdown.png')]

# assign change coordinator
pyautogui.click(pyautogui.center(buttons[1]))
time.sleep(1)
pyautogui.click(pointAt('name.png'))

# assign change manager
pyautogui.click(pyautogui.center(buttons[2]))
time.sleep(1)
pyautogui.click(pointAt('name.png'))

# open task
pyautogui.click(pointAt('tasks.png'))
time.sleep(1)
pyautogui.doubleClick(pointAt('pmatrix_task.png'))
time.sleep(1)
pyautogui.click(pointAt('save_con.png'))
time.sleep(8)
## process task
# set dates
pyautogui.click(pointAt('dates.png'))
time.sleep(1)
pyautogui.moveTo('start_date.png')
pyautogui.moveRel(277, 0)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.press('enter')
pyautogui.moveRel(500, 0)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.write(END_DATE)

# assign to person
pyautogui.click(pointAt('assignment.png'))

input("Assign the engineer, press enter to continue")
time.sleep(2)
pyautogui.click(pointAt('save_task.png'))
time.sleep(2)
pyautogui.click(pointAt('ok.png'))
time.sleep(1)
pyautogui.click(pointAt('back.png'))
time.sleep(3)
# set CRQ dates
pyautogui.moveTo('start_date_crq.png')
pyautogui.moveRel(277, 0)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveRel(0, 30)
pyautogui.click()
time.sleep(1)
try:
    pyautogui.click(pointAt('close.png'))
    pyautogui.moveTo('start_date_crq.png')
    pyautogui.moveRel(277, 0)
    pyautogui.moveRel(0, 30)
    pyautogui.click()
    time.sleep(1)
except pyautogui.ImageNotFoundException:
    print("No close window 1")
    time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.write(END_DATE)
time.sleep(1)
try:
    pyautogui.click(pointAt('close.png'))
except pyautogui.ImageNotFoundException:
    print("No close window 2")
time.sleep(1)
# move to scheduled and save
pyautogui.moveRel(-300, 0)

pyautogui.scroll(-200)
time.sleep(1)
pyautogui.scroll(-200)
time.sleep(1)
pyautogui.click(pointAt('next_stage.png'))
time.sleep(1)
pyautogui.click(pointAt('yes.png'))
time.sleep(5)
try:
    pyautogui.click(pointAt('ok.png'))
except pyautogui.ImageNotFoundException:
    time.sleep(8)
    pyautogui.click(pointAt('ok.png'))
time.sleep(1)
pyautogui.click(pointAt('next_stage.png'))
time.sleep(5)
try:
    pyautogui.click(pointAt('ok.png'))
except pyautogui.ImageNotFoundException:
    time.sleep(5)
    pyautogui.click(pointAt('ok.png'))
time.sleep(1)
pyautogui.scroll(-200)
time.sleep(1)
pyautogui.scroll(-200)
time.sleep(1)
pyautogui.click(pointAt('save_crq.png'))
time.sleep(2)
pyautogui.click(pointAt('yes_2.png'))
time.sleep(1)
pyautogui.scroll(200)
pyautogui.scroll(200)
print("Automation completed")