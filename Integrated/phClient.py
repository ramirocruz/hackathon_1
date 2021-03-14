import requests

def makeUrl(ip,port):
    return "http://" + str(ip)+":"+port
    
class phClient:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
    
    def getPH(self):
        url = makeUrl(self.ip,self.port)
        res = requests.post(url,json={"func":"getPH"})
        return res.json()["data"]
    
    def setSprinkler(self):
        url = makeUrl(self.ip,self.port)
        res = requests.post(url,json={"func":"setSprinkler"})