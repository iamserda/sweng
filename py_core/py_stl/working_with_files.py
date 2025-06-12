from pathlib import Path
from time import ctime

path_manager = Path("/Volumes/SSD1TB/bookstore")
files = [
    {
        "stem": elem.stem,
        "suffix": elem.suffix,
        "abs-path": elem.absolute(),
        "created_on(s)": elem.stat().st_ctime,
        "created_date": ctime(elem.stat().st_ctime),
        "size": f"{round(elem.stat().st_size/1024, 2)} KB",
    }
    for elem in path_manager.rglob("*.pdf")
]


# for file in files:
#     print(file["stem"])
for index, file in enumerate(files):
    print(f"{index + 1}.\tname:{file["stem"]}\t\tsize:{file["size"]}\t\t")
