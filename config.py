#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Manage configuration for the Sense HAT plugin.
"""

def sense_config():
    from meerschaum.config import get_plugin_config, write_plugin_config
    _config = get_plugin_config(warn=False)
    if _config is None:
        import uuid
        _config = {
            'columns' : {
                'datetime' : 'utc_datetime',
                'id' : 'sensor_id',
            },
            'sensor_id' : str(uuid.uuid4()),
        }
        write_plugin_config(_config)
    return _config
