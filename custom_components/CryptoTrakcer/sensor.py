import requests
import json
import logging
from homeassistant.util import Throttle

from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    SCAN_INTERVAL,
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

SCAN_INTERVAL = DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_RESOURCES, default=[]): vol.All(
        cv.ensure_list,
        [
            vol.Schema({
                vol.Required(CONF_COMPARE, default=DEFAULT_COMPARE): cv.string,
                vol.Optional(CONF_NAME, default=DOMAIN): cv.string,
            })
        ],
    )
})


def get_data(compare):
    """Get The request from the api"""

    parsed_url = URL.format(compare)
    #The headers are used to simulate a human request
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    req = ""
    try:
        req = requests.get(parsed_url, headers=headers, timeout=10)
        req.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        _LOGGER.error(errh)
    except requests.exceptions.ConnectionError as errc:
        _LOGGER.error(errc)
    except requests.exceptions.Timeout as errt:
        _LOGGER.error(errt)
    except requests.exceptions.RequestException as err:
        _LOGGER.error(err)

    resp_parsed = ""
    if (req.status_code == 200):
        #The request is ok
        jsone = req.json()
        resp = json.dumps(jsone)
        resp_parsed = json.loads(resp)

        if (resp_parsed["success"]):
            return resp_parsed["ticker"]["price"]
        else:
            _LOGGER.warning("Recivied an error in the ticker")
            _LOGGER.error(resp_parsed["error"])
            return resp_parsed["error"]
    else:
        _LOGGER.error(f"Request returned a bad error code {req.status_code}")

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

        entities.append(
            CurrencySensor(hass, name, compare_)
        )

    async_add_entities(entities, True)

class CurrencySensor(SensorEntity):
    """Main class for curency sensor"""

    def __init__(self, hass, name, compare):
        """Inizialize sensor"""
        self._state = STATE_UNKNOWN
        self._name = name
        self._hass = hass
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

        self._state = get_data(self._compare)
