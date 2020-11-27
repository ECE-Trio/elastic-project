import requests, json

class elastic():
  def __init__(self, url):
    self.url = url
    self.headers = {'Content-Type': 'application/json'}

  def query(self, queryJson):
    data = json.dumps(queryJson)

    try:
      res = requests.get(url=self.url, data=data, headers=self.headers)

      status=res.status_code
      if status==200 :
        response = res.content
        response = response.decode('utf-8')
        response = json.loads(response) #convert to json
        print("Ok")
      else:
        response={}
        print("Error with response")

      return response, status

    except:
      print("Error making request")
      return {},-1

  def printResponse(response):
    if response=={} :
      print("No valid response to print")
    else:
      print(json.dumps(response, indent=2, sort_keys=True))
