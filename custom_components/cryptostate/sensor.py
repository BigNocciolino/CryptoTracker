"""Sensor platform for integration_blueprint."""
from homeassistant.components.sensor import SensorEntity

from .const import DOMAIN
from homeassistant.const import CONF_NAME
from .entity import CryptoTrackerEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    name = entry.data.get(CONF_NAME)
    async_add_devices([CryptoTrackerSensor(coordinator, entry, name)])


class CryptoTrackerSensor(CryptoTrackerEntity, SensorEntity):
    """integration_blueprint Sensor class."""

    def __init__(self, coordinator, config_entry, name):
        super().__init__(coordinator, config_entry)
        self._name = name

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self._name}"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        # TODO redifine default value,
        return self.coordinator.data.get("eur")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return "mdi:format-quote-close"
