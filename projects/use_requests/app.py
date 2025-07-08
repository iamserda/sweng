import requests
import json


def get_data():
    try:
        resp = requests.get("https://jsonplaceholder.typicode.com/posts")
        if resp.status_code == 200:
            data = resp.json()
            with open("./data.json", "w+") as file:
                json.dump(data, file)
        else:
            raise ConnectionError(
                f"Failed to fetch data: status code {resp.status_code}"
            )
    except Exception as err:
        print(f"Error: {err}.")


def put_data():

    try:
        new_data = {
            "userId": 1,
            "id": 1,
            "title": "Mortal Kombat: Deadly Alliance",
            "body": "Roman Church",
        }
        resp = requests.put(
            "https://jsonplaceholder.typicode.com/posts/1", json=new_data
        )
        data = resp.json()
        print(resp.status_code, data)
    except Exception as err:
        print(f"Error: {err}.")


get_data()
put_data()
