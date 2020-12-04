from lib import elastic
import requests, json

#Will do the same as this command :
#curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/testpython/_bulk?pretty' --data-binary @data.json

es = elastic('http://localhost:9200/testpython/_bulk?pretty')


json_file = open('data.json')
data=json_file.readlines()
dataString="".join(data)

es.send(dataString)