import pyautogui
import OsController
countSeconds = 0

def AutoWrite():
    global countSeconds
    pyautogui.write(str(countSeconds))
    pyautogui.press('space')
    countSeconds += 5

def EndAutoWrite(timeInMinutes, turnIndication):
    pyautogui.write('\n \n Espere por {} minutos'.format(timeInMinutes))
    OsController.ShutdownPc(turnIndication)
    