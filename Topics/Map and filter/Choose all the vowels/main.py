def choose_vowels(letters):
    vowels = ['a', 'e', 'i', 'u', 'o']
    filtered = filter(lambda x: x in vowels, letters)
    return list(filtered)
