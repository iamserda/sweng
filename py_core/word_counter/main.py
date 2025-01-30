def text_analytics(file_path)->tuple:
    char_count1 = 0
    char_count2 = 0 # with spaces
    word_count = 0
    line_count = 0
    with open(file_path) as file:
        lines = file.readlines()
        line_count = len(lines)
        for line in lines:
            words = line.split()
            word_count += len(words)
            char_count2 += len(line)
            for word in words:
                char_count1 += len(word)
    return line_count, word_count, char_count1, char_count2

for file_path in ["./book/chapter1.txt", "./book/chapter2.txt"]:
    lc, wc, cc1, cc2 = text_analytics(file_path)
    print(f"\nWord Count: {wc}\nChar Count w/o spaces: {cc1}\nChar Count w/ spaces: {cc2}\nLine Count: {lc}""")
