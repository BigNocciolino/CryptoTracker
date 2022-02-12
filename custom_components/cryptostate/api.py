"""Crypto trakcer api client"""
from email import header
import logging
import asyncio
import socket
from typing import Optional
import aiohttp
from .const import BASED_CURR_VALUE_URL, ALL_CURR_URL


_LOGGER: logging.Logger = logging.getLogger(__package__)
HEADERS = {"Content-type": "application/json; charset=UTF-8"}


class CryptoTrackerApiClient:
    """Crypto tracker api class"""

    def __init__(self, crypto: str, base: str, session: aiohttp.ClientSession) -> None:
        """API client"""
        self._crypto = crypto
        self._base = base
        self._session = session

    async def async_get_data(self) -> dict:
        """Get the data from the api"""
        url = BASED_CURR_VALUE_URL.format(crypto=self._crypto, base=self._base)
        return await self.api_wrapper(method="values", url=url, headers=HEADERS)

    async def async_get_currecy_list(self) -> dict:
        url = ALL_CURR_URL
        return await self.api_wrapper(method="currencies", url=url, headers=HEADERS)

    async def api_wrapper(self, method: str, url: str, headers: dict = {}) -> dict:
        """Get information from the api"""
        try:
            if method == "values":
                res = await self._session.get(url, headers=headers)
                return await res.json()
            if method == "currencies":
                res = await self._session.get(url, headers=headers)
                return await res.json()
        except asyncio.TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

        except (KeyError, TypeError) as exception:
            _LOGGER.error(
                "Error parsing information from %s - %s",
                url,
                exception,
            )
        except (aiohttp.ClientError, socket.gaierror) as exception:
            _LOGGER.error(
                "Error fetching information from %s - %s",
                url,
                exception,
            )
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Something really wrong happened! - %s", exception)
