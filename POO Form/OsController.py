import os

def ShutdownPc(turnIndication):
    if turnIndication:
        os.system("shutdown /s /t 1")