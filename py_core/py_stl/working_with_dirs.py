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

print()
print(f"Content:\nTotal Count: {len(downloads_content)}")
for element in downloads_content[-10:]:
    print(element["abs-path"])
