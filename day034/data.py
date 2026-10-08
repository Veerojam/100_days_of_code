import requests

PARAMS = {
    "amount": 10,
    "type": "boolean",
}


r = requests.get("https://opentdb.com/api.php", params=PARAMS)
r.raise_for_status()
data = r.json()
question_data = data["results"]
