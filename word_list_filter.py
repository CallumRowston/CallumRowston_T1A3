word_word = []

with open('word_list.txt', 'r') as f:
    for word in f.readlines():
        word_word.append(word.strip())

with open('word_list_6.txt', 'w') as g:
    for word in word_word:
        g.write(word.upper() + "\n")
