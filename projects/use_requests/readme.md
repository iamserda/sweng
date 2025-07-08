# use_requests

A simple Python project demonstrating how to use the `requests` library for making HTTP requests.

## Features

- Perform GET, POST, PUT, and DELETE requests
- Handle JSON responses
- Basic error handling

## Requirements

- Python 3.7+
- `requests` library

## Installation

```bash
pip install pipenv
pipenv install requests
pipenv shell
python3 ./app.py
```

## Usage

```python
import requests
import json

def get_data():
    try:
        resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if resp.status_code == 200:
            data = resp.json()
            print(data)
            # Uncomment the following lines to save the JSON response to a file:
            # with open("./data.json", "w+") as file:
            #     json.dump(data, file)
        else:
            raise ConnectionError(f"Failed to fetch data: status code {resp.status_code}")
    except Exception as err:
        print(f"Error: {err}.")

get_data()
```

## License

MIT License