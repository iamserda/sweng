class TagCloud:
    def __init__(self):
        self.tags = {}

    def __getitem__(self, key):
        return self.tags.get(key, 0)

    def __setitem__(self, key, val):
        self.tags[key] = val

    def __len__(self):
        return self.tags.__len__()

    def __iter__(self):
        return iter(self.tags)


__tagcloud1 = TagCloud()

print("Before: ", __tagcloud1["python"])
__tagcloud1["python"] = 1
__tagcloud1["javascript"] = 10
__tagcloud1["java"] = 20
__tagcloud1["go"] = 30
print("After: ", __tagcloud1["python"])
print("Length:", len(__tagcloud1))
for k in __tagcloud1:
    print(k)
