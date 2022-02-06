import json
import logging
import aiohttp

from .const import BASED_CURR_VALUE_URL

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}


class CryptoTrackerApiClient:
    def __init__(self, crypto, base, session: aiohttp.ClientSession) -> None:
        self._crypto = crypto
        self._base = base
        self._session = session
        self._url = BASED_CURR_VALUE_URL.format(crypto=self._crypto, base=self._base)

        async def async_degt_data(self):
            return await self.api_wrapper()

        async def api_wrapper(self):
            try:
                res = await self._session.get(self._url, headers=HEADERS)
                _LOGGER.info("URL: %s", self._url)
                _LOGGER.info("RESPONSE: %s", str(res.json()))
                return await res.json()
            except Exception as e:
                _LOGGER.error(" Error here %s", e)
