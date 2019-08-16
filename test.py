import json
import requests

api_url = 'http://127.0.0.1:8000/reviews/3'
data = {
        "id": 0,
        "restaurant_id": 0,
        "name": "Amy",
        "createdAt": 1504095567183,
        "updatedAt": 1504095567183,
        "rating": 5,
        "comments": "TEST."
      }


req = requests.post(api_url, json=data)
