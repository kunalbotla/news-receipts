from asyncore import write
import keys
active_NYT_KEY = keys.NYT_KEY

import requests
import json
from random import randrange

def execute():
#   print(active_NYT_KEY)
    requestUrl = "https://api.nytimes.com/svc/topstories/v2/home.json?api-key="+active_NYT_KEY
#   print(requestUrl)
    requestHeaders = {
      "Accept": "application/json"
  }

    nyt_out = requests.get(requestUrl, headers=requestHeaders)
    data = json.loads(nyt_out.text)

    pick_rand_article(data)

def pick_rand_article(data):
    rand_article = data['results'][randrange(len(data['results']))]
    print(rand_article['title'])
    print(rand_article['abstract'])
    print(rand_article['short_url'])
    print(rand_article['published_date'])

if __name__ == "__main__":
    execute()