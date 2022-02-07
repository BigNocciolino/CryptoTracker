"""Sensor platform for integration_blueprint."""
from homeassistant.components.sensor import SensorEntity

from .const import DEFAULT_NAME, DOMAIN
from .entity import CryptoTrackerEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([CryptoTrackerSensor(coordinator, entry)])


class CryptoTrackerSensor(CryptoTrackerEntity, SensorEntity):
    """integration_blueprint Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_sensor"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        # TODO redifine default value,
        return self.coordinator.data["eur"]

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return "mdi:format-quote-close"
