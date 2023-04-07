import InputController
import TimeController

inputValues = InputController.InitializeWaitValues()

print("Selecciona un campo de texto")
TimeController.WaitForSeconds(5)
TimeController.SetStartCountingTime(inputValues[0], inputValues[1])