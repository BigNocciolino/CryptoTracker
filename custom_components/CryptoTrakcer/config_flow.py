from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol
from .const import DOMAIN, CONF_COMPARE
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
            valid = await self._test_credentials(user_input[CONF_COMPARE])
            if valid:
                return self.async_create_entry(
                    title=user_input[CONF_NAME], data=user_input
                )
            else:
                self.errors = {"base": "invalid_format"}

            return await self._show_config_form(user_input)

        user_input = {}
        # Provide defaults for form
        user_input[CONF_COMPARE] = ""
        user_input[CONF_NAME] = ""

        return await self._show_config_form(user_input)

    # @staticmethod
    # @callback
    # def async_get_options_flow(config_entry):
    #     return BlueprintOptionsFlowHandler(config_entry)

    async def _show_config_form(self, user_input):  # pylint: disable=unused-argument
        """Show the configuration form to edit location data."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_COMPARE, default=user_input[CONF_COMPARE]): str,
                    vol.Optional(CONF_NAME, default=user_input[CONF_NAME]): str,
                }
            ),
            errors=self._errors,
        )

    async def _test_credentials(self, compare):
        """Return true if credentials is valid."""
        if len(compare) == 7:
            return True
        else:
            return False


# class BlueprintOptionsFlowHandler(config_entries.OptionsFlow):
#     """Blueprint config flow options handler."""

#     def __init__(self, config_entry):
#         """Initialize HACS options flow."""
#         self.config_entry = config_entry
#         self.options = dict(config_entry.options)

#     async def async_step_init(self, user_input=None):  # pylint: disable=unused-argument
#         """Manage the options."""
#         return await self.async_step_user()

#     async def async_step_user(self, user_input=None):
#         """Handle a flow initialized by the user."""
#         if user_input is not None:
#             self.options.update(user_input)
#             return await self._update_options()

#         return self.async_show_form(
#             step_id="user",
#             data_schema=vol.Schema(
#                 {vol.Required("sensor", default=self.options.get("sensor", True)): bool}
#             ),
#         )

#     async def _update_options(self):
#         """Update config entry options."""
#         return self.async_create_entry(
#             title=self.config_entry.data.get(CONF_COMPARE), data=self.options
#         )
