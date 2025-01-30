"""
Challenge:
- Implement HashTable Class
    - Constructor
    - Method to print all key,value pairs of the hash_table

HINT: How Hash Method should work:
    The hash of a given string is:
    - previous hash or 0(no previous letter)
    - added to the ord() of the current letter
    - times some prime number.
    - all that modulo length of the current array container 

    FORMULA:
        hash = ((hash or 0() + ord(current letter) * 23) % len(self.data_map)
    
    hash is always an integer value
    hash should always be an index in self.data_map
    hash should be "DERTIMINISTIC", which means, I should get the same index key, for a given string
    
    example if I enter "iamserda" , in hash, 1000 times, I should ALWAYS get the same index 1000.

"""

class HashTable:
    def __init__(self, size=7):
        """Implement Constructor"""

    def __hash(self, key):
        """Implement Constructor"""

    def print_table(self):
        """I"""


#Testing Arenas:

my_hash_table = HashTable()

assert my_hash_table.data_map [0] == None
assert my_hash_table.data_map[1] == None
assert my_hash_table.data_map[2] == None
assert my_hash_table.data_map[3] == None
assert my_hash_table.data_map[4] == None
assert my_hash_table.data_map[5] == None
assert my_hash_table.data_map[6] == None



"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  None
    5 :  None
    6 :  None

"""