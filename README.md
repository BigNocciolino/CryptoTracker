[![GitHub Activity](https://img.shields.io/github/commit-activity/y/PepegaBruh/Cryptotracker?style=for-the-badge)](https://github.com/PepegaBruh/CryptoTracker/commits/main)

# CryptoTracker

This integration use the [Cryptonator api](https://www.cryptonator.com/api), that's cover 300+ cryptocurrencies from 16 exchanges.

You can use it to track the price of a cryptocurrency and you can customize it as you see fit

# Installation

This integrantion is in the default repo, so now you can found it in default hacs, searching it

# Configuration

To activate this extension you can put this in your configuration file "configuration.yml"

This is an example of a base configuration, you can set the comparison.

To correctly set the integration in the `- compare:` you mast insert this forula `{CURRENCY}` **-** `{FIAT CURRENCY}`  or mabye you can invert it.

**Alternative you can compare two cryptocurrencies**

```yaml
sensor:
- platform: cryptostate
  resources:
    #Example of the first formula
    - compare: doge-eur
      name: dogecon

    - compare: btc-eur
      name: bitboin

    - compare: eth-eur
      name: ethereum

    #Example of the alternative formula
    - compare: eur-doge
      name: dogecon

    - compare: eur-btc
      name: bitboin

    - compare: eur-eth
      name: ethereum
```

## Example of my configuration

![Example](https://github.com/PepegaBruh/CryptoTracker/blob/main/images/example.png?raw=true)

### Code

**I'm using the [mini-graph-card](https://github.com/kalkih/mini-graph-card) custom integration to create a cool graph**

```yaml
type: 'custom:mini-graph-card'
entities:
  - sensor.dogecoin
name: Dogecoin
line_color: '#735119'
line_width: 2
hours_to_show: 5
decimals: 8
points_per_hour: 10
animate: true
icon: 'mdi:dog'
show:
  labels: false
color_thresholds:
  - value: 0.08
    color: '#008f39'
  - value: 0.1
    color: '#ffff00'
  - value: 0.2
    color: '#ff0000'

```

## Available options

Available Options | Type | Default | Info
:-----------------|:----:|:-----:| :----:|
resource         | `list`  |  None   |You need this, is the enrypoint of the sensors
compare           | `string` | doge-eur  | Here you can insert the formula of the comparison
name:             | `string` | cryptostate  |You can set the name for this sensor 