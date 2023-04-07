import time
import AutoWriteController

def WaitForSeconds(seconds):
    time.sleep(seconds)

def SetStartCountingTime(timeInMinutes, turnIndication):
    actualTime = time.time()
    timeInSeconds = timeInMinutes * 60
    timeToIdle = actualTime + timeInSeconds
    CountingTimeLoop(timeToIdle, timeInMinutes, turnIndication)

def CountingTimeLoop(timeToIdle, timeInMinutes, turnIndication):
    while(True):
        if timeToIdle < time.time():
            break

        AutoWriteController.AutoWrite()
        WaitForSeconds(5)
    
    AutoWriteController.EndAutoWrite(timeInMinutes, turnIndication)
