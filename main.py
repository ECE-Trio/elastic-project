from lib import elastic
import requests, json

es = elastic('http://localhost:9200/shakespeare-catalog-2/_search')

q={
    "query":{
      "match":{
        "text_entry.english":{
            "query":"The edge of war",
            "minimum_should_match":"2"
        }
      }
    }
  }

result, status = es.query(q)

es.printResponse()