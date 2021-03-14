import requests

def makeUrl(ip,port):
    return "http://" + string(ip)+":"+port"
class humidityClient:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
    
    def getHumidity(self):
        url = makeUrl(self.ip,self.port)
        res = requests.post(url,json={"func":"getHumidity"})
        return res.json()["data"]
    
    def setSprinkler(self):
        url = makeUrl(self.ip,self.port)
        res = requests.post(url,json={"func":"setSprinkler"})