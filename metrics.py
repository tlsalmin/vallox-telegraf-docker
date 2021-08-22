#!/usr/bin/env python

from importlib import util
import asyncio
from vallox_websocket_api import Client
import os

client = Client(os.environ['VALLOX_HOST'])

async def run():
    items_of_interest = {('A_CYC_TEMP_OUTDOOR_AIR', 'Outdoor air temperature', 'NUMBER|DECIMAL'),
            ('A_CYC_TEMP_EXHAUST_AIR', 'Exhaust air temperature', 'NUMBER|DECIMAL'),
            ('A_CYC_TEMP_EXTRACT_AIR', 'Extract air temperature', 'NUMBER|DECIMAL'),
            ('A_CYC_TEMP_SUPPLY_AIR', 'Supply air temperature', 'NUMBER|DECIMAL'),
            ('A_CYC_TEMP_SUPPLY_CELL_AIR', 'Supply air cell temperature', 'NUMBER|DECIMAL'),
            ('A_CYC_CO2_VALUE', 'CO2 Air value', 'NUMBER|INTEGER'),
            ('A_CYC_FAN_SPEED', 'Fan speed', 'NUMBER|INTEGER'),
            ('A_CYC_SUPPLY_EFFICIENCY', 'Supply efficiency', 'NUMBER|INTEGER'),
            ('A_CYC_MULTISENSOR_RH', 'Relative humidity', 'NUMBER|INTEGER'),
            ('A_CYC_SUPP_FAN_SPEED', 'Support fan speed', 'NUMBER|INTEGER')}

    metrics = await client.fetch_metrics([i[0] for i in items_of_interest])

    for i, item, in enumerate(items_of_interest):
        if i:
            print(',', end='')
        print("{}".format(item[1], ), end = '')
        if i == len(items_of_interest) - 1:
            print("")
    for i, item, in enumerate(items_of_interest):
        if i:
            print(',', end='')
        print("{}".format(metrics[item[0]]), end = '')
        if i == len(items_of_interest) - 1:
            print("")

asyncio.get_event_loop().run_until_complete(run())
