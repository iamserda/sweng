import os

def manual_get_filename_and_fileextension(folder_path):
    """Given a directory, prints the name and extension of all files within the directory."""
    print("\nMunual Split of:\nFile Names\t\tFile Extensions:")
    for item in os.listdir(folder_path):
        if os.path.isfile(folder_path + item):
            # the file extension
            index = len(item) - 1
            while item[index] != ".":
                index -= 1

            # moving the index ahead of the '.' from the previous loop
            end_index = index
            
            #extracting the file name
            while item[index] != "/":
                index -= 1
                if index >= 0:
                    start_index = index
                else:
                    break
            file_name = item[start_index:end_index]
            file_ext = item[end_index:]
            if len(file_name) > 5:
                print(f" filename: {file_name}\t extention: {file_ext}")
            else:
                print(f" filename: {file_name}\t\t extention: {file_ext}")

# Using standard-lib module OS
def get_filename_and_ext(folderpath:str)->None:
    print("\nUsing OS.PATH.SPLITEXT(PATH_VAR)\nFile Names\t\tFile Extensions:")
    for item in os.listdir(folderpath):
        if os.path.isfile(folderpath+item):
            filename, extension = os.path.splitext(item)
            if len(filename) > 5:
                print(f" filename: {filename}\t extention: {extension}")
            else:
                print(f" filename: {filename}\t\t extention: {extension}")

def get_file_that_ends_with(filepath:str, suffix:str)->None:
    """Given a filepath, and suffix, this function prints all item with that path with the matching suffix. Not-recurisving."""
    print(f"\nFiles ending with {suffix}:")
    for item in os.listdir(filepath):
        if item.endswith(suffix):
            print(item, type(item))

def get_file_that_starts_with(filepath:str, prefix:str)->None:
    """Given a filepath, and prefix, this function prints all item with that path with the matching prefix. Not-recurisving"""
    print("\nFiles:")
    for item in os.listdir(filepath):
        if item.startswith(prefix):
            print(item)

#test
manual_get_filename_and_fileextension("../")
get_filename_and_ext(folderpath="../")
get_file_that_ends_with("../", suffix=".md")
get_file_that_starts_with("../", prefix="py")