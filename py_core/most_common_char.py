def find_maxi(sentence):
    dictio = {}
    maxi = None
    for char in sentence:
        if char == " ":
            continue
        if char not in dictio:
            dictio[char] = 1
        else:
            dictio[char] += 1

        if maxi is None:
            maxi = char
        else:
            maxi = char if dictio[char] > dictio[maxi] else maxi
    return dictio, maxi


sentence = "This is a common interview question"
dictio, maxi = find_maxi(sentence)
print(f"The most common character is: {maxi}.\nOccurrence: {dictio[maxi]} times")
