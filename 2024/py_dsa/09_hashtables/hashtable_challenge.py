class HashTable:
    def __init__(self, size=7):
            """constructor"""

    def get_size(self):
        """size of hashtable"""

    def __hash(self, key)->int:
        """hash function"""

    def set_item(self, key:str, value:str)->list:
        """set or update a value"""

    def get_item(self, key:str) -> str:
        """get method"""

    def print_data_map(self):
        """print data_map"""

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
