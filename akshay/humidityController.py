class humidityController:
    def __init__(self,humiditySensorClient):
        self.humidiySensorClient = humiditySensorClient
        self.startControl()
    
    def startControl(self):
        humidity = self.humidiySensorClient.getSensorData()
        while(humidity < 5):
            self.humidiySensorClient.startSprinkler()
            humidity = self.humidiySensorClient.getSensorData()
        self.humidiySensor.Client.stopSprinkler()