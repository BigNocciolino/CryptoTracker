import requests
import json
import logging
from homeassistant.util import Throttle

from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    SensorEntity,
    SensorEntityDescription,
    STATE_CLASS_MEASUREMENT,
)
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from homeassistant.const import (
    ATTR_ATTRIBUTION,
    CONF_NAME,
    STATE_UNKNOWN,
    CONF_RESOURCES,
    CONF_SCAN_INTERVAL,
)

from .const import (
    URL,
    DEFAULT_COMPARE,
    ICON,
    DEFAULT_SCAN_INTERVAL,
    ATTRIBUTION,
    CONF_COMPARE,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_RESOURCES, default=[]): vol.All(
        cv.ensure_list,
        [
            vol.Schema({
                vol.Required(CONF_COMPARE, default=DEFAULT_COMPARE): cv.string,
                vol.Optional(CONF_NAME, default=DOMAIN): cv.string,
                vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): cv.time_period,
            })
        ],
    )
})

def get_data(compare):
    """Get The request from the api"""

    parsed_url = URL.format(compare)
    #The headers are used to simulate a human request
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'}

    req = ""
    try:
        req = requests.get(parsed_url, headers=headers, timeout=10)
    except Exception as e:
        _LOGGER.error(e)

    resp_parsed = ""
    if (req.status_code == 200):
        #The request is ok
        jsone = req.json()
        resp = json.dumps(jsone)
        resp_parsed = json.loads(resp)

        if (resp_parsed["success"]):
            return resp_parsed["ticker"]["price"]
        else:
            _LOGGER.warning("Recivied an error in the ticker, if the issue persist consider to open a ticket")
            _LOGGER.error(resp_parsed["error"])
            return False
    else:
        return False

def parse_unit_of_mesurament(compare):
    """Parse the input for the unit of mesurament"""

    s = compare.split("-")

    return s[1].upper()

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Setup the currency sensor"""

    entities = []

    for resource in config[CONF_RESOURCES]:
        compare_ = resource[CONF_COMPARE]
        name = resource[CONF_NAME]
        scan_interval = resource[CONF_SCAN_INTERVAL]

        entities.append(
            CurrencySensor(hass, name, compare_, scan_interval)
        )

    async_add_entities(entities, True)

class CurrencySensor(SensorEntity):
    """Main class for curency sensor"""

    def __init__(self, hass, name, compare, scan_interval):
        """Inizialize sensor"""
        self._state = STATE_UNKNOWN
        self._name = name
        self._hass = hass
        self._scan_interval = scan_interval
        self._compare = compare
        self.entity_description = (
            SensorEntityDescription(
                # Enable long term data
                key = "crypto",
                state_class=STATE_CLASS_MEASUREMENT,
            )
        )
        self.update = self._update

    @property
    def name(self):
        """Return the name sensor"""
        return self._name

    @property
    def icon(self):
        """Return the default icon"""
        return ICON

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return parse_unit_of_mesurament(self._compare)

    @property
    def state(self):
        """Return the state of the sensor"""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes of the sensor."""
        return {ATTR_ATTRIBUTION: ATTRIBUTION}

    def _update(self):
        """Get the latest update fron the api"""

        data = get_data(self._compare)

        if data != False:
            self._state = data
        else: 
            return False