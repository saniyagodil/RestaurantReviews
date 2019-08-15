import json
import requests

api_url = 'http://127.0.0.1:8000/reviews/1'
data = {
        "id": 31,
        "restaurant_id": 1,
        "name": "Amy",
        "createdAt": 1504095567183,
        "updatedAt": 1504095567183,
        "rating": 5,
        "comments": "TEST."
      }


req = requests.post(api_url, json=data)
