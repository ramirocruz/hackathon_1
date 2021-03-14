import time

class humidityController:
    def __init__(self,humiditySensorClient):
        self.humidiySensorClient = humiditySensorClient
        self.startControl()
    
    def startControl(self):
        print("Application Deployed")

        while(1):
            humidity = self.humidiySensorClient.getHumidity()
            print("Humidity = " + str(humidity))
            if(humidity < 5):
                self.humidiySensorClient.setSprinkler()
                print("Low Humidity, Sprinkler Started.")
            time.sleep(2)