from pathlib import Path

user_home = Path().home()
print(f"user-home: {user_home}")

current_path = Path()  # the relative path to the current directory

# print relative path:
print("\nrel-path:", current_path)  # .
print(
    "abs-path:", current_path.absolute()
)  # /Users/iamserda/repos/sweng/py_core/py_stl

# Windows Paths
win_path_example = Path("c:\\users\\iamserda\\repos\\python\\py_stl")
print("\nwin-style-path:", win_path_example)

# using Raw strings, \ is no longer an ESCAPE char. It is just used as a string.
win_path_example = Path(r"c:\users\iamserda\repos\python\py_stl")
print("win-style-path:", win_path_example)

# print path, and adding
file_path = Path("working_with_paths.py")
print(f"\nfile_path: {file_path}")
print(f"is_file?: {'Yes' if file_path else 'No'}")  # Yes

# /Users/iamserda/repos/sweng/py_core/py_stl/working_with_paths.py
print(f"file_path(abs): {file_path.absolute()}")

# Check if a given path is a directory
print(
    f"Is this path a directory?: {'Yes' if current_path.is_dir() else 'Nope'}."
)  # Yes

# # check if a path object is a file.
new_file_path = current_path / Path("working_with_paths.py")
# /Users/iamserda/repos/sweng/py_core/py_stl/working_with_paths.py
print(new_file_path.absolute)
print("\nIs this a path to a")
print(f"dir-path?: {'Yes' if new_file_path.is_dir() else 'Nope'}.")
print(f"file-path: {'Yes' if new_file_path.is_file() else 'Nope'}.")

# usefule methods for a path
dir_path = Path()
print("\ndirectory:", dir_path.absolute())

# combine
file_path = dir_path / Path("MyApp.txt")
print("\nabs-file_path", new_file_path.absolute())
print(f"file-path: {'Yes' if new_file_path.is_file() else 'Nope'}.")

# combining path object dir_path, with a string "MyApp.txt"
file_path = dir_path / "MyApp.txt"
print("\nabs-file_path", new_file_path.absolute())
print(f"file-path: {'Yes' if new_file_path.is_file() else 'Nope'}.")
# It does not mean the file EXIST.
# It ONLY means this would be considered a file, because of the suffix

# get specific portions:
print("\nGet specific portions:\n")
# name(filename/stem + fileextension/suffix)
print(f"filename + ext: {file_path.name}")
# just name aka stem
print(f"name(stem): {file_path.stem}")
# just extension aka suffix
print(f"ext(suffix): {file_path.suffix}")

# parent
print()
print(f"file_path: {file_path.absolute()}")
print(f"show-parent-folder: {file_path.parent.absolute()}")

# create a new path by changing file name, same extension
print()
print(f"file1: {file_path.absolute()}")
print(f"file2: {file_path.with_stem("my_new_file").absolute()}")

# create a new file path by changing extension
print()
print(f"file1: {file_path.absolute()}")
print(f"file2: {file_path.with_suffix(".txt").absolute()}")

# create a new file path, changing both names and extension
print()
print(f"file1: {file_path.absolute()}")
print(f"file2: {file_path.with_name("new_file_.txt").absolute()}")
