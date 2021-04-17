[![GitHub Activity](https://img.shields.io/github/commit-activity/y/PepegaBruh/CryptoTrakcer?style=for-the-badge)](https://github.com/PepegaBruh/CryptoTrakcer/commits/main)
# CryptoTracker

This integration use the [Cryptonator api](https://www.cryptonator.com/api), that's cover 300+ cryptocurrencies from 16 exchanges.

You can use it to track the price of a cryptocurrency and you can customize it as you see fit

# Installation

For now you must add the custom repository to your hacs installation.

# Configuration

To activate this extension you can put this in your configuration file "configuration.yml"

This is an example of a base configuration, you can set the comparison.

To correctly set the integration in the `- compare:` you mast insert thhis forula `{CURRENCY}` **-** `{FIAT CURRENCY}`  or mabye you can invert this formula.

**Alternative you can compare two cryptocurrencies**

```yaml
sensor:
- platform: cryptostate
  resource:
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

[Example][https://github.com/PepegaBruh/CryptoTracker/blob/main/images/example.png]

### Code

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