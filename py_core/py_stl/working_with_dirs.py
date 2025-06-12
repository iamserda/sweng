from pathlib import Path

user_home = Path().home()
downloads = user_home / Path("Downloads")

if downloads.exists() and downloads.is_dir():
    downloads_content = [
        {
            "stem": path.stem,
            "suffix": "" if not path.is_file() else path.suffix,
            "abs-path": path.absolute(),
        }
        for path in Path("/Volumes/SSD1TB/courses/").rglob("**/*.*")
    ]
# for Path(some_path).glob, use "**/*.*"
# example Path("/Volumes/SSD1TB/courses/").glob("**/*.*")

# for Path(some_path).rglob("*.mp4"), you can simply pass the file type
print()
print(f"Content:\nTotal Count: {len(downloads_content)}")
for element in downloads_content[-10:]:
    print(element["abs-path"])
