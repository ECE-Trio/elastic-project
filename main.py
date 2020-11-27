import sys
import requests, json, base64

##Parameter for the Requests
url = 'http://localhost:9200/shakespeare-catalog-2/_search'
headers = {'Content-Type': 'application/json'}

query = {
          "query":{
              "match":{
                "text_entry.english":{
                    "query":"The edge of war",
                    "minimum_should_match":"2"
                }
              }
          }
        }
data=json.dumps(query)

##Making request
print("Making request... ", end="")
try:
  res = requests.get(url=url, data=data, headers=headers)

  if res.status_code == 200: #ok
    content = res.content
    content = json.loads(content.decode('utf-8'))
    print("Done!\n")
    print("Result:\n")
    print(json.dumps(content, indent=2, sort_keys=True))
  else:
    print("Failed! (Error {})".format(res.status_code))
except:
    print("Failed! (Error making request)")

