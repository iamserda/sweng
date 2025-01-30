class HashTable:
    def __init__(self, size=2):
        self.data_map = [None]*size

    def __hash(self, key):
        my_hash = 0
        for k in key:
            my_hash = (my_hash + ord(k) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        for i, v in enumerate(self.data_map):
            if i == index:
                if v is None:
                    self.data_map[index] = [[key, value]]
                else:
                    self.data_map[index].append([key, value])
                return True

    def get_item(self, key):
        index = self.__hash(key)
        for i in range(len(self.data_map)):
            if index == i:
                # [col,...,col] rows includes Zero(0) or more columns
                row = self.data_map[index]
                if len(row) == 1:
                    value = row[0][1]
                    return value
                elif len(row) > 1:
                    for col in row:
                        _key, _val = col
                        if _key == key:
                            return _val

    def get_keys(self):
        keys_arr = []
        for row in self.data_map:
            if len(row) > 1:
                for col in row:
                    keys_arr.append(col[0])
            elif len(row) == 1:
                col = row[0]
                keys_arr.append(col[0])
        return set(keys_arr)

    def get_size(self):
        return len(self.data_map)


# Testing Arenas:
my_hash_table = HashTable(7)
assert my_hash_table.get_size() == 7
my_hash_table.set_item("a", 10)
assert my_hash_table.get_item("a") == 10
my_hash_table.set_item("b", 20)
assert my_hash_table.get_item("b") == 20
my_hash_table.set_item("c", 30)
assert my_hash_table.get_item("c") == 30
my_hash_table.set_item("d", 40)
assert my_hash_table.get_item("d") == 40
my_hash_table.set_item("e", 50)
assert my_hash_table.get_item("e") == 50
my_hash_table.set_item("f", 60)
assert my_hash_table.get_item("f") == 60
my_hash_table.set_item("g", 180)
assert my_hash_table.get_item("g") == 180
my_hash_table.set_item("h", 120)
assert my_hash_table.get_item("h") == 120
my_hash_table.set_item("i", 130)
assert my_hash_table.get_item("i") == 130
my_hash_table.set_item("j", 80)
assert my_hash_table.get_item("j") == 80
my_hash_table.set_item("k", 20)
assert my_hash_table.get_item("k") == 20
my_hash_table.set_item("l", 80)
assert my_hash_table.get_item("l") == 80

assert my_hash_table.get_item("z") == None

a = my_hash_table.get_keys()
b = set("abcdefghijkl")
assert len(a.symmetric_difference(b)) == 0
