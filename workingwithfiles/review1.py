import os
import fnmatch
from pathlib import Path

dir_path = "/users/iamserda/repos/sweng/"

# listing directory content
for content in os.listdir(dir_path):
    print(content)

# checking prefix and suffix
suffix = "e"
prefix = "py"
for content in os.listdir(dir_path):
    if content.endswith(suffix) and content.startswith(prefix):
        print(f"both: {content}")
    elif content.endswith(suffix):
        print("suffix-matched: ", content)
    elif content.startswith(prefix):
        print("prefix-matched: ", content)

# using pattern matching
for content in os.listdir(dir_path):
    if fnmatch.fnmatch(content, f"{prefix}*{suffix}"):
        print(f"both: {content}")
    elif fnmatch.fnmatch(content, f"*{suffix}"):
        print("suffix-matched: ", content)
    elif fnmatch.fnmatch(content, f"{suffix}*"):
        print("prefix-matched: ", content)

# using glob, prints actual workign links, not just strings because we used Pathlib object.
dir_path: Path = Path(dir_path)
for content in dir_path.glob(f"{prefix}*{suffix}"):
    print(f"both-matched: {content}")

for content in dir_path.glob(f"{prefix}*"):
    print(f"prefix-matched: {content}")

for content in dir_path.glob(f"*{suffix}"):
    print(f"suffix-matched: {content}")
