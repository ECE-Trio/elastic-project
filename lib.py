import requests, json

class elastic():
  def __init__(self, url):
    self.url = url
    self.headers = {'Content-Type': 'application/json'}
    self.result={}
    self.status=0

  def query(self, queryJson):
    data = json.dumps(queryJson)

    try:
      res = requests.get(url=self.url, data=data, headers=self.headers)

      self.status=res.status_code
      if self.status==200 :
        self.result = res.content
        self.result = self.result.decode('utf-8')
        self.result = json.loads(self.result) #convert to json
        print("Ok")
      else:
        self.result={}
        print("Error with response")

      return self.result, self.status

    except:
      self.result={}
      print("Error making request")
      return {},-1


  def printResponse(self):
    if self.status==200 :
      print(json.dumps(self.result, indent=2, sort_keys=True))
    else:
      print("No valid response to print")
      self.result={}
