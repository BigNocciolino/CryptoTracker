from datetime import timedelta
import requests
import json
from collections import defaultdict
import logging

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.const import (
    CONF_NAME,
)

_LOGGER = logging.getLogger(__name__)

ICON = "mdi:cash-multiple"

SCAN_INTERVAL = timedelta(minutes=5)

ATTRIBUTION = "data provided by cryptonator api"

DOMAIN = "Crypto"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME): cv.string
})

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

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the currency sensor"""
    name = config.get(CONF_NAME)

    add_entities([CurrencySensor(toPython(), DOMAIN, 10)], True)

class CurrencySensor(Entity):
    
    def __init__(self, state, name, interval):
        """Inizialize sensor"""
        self._state = state
        self._name = name
        self._update = Throttle(interval)(self._update)

    @property
    def name(self):
        """Return the name sensor"""
        return self._name or DOMAIN

    @property
    def icon(self):
        """Return the default icon"""
        return ICON

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return "EUR"

    @property
    def update(self):
        """Get the latest update fron the api"""

        self._state = toPython() 