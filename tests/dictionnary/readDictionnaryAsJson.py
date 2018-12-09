#!/usr/bin/python

import json

f = open('data.json')
data = json.load(f)
f.close()

print(data)