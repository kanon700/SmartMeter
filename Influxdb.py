#!/usr/bin/python3
# -*- coding: utf-8 -*-

from influxdb import InfluxDBClient


def WriteDB(dbname, meas, field, data):
    json_body = [
        {
            "measurement": meas,
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
