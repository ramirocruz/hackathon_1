# read deployConfig
# get ip,port from database.json given sensor location
# get name of the algoclass to run
# creat a client from ip,port
# create the algoclass(client) (humidityController)
import os
import json
import importlib

CONFIG_FILE_NAME = "deployConfig.json"

def getSensorIPPort(sensor_location:str,dbfileName):
    with open(dbfileName) as f:
        sensorDet = json.load(f)
        return sensorDet['location'][sensor_location]

def main():
    with open(CONFIG_FILE_NAME) as f:
        deploymentDetails = json.load(f)
        algoName = deploymentDetails['bindings']['algorithmClass']
        sensor_location = deploymentDetails['bindings']['sensor params']['location']
    
    listOfAddresses = getSensorIPPort(sensor_location,"database.json")

    classname = os.path.splitext(os.path.basename(listOfAddresses[0][-1]))[0]
    module = importlib.import_module(classname)    
    sensor_instance = getattr(module, classname)(listOfAddresses[0][0], listOfAddresses[0][1])

    classname = os.path.splitext(os.path.basename(algoName))[0]
    module = importlib.import_module(classname)    
    algo_instance = getattr(module, classname)(sensor_instance)

if __name__ == "__main__":
    main()