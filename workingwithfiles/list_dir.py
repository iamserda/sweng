import os

def list_directory(folder:str)->None:
    """Given a directory path as a string, this function will list all the items within the directory."""
    if os.path.exists(folder) and os.path.isdir(folder):
        for name in os.listdir(folder):
            if os.path.isdir(folder+f"/{name}"):
                print(f"Folder: {name}")
            else:
                print(f"File: {name}")

list_directory("../")