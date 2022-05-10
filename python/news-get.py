# Pulling the top stories from the home page from the NYTimes API to a JSON file.

# See instructions for installing Requests module for Python
# https://requests.readthedocs.io/en/master/user/install/#install

import keys
active_NYT_KEY = keys.NYT_KEY

import requests

def execute():
#   print(active_NYT_KEY)
    requestUrl = "https://api.nytimes.com/svc/topstories/v2/home.json?api-key="+active_NYT_KEY
#   print(requestUrl)
    requestHeaders = {
      "Accept": "application/json"
  }

    response = requests.get(requestUrl, headers=requestHeaders)

    print(response.text)

if __name__ == "__main__":
    execute()