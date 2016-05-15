# Geocoding with Bing

## Setup

Install requests module:

```shell
sudo pip install requests
```

Create settings file and add your API key:

```shell
cat settings.ini
```

```
[Bing]
Key=<your api key>
```

## Usage

Test file with list of places:

```shell
cat data/places.txt
```

```
Alphabet Inc.
```

```shell
./driver.py data/places.txt
```

```
```

### Misc

Simple request:

```
http://dev.virtualearth.net/REST/v1/Locations?q=Greenville&maxResults=10&key=BingMapsKey
```

