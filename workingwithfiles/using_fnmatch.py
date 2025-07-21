import os
import fnmatch

def file_with_patterns(dir_path, pattern):
    for index, item in enumerate(os.listdir(dir_path)):
        if fnmatch.fnmatch(item, pat=pattern):
            print(f"file no. {index + 1}: {item}")

file_with_patterns("/volumes/ssd1tb/bookstore", "*python*.pdf")