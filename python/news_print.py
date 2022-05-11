from asyncore import write
import keys
active_NYT_KEY = keys.NYT_KEY

import requests
import json

def execute():
#   print(active_NYT_KEY)
    requestUrl = "https://api.nytimes.com/svc/topstories/v2/home.json?api-key="+active_NYT_KEY
#   print(requestUrl)
    requestHeaders = {
      "Accept": "application/json"
  }

    nyt_out = requests.get(requestUrl, headers=requestHeaders)

    data = json.loads(nyt_out.text) 
    for article in data['results']:
        print(article['title'])
        print(article['abstract'])
        print(article['short_url'])
        print(article['published_date'])

if __name__ == "__main__":
    execute()