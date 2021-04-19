#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Implement the Meerschaum fetch method to read from the Sense HAT and return a dictionary.
"""

_sense = None

def fetch(pipe, **kw):
    import datetime
    from sense_hat import SenseHat
    from .config import sense_config
    global _sense
    if _sense is None:
        _sense = SenseHat()

    if not pipe.columns:
        pipe.columns = sense_config()['columns'].copy()
        pipe.edit()
    sensor_id = sense_config()['sensor_id']

    return {
        'utc_datetime' : [datetime.datetime.utcnow()],
        'sensor_id' : [sensor_id],
        'temperature' : [_sense.get_temperature()],
        'humidity' : [_sense.get_humidity()],
        'pressure' : [_sense.get_pressure()],
    }
