[![GitHub Activity](https://img.shields.io/github/commit-activity/y/PepegaBruh/Cryptotracker?style=for-the-badge)](https://github.com/PepegaBruh/CryptoTracker/commits/main)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
# CryptoTracker ⚠️  ⚠️  ⚠️ 

⚠️ Given the latest issues with the API, I am rewriting the project in spite of the API written by [fawazahmed0](https://github.com/fawazahmed0/currency-api). At the moment the component is not working !!!

Development is happening in the branch [new_api](https://github.com/BigNocciolino/CryptoTracker/tree/new_api)

# Installation

This integrantion is in the default repo, so now you can found it in default hacs, searching it

# Configuration

Please before configuring the integration visit the section [Available Fiat currency](#available-fiat-currency)

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
      name: dogecoin

    - compare: btc-eur
      name: bitcoin

    - compare: eth-eur
      name: ethereum

    #Example of the alternative formula
    - compare: eur-doge
      name: dogecoin

    - compare: eur-btc
      name: bitcoin

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

## Available fiat currency 

| Fiat currency | Abbreviation |
|:--------------:|:-----------:
| Armenian Dram | AMD |
| Australian dollar | AUD |
| Bosnia and Herzegovina convertible mark | BAM |
| Brazilian real | BRL |
| Canadian dollar | CAD |
| Euro | EUR |
| Pound sterling | GBP |
| Gambian dalasi | GMD |
| Indonesian rupiah | IDR |
| Japanese yen | JPY |
| Kazakhstani tenge | KZT |
| Nigerian naira | NGN | 
| Polish złoty | PLN |
| Russian ruble | RUB |
| Solomon Islands dollar | SBD | 
| Turkish lira | TRY |
| Ukrainian hryvnia | UAH |
| United States dollar | USD |
