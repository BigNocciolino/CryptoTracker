from email.policy import default
from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol
from .const import DOMAIN, CONF_BASE, CONF_CRYPTO, DEFAULT_NAME
from homeassistant.const import CONF_NAME


class CryptoTrackerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Crypto Tracker config flow"""

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input=None):

        self._errors = {}

        # TODO validate and split values

        if user_input is not None:
            valid = await self._test_credentials(
                user_input[CONF_CRYPTO], user_input[CONF_BASE]
            )
            if valid:
                return self.async_create_entry(
                    title=user_input[CONF_NAME], data=user_input
                )
            else:
                self._errors["base"] = "invalid_format"

            return await self._show_config_form(user_input)

        user_input = {}
        # Provide defaults for form
        user_input[CONF_CRYPTO] = ""
        user_input[CONF_BASE] = ""
        user_input[CONF_NAME] = ""

        return await self._show_config_form(user_input)

    async def _show_config_form(self, user_input):  # pylint: disable=unused-argument
        """Show the configuration form to edit location data."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_CRYPTO, default=user_input[CONF_CRYPTO]): str,
                    vol.Required(CONF_BASE, default=user_input[CONF_BASE]): str,
                    vol.Optional(CONF_NAME, default=DEFAULT_NAME): str,
                }
            ),
            errors=self._errors,
        )

    async def _test_credentials(self, crypto, base):
        """Return true if credentials is valid."""
        return True
