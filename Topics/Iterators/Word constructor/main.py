word1 = input()
word2 = input()
new_word = ''

for letter1, letter2 in zip(word1, word2):
    new_word += letter1
    new_word += letter2

print(new_word)
