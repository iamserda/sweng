import csv


def write_csv():
    with open("./mycsvfile.csv", "w+") as file:
        writer = csv.writer(file)
        writer.writerow(["No.", "Name", "Country", "Nickname"])
        writer.writerow([9, "Ronaldo L. Nazario", "Brazil", "R9"])
        writer.writerow([11, "Romario Farias", "Brazil", "R11"])
        writer.writerow([10, "Ronaldinho Gaucho", "Brazil", "R10"])
        writer.writerow([3, "Roberto Carlos", "Brazil", "R3"])
        writer.writerow([2, "Cafú", "Brazil", "2"])


def read_csv():
    with open("./mycsvfile.csv", "r") as file:
        reader = csv.reader(file)
        arr = [
            {"No.": row[0], "Name": row[1], "Country": row[2], "Nickname": row[3]}
            for row in reader
        ]
        for row in arr[1:]:
            number, name, country, nickname = row.values()
            print(
                f"Player {name}, aka. {nickname}, wore No. {number} for their national team {country}.\n"
            )


# write_csv()
read_csv()
