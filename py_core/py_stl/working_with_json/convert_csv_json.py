import csv, json

data = []


def csv_to_json(csvfilepath="mycsvfile.csv", jsonfilepath="myjsonfile.json"):
    with open(csvfilepath) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            number, name, country, nickname = row
            data.append(
                {
                    "number": number,
                    "name": name,
                    "country": country,
                    "nickname": nickname,
                }
            )

    with open(jsonfilepath, "w") as json_file:
        # Option 1:
        # convert list content to a json string with dumps.
        json_string = json.dumps(data)
        # use file.write() to write the string into a file
        json_file.write(json_string)

        # Option 2:
        # json.dump(data, json_file)


def read_json(jsonfilepath="myjsonfile.json"):
    with open(jsonfilepath) as jsonfile:
        data = json.load(jsonfile)
        for row in data:
            number, name, country, nickname = row.values()
            print(
                f"{name}, aka {nickname}, plays for {country}. Shirt number {number}."
            )


# csv_to_json()

read_json()
