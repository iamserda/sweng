def remove_duplicates(list_a:list)->list:
    return list(set(list_a))



my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)

assert new_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]
