
def mergeAlternately(word1: str, word2: str) -> str:
    """Given two strings, return a string that's made
    of the chars from string1 and string where characters alternate
    between string1 and string2. ex: "abc" and "xyz" => "axbycz". """
    count = len(word1) if len(word1) >= len(word2) else len(word2)
    word3 = ""
    for i in range(count):
        if i < len(word2) and i < len(word1):
            word3 += word1[i]
            word3 += word2[i]
            continue
        if i >= len(word1):
            word3 += word2[i]
            continue
        else:
            word3 += word1[i]
    return word3

assert mergeAlternately(word1 = "abc", word2 = "pqr") == "apbqcr"
assert mergeAlternately(word1 = "ab", word2 = "pqrs") == "apbqrs"
assert mergeAlternately(word1 = "abcd", word2 = "pq") == "apbqcd"