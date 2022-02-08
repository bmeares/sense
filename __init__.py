#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Meerschaum plugin for the Raspberry Pi Sense HAT.
"""

__version__ = '1.0.3'
required = ['sense-hat']

def register(pipe, **kw):
    from .config import sense_config
    return {'columns': sense_config()['columns']}

_sense = None
def fetch(pipe, **kw):
    import datetime
    from sense_hat import SenseHat
    from .config import sense_config
    global _sense
    if _sense is None:
        _sense = SenseHat()

    sensor_id = sense_config()['sensor_id']

    return {
        'utc_datetime' : [datetime.datetime.utcnow()],
        'sensor_id' : [sensor_id],
        'temperature' : [_sense.get_temperature()],
        'humidity' : [_sense.get_humidity()],
        'pressure' : [_sense.get_pressure()],
    }
