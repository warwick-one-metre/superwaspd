
## SuperWASP weather proxy daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/superwaspd.svg?branch=master)](https://travis-ci.org/warwick-one-metre/superwaspd)

Part of the observatory software for the Warwick one-meter, NITES, and GOTO telescopes.

`superwaspd` is a Pyro frontend for querying the SuperWASP weather log via http.

`superwasp` is a commandline utility that queries the SuperWASP weather log daemon.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software setup
After installing `observatory-superwasp-server`, the `superwaspd` must be enabled using:
```
sudo systemctl enable superwaspd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start superwaspd.service
```

The URL for the superwasp weather log is hardcoded in `superwaspd`.  If this ever changes it should be updated here.
