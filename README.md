[![GitHub Activity](https://img.shields.io/github/commit-activity/y/PepegaBruh/CryptoTrakcer?style=for-the-badge)](https://github.com/PepegaBruh/CryptoTrakcer/commits/main)
# CryptoTracker

This is an integration for Home Assistant to track over 300 cryptocurrencies.

This integration use the [Cryptonator api](https://www.cryptonator.com/api), that's cover 300+ cryptocurrencies from 16 exchanges.

## Installation

For now you must add the custom repository to yout hacs installation.
## Configuration

To activate this extension you can put this in your configuration file "configuration.yml"

This is the base configuration file, only the `currency:` is required
```yaml
sensor:
- platform: cryptostate
  name: Dogecoin # This is option you can use this if you want
  currency: doge # This section is not case sensitive
  fiat: eur # This if for the conversion from the currency to money, you can also insert an other crypto
```
## Available options

Available Options | Type | Info
:-----------------|:----:|:-----:
name              |string | Use this to set a custom name to the sensor
currency          |string  | This is requred and you can set the compare currency
fiat              |string | This is optional, but by default is set to `eur`