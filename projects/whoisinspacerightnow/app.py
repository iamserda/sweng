import requests
import json


def get_data(url="http://api.open-notify.org/astros.json"):
    if not url:
        return
    try:
        response = requests.get(url)
        return {"data": response.text}

    except Exception as err:
        print(f"Some error occured with this request.\nRead more:\n{err}")
        return {"data": None}

def save_data():
    with open("opennotify-api-data.json", "w+") as filew:
        data = get_data()["data"]
        
        if data is None:
            print("Failed!")
        
        if data:
            filew.write(data)
            print("Success!")

with open("./opennotify-api-data.json", "r") as file_reader:
    try:
        file_content = file_reader.read()

        if not file_content:
            save_data()
            file_content = file_reader.read()
        
        data = json.loads(file_content)
        print(f"Currently, there are {data['number']} astronauts on active missions in space!")
        
        for astronaut in data["people"]:
            print(f"Astronaut '{astronaut['name']}' is on a mission on '{astronaut['craft']}'")
    
    except Exception as err:
        print("Some error occurred!")
