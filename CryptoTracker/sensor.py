from datetime import timedelta
import requests
import json
import logging

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

ICON = "mdi:cash-multiple"

SCAN_INTERVAL = timedelta(minutes=5)

ATTRIBUTION = "Data provided by cryptonator api"

# TODO add a config to get the request to do
compareCurrency = ["eur", "usd"]
needCompare = ["doge","btc","eth"]

url = "https://api.cryptonator.com/api/ticker/{0}-{1}"

def getRequest(toCompare, comapred):
    parsedUrl = url.format(toCompare, comapred)
    #The headers are used to simulate a human request
    req = requests.get(parsedUrl, headers={"User-Agent": "Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)"}) 

    return req

#def getStatusCode():
#   return getRequest(compareCurrency, needCompare).status_code

def toJson():
    jsone = []
    jsone.append(getRequest("doge", "eur").json())
    return jsone
    
def toPython():
    jsone = toJson()
    resp = json.dumps(jsone)
    respParsed = json.loads(resp)

    return respParsed["ticker"]["price"]

#def main():
#    jsone = toJson()
#
#    for i in range(len(jsone)):
#        resp = json.dumps(jsone[i])
#        respParsed = json.loads(resp)
#        if respParsed["success"] == True:
#            print("Comparing " + respParsed["ticker"]["base"] + " " + respParsed["ticker"]["target"])
#            print(json.dumps(jsone[i], indent=4, sort_keys=True))
#        else:
#            print ("Error parsing the request")

def setup_platform(hass, config, add_entity, discovery_info= True):
    """Setup the currency sensor"""

    data = CyrrencyData()
    dev = []

    dev.append(CurrencySensor(data))

    add_entity(dev, True)

class CurrencySensor(SensorEntity):
    
    def __init__(self, data):
        """Inizialize sensor"""
        self.data = data

    @property
    def name(self):
        """Return the name sensor"""
        return self.name

    @property
    def icon(self):
        """Return the default icon"""
        return ICON

    @property
    def update(self):
        """Get the latest update fron the api"""
        self.data.update()

        self.data = toPython() 

class CyrrencyData():
    """Get the latest update from the sensor"""

    def __init__(self):
        """Inizialize the data object"""
        self.ticker = None

    def update(self):
        """Get thelatest data from yhe api"""
        self.ticker = toPython()