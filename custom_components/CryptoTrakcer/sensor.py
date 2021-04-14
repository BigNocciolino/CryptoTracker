from datetime import timedelta
import requests
import json
from collections import defaultdict
import logging

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.aiohttp_client import async_create_clientsession
import voluptuous as vol
#TODO Switch to Fiat and crypto
from homeassistant.const import (
    CONF_NAME,
    STATE_UNKNOWN,
    CONF_CURRENCY,
)

_LOGGER = logging.getLogger(__name__)

ICON = "mdi:cash-multiple"

SCAN_INTERVAL = timedelta(seconds=30)

ATTRIBUTION = "Data provided by cryptonator api"

DEFAULT_FIAT = "EUR"

DEFAULT_CURRENCY = "DOGE"

DOMAIN = "cryptostate"

CONF_FIAT = "fiat"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_CURRENCY, default=DEFAULT_CURRENCY): cv.string,
    vol.Required(CONF_FIAT, default=DEFAULT_FIAT): cv.string,   
    vol.Optional(CONF_NAME, default=DOMAIN): cv.string,
})

url = "https://api.cryptonator.com/api/ticker/{0}-{1}"

def parseUrl(crypto, fiat):
    parsedUrl = url.format(crypto, fiat)

    return parseUrl


def getData(url):
    """Get The request from the api"""
    #The headers are used to simulate a human request
    req = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)"}) 

    jsone = req.json()
    resp = json.dumps(jsone)
    respParsed = json.loads(resp)

    return respParsed["ticker"]["price"]

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the currency sensor"""
    name = config.get(CONF_NAME)
    fiat = config.get(CONF_FIAT)
    currency = config.get(CONF_CURRENCY)

    session = parseUrl(currency, fiat)

    add_entities([CurrencySensor(hass, name, session)], True)

class CurrencySensor(SensorEntity):
    
    def __init__(self, hass, name, session):
        """Inizialize sensor"""
        self._state = STATE_UNKNOWN
        self._name = name
        self._hass = hass
        self._session = session

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
    def state(self):
        """Return the state of the sensor"""
        return self._state

    def update(self):
        """Get the latest update fron the api"""

        self._state = getData(self._session)
