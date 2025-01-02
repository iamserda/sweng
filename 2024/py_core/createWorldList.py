import string


def createWordListFromString(phrase: str) -> list:
    "Given a string, find all the words in the phrase"
    if not phrase:
        return []
    words = []
    word = ""
    alphabet = set(list(string.ascii_lowercase))
    for char in phrase.strip():
        word += char
        if char.lower() not in alphabet:
            word = word[:-1]
            if word:
                words.append(word)
                word = ""
            continue
    # insert the last word found
    if word:
        words.append(word)
        word = ""

    return words


if __name__ == "__main__":
    phrase = "Python is an amazing programming language. You should try it!"
    words = createWordListFromString(phrase)
    words_set = ['python', 'is', 'an', 'amazing', 'programming', 'language', 'you', 'should', 'try', 'it']
    for word in words:
        assert word.lower() in words_set
