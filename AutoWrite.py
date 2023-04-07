import pyautogui
import os
import time

timeInMinutes = float(input("¿Cuanto tiempo en minutos quieres esperar? "))
turnStr = input("¿Quieres apagar el pc al acabar? (y/n) ")

if turnStr == "y":
    turnIndication = True
elif turnStr == "n":
    turnIndication = False


actualTime = time.time()
timeInSeconds = timeInMinutes * 60
timeToIdle = actualTime + timeInSeconds

countSeconds = 0
print("Selecciona un campo de texto")
time.sleep(5)

while(True):

    if timeToIdle < time.time():
        break

    pyautogui.write(str(countSeconds))
    pyautogui.press('space')
    time.sleep(5)
    countSeconds += 5


pyautogui.write('\n \n Espere por {} minutos'.format(timeInMinutes))
if turnIndication:
    os.system("shutdown /s /t 1")

