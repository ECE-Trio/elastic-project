
# Elastic project
ECE 2020, Gr1, SubGroup 4
Composed of
- DALMASSO Olivia
- DIREZ Alexis
- SEGARD Neil

***
### Adding data
This python script will put json data (imported from a .json file) into ElasticSearch.

The program is equivalent to :

`curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/python/_bulk?pretty' --data-binary @data.json`

### Retrieving data
Then it will make a request on the previously added data, with the following request :
```
{
    "query":{
       "match":{
          "account_number":13
       }
    }
}
```
