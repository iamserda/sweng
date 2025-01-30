class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def get_size(self):
        return len(self.data_map)

    def __hash(self, key)->int:
        my_hash = 0
        for char in key:
            # same as: my_ash = (my_ash + order(char) * 23) % len(self.data_map)
            my_hash += ord(char) * 23
            my_hash %= len(self.data_map)
        return my_hash

    def set_item(self, key:str, value:str)->list:
        """add or update values within a hashtable"""
        index = self.__hash(key)
        if self.data_map[index] is not None:
            if "list" in str(type(self.data_map[index])):
                self.data_map[index].append({key:value})
            else:
                new_list = [self.data_map[index]]
                new_list.append({key: value})
                self.data_map[index] = new_list
        else:
            self.data_map[index] = {key: value}

    def get_item(self, key:str) -> str:
        """get method"""
        index = self.__hash(key)
        if "list" in str(type(self.data_map[index])):
            for elem in self.data_map[index]:
                if key in elem:
                    return elem[key]
        return self.data_map[index][key] if key in self.data_map[index] else None

    def get_keys(self):
        keys_arr = []
        for elem in self.data_map:
            if elem == None:
                continue
            elif "list" in str(type(elem)):
                for el in elem:
                    keys_arr.append(list(el.keys())[0])
            else:
                keys_arr.append(list(elem.keys())[0])
        return set(keys_arr)

    def print_data_map(self):
        """print data_map"""
        for i,v in enumerate(self.data_map):
            print(f"{i}: {v}")

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

# assert my_hash_table.get_item("z") == None
a = my_hash_table.get_keys()
b = set("abcdefghijkl")
assert len(a.symmetric_difference(b)) == 0
