class PHController:
    def __init__(self,PHSensorInstance):
        self.PHSensorInstance = PHSensorInstance
        self.startControl()
    
    def startControl(self):
        phValue = self.PHSensorInstance.getSensorData()
        while(phValue > 9):
            self.PHSensorInstance.decreasePH()
            phValue = self.PHSensorInstance.getSensorData()
        self.PHSensorInstance.stop()
