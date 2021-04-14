from datetime import timedelta
import requests
import json
from collections import defaultdict
import logging

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
import homeassistant.helpers.config_validation as cv
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

CONF_ARG = "arg"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DOMAIN): cv.string,

    vol.Required(CONF_CURRENCY, default=DEFAULT_CURRENCY): vol.All(
        cv.ensure_list,
        [
            vol.Schema({
                vol.Optional(CONF_ARG):cv.string
            })
        ]
    )

#    vol.schema ({
#        vol.Required(CONF_CURRENCY, default=DEFAULT_CURRENCY): cv.string,
#        vol.Optional(CONF_ARG, default=DEFAULT_FIAT): cv.string,
#    })   
})

url = "https://api.cryptonator.com/api/ticker/{0}-{1}"

def getData(crypto, fiat):
    """Get The request from the api"""
    parsedUrl = url.format(crypto, fiat)
    #The headers are used to simulate a human request
    req = requests.get(parsedUrl, headers={"User-Agent": "Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)"}) 

    jsone = req.json()
    resp = json.dumps(jsone)
    respParsed = json.loads(resp)

    return respParsed["ticker"]["price"]

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the currency sensor"""
    name = config.get(CONF_NAME)
    currency = config.get(CONF_CURRENCY)
    fiat = config.get(CONF_ARG)

    add_entities([CurrencySensor(hass, name, currency, fiat)], True)

class CurrencySensor(SensorEntity):
    
    def __init__(self, hass, name, currency, fiat):
        """Inizialize sensor"""
        self._state = STATE_UNKNOWN
        self._name = name
        self._hass = hass
        self._currency = currency
        self._fiat = fiat

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

        self._state = getData(self._currency, self.fiat)
