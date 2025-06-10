import os, json, requests
from dotenv import load_dotenv


load_dotenv(dotenv_path="./.env")

API_KEY = os.environ["API_KEY"]
BASE_URL = os.environ.get("BASE_URL")
endpoints = {
    "businesses": "/businesses/search",
    "phone": "/businesses/search/phone",
}
headers = {"Authorization": f"Bearer {API_KEY}", "accept": "application/json"}
response = requests.get(
    headers=headers,
    url=BASE_URL + endpoints["businesses"],
    params={"location": "New York, NY", "term": "starbucks", "limit": "20"},
)
if response.status_code == 200:
    businesses = response.json()["businesses"]
    with open("./yelpdata.json", "w+") as file:
        file.write(json.dumps(businesses))
else:
    print(response.status_code, ":", response.text)
