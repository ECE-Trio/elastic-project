from lib import elastic
import requests, json, time

"""
Will do the same as this command :
curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/testpython/_bulk?pretty' --data-binary @data.json

And then will retrieve one of this data with a query
"""

##Adding data
es = elastic('http://localhost:9200/python/_bulk?pretty')

json_file = open('data.json')
data=json_file.readlines()
dataString="".join(data)

status = es.send(dataString)
if status==200 :
    print("Ok")


#Wait before retrieving data
time.sleep(1)

##Retrieving data
print("\nRetrieving data")
es = elastic('http://localhost:9200/python/_search')

q={
    "query":{
      "match":{
        "account_number":13
      }
    }
  }

response, status = es.query(q)

elastic.printResponse(response)

