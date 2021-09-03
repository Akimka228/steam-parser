import requests
import json

headers = {
    'content-type': "application/json",
    'x-apikey': "",
    'cache-control': "no-cache"
    }


def add_following_link(url, user_id):
    db_url = "https://practicebot-a0f1.restdb.io/rest/following-pages"
    payload = json.dumps({"link": db_url, "user-id": user_id})
    response = requests.request("POST", db_url, data=payload, headers=headers)
    return response.ok

