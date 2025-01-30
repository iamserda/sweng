def mergeAlternately(word1: str, word2: str) -> str:
        """Given two strings, return a string that's made
    of the chars from string1 and string where characters alternate
    between string1 and string2. ex: "abc" and "xyz" => "axbycz". """
    
    
assert mergeAlternately(word1 = "abc", word2 = "pqr") == "apbqcr"
assert mergeAlternately(word1 = "ab", word2 = "pqrs") == "apbqrs"
assert mergeAlternately(word1 = "abcd", word2 = "pq") == "apbqcd"