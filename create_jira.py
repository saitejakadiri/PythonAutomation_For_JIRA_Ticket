# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://saitejakadiri.atlassian.net/rest/api/3/issue"

API_TOKEN=""

auth = HTTPBasicAuth("saiteja4520@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My First Jira Ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    
    "issuetype": {
      "id": "10036"
    },
    "project": {
      "key": "SAI"
    },
    "summary": "First Jira Ticket",  
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))