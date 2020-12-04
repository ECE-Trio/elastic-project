from lib import elastic #self made library
import requests, json, time

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

