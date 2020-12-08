#!/usr/bin/python3
# -*- coding: utf-8 -*-

from influxdb import InfluxDBClient
from datetime import datetime
from pytz import timezone

def WriteDB(dbname, meas, field, data, time=None):
    if time is None:
        time = datetime.now(timezone('UTC')).isoformat('T').split('.')[0]
    json_body = [
        {
            "measurement": meas,
            "time": time,
            "tags": {
                "hard": "RasPi4+"
            },
            "fields": {
                field: data
            }
        }
    ]
    client = InfluxDBClient(database=dbname)
    client.write_points(json_body)
