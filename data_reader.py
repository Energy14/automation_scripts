# PARTIAL AUTOMATION

import win32clipboard as clipboard
import pyautogui
import time

def pointAt(img):
    while True:
        try:
            button_location = pyautogui.locateOnScreen(img, grayscale=True)
            if button_location is not None:
                return pyautogui.center(button_location)
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.2)

def safe_click(img):
    while True:
        try:
            center = pointAt(img)
            pyautogui.click(center)
            break
        except Exception as e:
            print(f"Failed to click {img}: {e}")
            time.sleep(0.2)

def safe_doubleClick(img):
    while True:
        try:
            center = pointAt(img)
            pyautogui.doubleClick(center)
            break
        except Exception as e:
            print(f"Failed to click {img}: {e}")
            time.sleep(0.2)

def copy():
    pyautogui.hotkey('ctrl', 'c')
    clipboard.OpenClipboard()
    data = clipboard.GetClipboardData()
    clipboard.CloseClipboard()
    return data

# Template definition
template = """
| Name      | {name} |
| --------- | ---- |
| CRQ       | {crq_number} |
| PSP       | {psp} |
| Requestor | {requestor_email} |
| SecEXC    | EXC- |
| Special   | {special} |
| PM        | {portmatrix} |

Tufin IDs:

**Template:**

Tufin Ticket - update of the Tickets via Email:

Click the link to view the current state of the created Tufin Tickets. Note that you have to login FIRST with your ITOper account using this link: https://secureapp.swisscom.com

The Ticket is implemented as soon as you receive the email or if you check with the link, if in the top right corner it says "Ticket closed".

Tufin Ticket:

https://secureapp.swisscom.com/securechangeworkflow/pages/manageTasks/manageTasksViewTicket.seam?ticketId=
"""
# Gather data
time.sleep(2)
safe_click('crq.png')
pyautogui.moveRel(277, 0)
pyautogui.doubleClick()
crq_number = copy()

safe_click('summary.png')
pyautogui.moveRel(255, 0)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
name = copy()

safe_click('requested_for.png')
safe_click('email.png')
pyautogui.moveRel(277, 0)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
requestor_email = copy()
psp = ""
special = ""
portmatrix = ""

# Format the template with gathered data
formatted_template = template.format(
    name=name,
    crq_number=crq_number,
    psp=psp,
    requestor_email=requestor_email,
    special=special,
    portmatrix=portmatrix
)

# Write to a markdown file
with open('tufin_ticket.md', 'w') as f:
    f.write(formatted_template)

safe_click('close_2.png')