from pathlib import Path
from zipfile import ZipFile

oop_folder = Path("./oops")


with ZipFile("oops.zip", "w") as writable_zip:
    for item in oop_folder.iterdir():
        # create a zipfile
        writable_zip.write(item)
