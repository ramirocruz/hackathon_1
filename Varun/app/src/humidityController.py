class humidityController:
    def __init__(self,humiditySensorInstance):
        self.humidiySensorInstance = humiditySensorInstance
        self.startControl()
    
    def startControl(self):
        humidity = self.humidiySensorInstance.getSensorData()
        while(humidity < 5):
            self.humidiySensorInstance.startSprinkler()
            humidity = self.humidiySensorInstance.getSensorData()
        self.humidiySensorInstance.stopSprinkler()