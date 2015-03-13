__author__ = 'mpetyx'

import json

import requests

base_server = "https://demo2.openi-ict.eu"
next_path = "/api/v1/types?offset=0"

mapping = {}
while next_path:
    result_types = requests.get(base_server + next_path)
    next_path = result_types.json()['meta']['next']
    
    for type in result_types.json()['result']:
        # pprint.pprint( type )
        mapping[type['@context'][0]['@property_name']] = type['@id']

with open('data.json', 'w') as outfile:
    json.dump(mapping, outfile, sort_keys=True, indent=4, ensure_ascii=False)
