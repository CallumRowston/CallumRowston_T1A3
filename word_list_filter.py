five_letter_words = []

with open('word_list.txt', 'r') as f:
    for line in f.readlines():
        word = line.upper()
        five_letter_words.append(word)

with open('word_list_5.txt', 'w') as g:
    for word in five_letter_words:
        g.write(word)