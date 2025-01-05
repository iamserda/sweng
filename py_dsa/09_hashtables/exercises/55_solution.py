def item_in_common_using_set(list_a, list_b):
    return len(set(list_a).intersection(set(list_b))) > 0

def item_in_common_using_hashtable(list_a, list_b):
    sol_dict = {}
    for key in list_a:
        sol_dict[key] = 1

    for item in list_b:
        if sol_dict.get(item) == 1:
            return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]
assert item_in_common_using_set(list1, list2) == True

list1 = [1,3,5]
list2 = [2,4,6]
assert item_in_common_using_hashtable(list1, list2) == False
