"""Const used by CryptoTracker"""
from __future__ import annotations

from datetime import timedelta

# With this url we can get all the currency names that are available
ALL_CURR_URL = (
    "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
)
# We format this url with the vale we want to convert the currency with
BASED_CURR_VALUE_URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{crypto}/{base}.json"

VERSION = "2.0.0"

CONF_COMPARE = "compare"

ICON = "mdi:cash-multiple"

DEFAULT_SCAN_INTERVAL = timedelta(days=1)

ATTRIBUTION = "Data provided by fawazahmed0 api"

DEFAULT_COMPARE = "btc-eur"

DOMAIN = "cryptostate"

NAME = DOMAIN

DEFAULT_NAME = NAME
