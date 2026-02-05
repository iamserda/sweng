from pathlib import Path

def using_pathglob(dir_path:str, pattern_:str)->None:
    path_obj = Path(dir_path)
    for filename in path_obj.glob(pattern=pattern_):
        print(filename.)

using_pathglob(dir_path="/volumes/ssd1tb/bookstore/", pattern_="*.pdf")
