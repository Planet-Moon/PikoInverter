import requests
from requests.auth import HTTPBasicAuth
import re
import _pikocreds
from PowerSource import PowerSource

class Piko_inverter(PowerSource):
    def __init__(self, name:str, ip_address=_pikocreds.address,username=_pikocreds.usr,password=_pikocreds.pwd):
        PowerSource.__init__(self,name)
        self.ip_address = ip_address
        self.username = username
        self.password = password

    def __str__(self):
        return "Ip address: {}, power: {} W".format(self.ip_address,self.power)

    def read_data(self):
        return requests.get(self.ip_address,auth=HTTPBasicAuth(self.username,self.password))

    @property
    def power(self):
        try:
            daten = self.read_data()
            text = daten.text
            liste = text.split("\r\n")
        except:
            liste = [0]

        try:
            piko_pwr = int(re.findall("\d+",liste[45])[0])
        except:
            piko_pwr = 0
        return piko_pwr

if __name__ == "__main__":
    piko_inverter = Piko_inverter()
    print(piko_inverter)