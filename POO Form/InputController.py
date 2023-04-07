
def InitializeWaitValues():
    timeInMinutes = float(input("¿Cuanto tiempo en minutos quieres esperar? "))
    turnStr = input("¿Quieres apagar el pc al acabar? (y/n) ")
    return timeInMinutes, CheckTurnOnOff(turnStr)

def CheckTurnOnOff(turnStr):
    if turnStr == "y" or turnStr == "yes" or turnStr == "Y" or turnStr == "Yes":
        return True
    elif turnStr == "n" or turnStr == "no" or turnStr == "N" or turnStr == "No":
        return False