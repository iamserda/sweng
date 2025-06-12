from pathlib import Path
from zipfile import ZipFile

zipfile_reader = ZipFile("oops.zip")
zipfile_reader.extractall("./extracted")
