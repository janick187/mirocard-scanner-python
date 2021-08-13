mirocard-scanner-python
===============

This repository contains simple python3 scripts to detect MiroCard beacons and provides endpoints to access temperature and humidity values over an API.

## Dependencies

* Python3
* [pybluez](https://github.com/pybluez/pybluez)

For Python 3, you may need to use `pip3`:

```
$ sudo apt-get install python3-pip libglib2.0-dev
$ sudo pip3 install bluepy
```

After installing, you can run the following python script:

```
$ sudo python3 mirocard-scanner.py
```

## RUN Flask web server on RPi
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run -h [RPi IP] -p 8080
```
Access latest humidity and temperature values measured by MiroCard (need to be connected to same network as RPi):
```
GET http://[RPi IP]:8080/temperature
GET http://[RPi IP]:8080/humidity
```
