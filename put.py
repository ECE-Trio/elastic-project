from lib import elastic
import requests, json

es = elastic('localhost:9200/neil/test/_bulk?pretty')

with open('data.json') as json_file:
    for line in json_file:
        jsonData = json.loads(line)

        print("\nSending...")
        print(jsonData)
        es.send(jsonData)