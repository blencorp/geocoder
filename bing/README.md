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
The Library of Congress
Mountain View, CA
```

```shell
./driver.py data/places.txt
```

```
Library of Congress, DC|38.8876113892|-77.0047073364
Mountain View, CA|37.3896713257|-122.081596375
```

