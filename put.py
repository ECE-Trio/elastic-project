from lib import elastic
import requests, json

#curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/testpython/_bulk?pretty' --data-binary @data.json

es = elastic('http://localhost:9200/testpython/_bulk?pretty')


json_file = open('data.json')
data=json_file.readlines()
dataString="".join(data)
es.send(dataString)

#.read().splitlines()
with open('data.json') as json_file:
    for line in json_file:
        break
        jsonData = json.loads(line)

        print("\nSending...")
        print(jsonData)
        es.send(jsonData)