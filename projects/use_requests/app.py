import requests
import json
from pathlib import Path
from flask import Flask, render_template, request

APP = Flask(__name__)


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


@APP.route("/", methods=["GET"])
def handle_home():
    return "<a href='/data'>Get Data</a>"


@APP.route("/data", methods=["GET"])
def handle_data():
    try:
        file_path = Path("./data.json")
        with open(file_path, "r") as file:
            return render_template("card.html", cards=json.load(file))
    except Exception as err:
        print(f"Error: {err}.")  # todo-logging
        return "<h1>Welcome to Flask App</h1>"


@APP.route("/q")
def handle_query_strings():
    # request is a flask module, not the 'requests' package from pypi.
    if request.args:
        arguments = request.args

    for key, *value in arguments:
        print(key, value)

    return "content"


if __name__ == "__main__":
    # put_data()
    # get_data()
    APP.run(host="0.0.0.0", port=8882, debug=True)
