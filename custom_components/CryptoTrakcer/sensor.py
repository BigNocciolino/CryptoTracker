from datetime import timedelta
import requests
import json
import logging

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

ICON = "mdi:cash-multiple"

SCAN_INTERVAL = timedelta(minutes=5)

ATTRIBUTION = "Data provided by cryptonator api"

DOMAIN = "Crypto"

# TODO add a config to get the request to do
compareCurrency = ["eur", "usd"]
needCompare = ["doge","btc","eth"]

url = "https://api.cryptonator.com/api/ticker/{0}-{1}"

def getRequest(toCompare, comapred):
    """get The request from the api"""
    parsedUrl = url.format(toCompare, comapred)
    #The headers are used to simulate a human request
    req = requests.get(parsedUrl, headers={"User-Agent": "Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)"}) 

    return req

def toJson():
    """Transofrm the request into a json"""
    jsone = []
    #This is for
    jsone.append(getRequest("doge", "eur").json())
    return jsone
    
def toPython():
    """Tranform json in python library"""
    jsone = toJson()
    resp = json.dumps(jsone)
    respParsed = json.loads(resp)

    return respParsed["ticker"]["price"]

def setup_platform(hass, config, add_entity, discovery_info= True):
    """Setup the currency sensor"""

    add_entity([CurrencySensor(self, DOMAIN, toPython())])

class CurrencySensor(Entity):
    
    def __init__(self, data):
        """Inizialize sensor"""
        self.data = data
        self.name = name

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