import pyautogui
import time
from pynput import keyboard

# Set end date for FW tasks
END_DATE = "27.02.2025 18:00:00"

def pointAt(img):
    while True:
        try:
            button_location = pyautogui.locateOnScreen(img, grayscale=True)
            if button_location is not None:
                return pyautogui.center(button_location)
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.5) 

# Function to click a button when it appears
def safe_click(img):
    while True:
        try:
            center = pointAt(img)
            pyautogui.click(center)
            break
        except Exception as e:
            print(f"Failed to click {img}: {e}")
            time.sleep(0.5)

def safe_doubleClick(img):
    while True:
        try:
            center = pointAt(img)
            pyautogui.doubleClick(center)
            break
        except Exception as e:
            print(f"Failed to click {img}: {e}")
            time.sleep(0.5)

# Global variable to signal when the key is pressed
key_pressed = False

def on_press(key):
    global key_pressed, ctrl_held
    try:
        # Check if Ctrl is pressed
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            ctrl_held = True
        # Check if F10 is pressed while Ctrl is held down
        elif key == keyboard.Key.f10 and ctrl_held:
            print("Ctrl + F10 pressed, continuing...")
            key_pressed = True
            return False  # Stop listener after the key is detected
    except AttributeError:
        pass

def on_release(key):
    global ctrl_held
    try:
        # Check if Ctrl is released
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            ctrl_held = False
    except AttributeError:
        pass

# Function to wait for the key press
def wait_for_key_press():
    global key_pressed
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    while not key_pressed:
        time.sleep(0.1)

time.sleep(2)
# Collect all instances of the button
buttons = list(pyautogui.locateAllOnScreen('dropdown.png'))
# assign change coordinator
pyautogui.click(pyautogui.center(buttons[1]))
time.sleep(1)
pyautogui.click(pointAt('name.png'))
# assign change manager
pyautogui.click(pyautogui.center(buttons[2]))
time.sleep(1)
pyautogui.click(pointAt('name.png'))
# Open task
safe_click('tasks.png')
safe_doubleClick('pmatrix_task.png')
safe_click('save_con.png')
time.sleep(2)
## Process task
# Set dates
safe_click('dates.png')
# Clear and set start date
pyautogui.moveTo(pointAt('start_date.png'))
pyautogui.moveRel(277, 0)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.press('enter')
# Set end date
pyautogui.moveRel(500, 0)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.write(END_DATE)
# Assign to person
safe_click('assignment.png')

print("Assign the engineer, press Ctrl + F10 to continue")
wait_for_key_press()

safe_click('save_task.png')
safe_click('ok.png')
safe_click('back.png')
time.sleep(1.5)
# Set CRQ dates
pyautogui.moveTo(pointAt('start_date_crq.png'))
pyautogui.moveRel(277, 0)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.press('enter')
pyautogui.moveRel(0, 30)
pyautogui.click()
safe_click('close.png')
pyautogui.moveTo(pointAt('start_date_crq.png'))
pyautogui.moveRel(277, 0)
pyautogui.moveRel(0, 30)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.write(END_DATE)

# Move to scheduled and save
pyautogui.moveRel(-300, 0)
pyautogui.scroll(-200)
time.sleep(1)  # Scroll delay
pyautogui.scroll(-200)
safe_click('next_stage.png')
safe_click('yes.png')
safe_click('ok.png')
safe_click('next_stage.png')
safe_click('ok.png')
safe_click('save_crq.png')
safe_click('yes_2.png')

pyautogui.moveRel(-300, 0)
time.sleep(1)
pyautogui.scroll(200)
pyautogui.scroll(200)

print("Automation completed")