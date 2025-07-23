import os
import fnmatch
from pathlib import Path

dir_path = "/volumes/ssd1tb/bookstore/epub/"

# listing directory content
print(f"\nListing directory content of {dir_path}: ")
for index, content in enumerate(os.listdir(dir_path)):
    print(index + 1, ":", content if len(content) < 80 else f"{content[:40]} ... {content[-20:]}")
# checking prefix and suffix
suffix = "e"
prefix = "py"
print("\nUsing str methods startswidth/endswith")
for content in os.listdir(dir_path):
    if content.endswith(suffix) and content.startswith(prefix):
        print(f"both: {content}")
    elif content.endswith(suffix):
        print("suffix-matched: ", content)
    elif content.startswith(prefix):
        print("prefix-matched: ", content)

# using pattern matching
print("\nFiltering using 'fnmatch':")
for content in os.listdir(dir_path):
    if fnmatch.fnmatch(content, f"{prefix}*{suffix}"):
        print(f"both: {content}")
    elif fnmatch.fnmatch(content, f"*{suffix}"):
        print("suffix-matched: ", content)
    elif fnmatch.fnmatch(content, f"{suffix}*"):
        print("prefix-matched: ", content)

# using glob, prints actual workign links, not just strings because we used Pathlib object.
dir_path: Path = Path(dir_path)
print("\nFiltering using 'Blog':")
for content in dir_path.glob(f"{prefix}*{suffix}"):
    print(f"both-matched: {content}")

for content in dir_path.glob(f"{prefix}*"):
    print(f"prefix-matched: {content}")

for content in dir_path.glob(f"*{suffix}"):
    print(f"suffix-matched: {content}")


dir_path: Path = Path(dir_path)
search_term = "python"
print(f"\nFile and Folders: Seaching for {search_term}")
for content in dir_path.glob(f"*{search_term}*"):
    print(f"{content}")
