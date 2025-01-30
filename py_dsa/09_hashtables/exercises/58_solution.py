def group_anagrams(arr):
    answer = []
    if arr is not None:
        grouped_anagrams = {}
        for elem in arr:
            elem_list = list(elem)
            print(elem, elem_list)
            sorted_elem = sorted(elem_list)
            key_elem = "".join(sorted_elem)
            if key_elem not in grouped_anagrams:
                grouped_anagrams[key_elem] = []
            grouped_anagrams[key_elem].append(elem)
        
        for values in grouped_anagrams.values():
            answer.append(values)
        return answer
    return answer



print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""