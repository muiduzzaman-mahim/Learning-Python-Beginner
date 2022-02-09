sentence = 'I love Bangladesh'
sentence = sentence.lower()

Letters = 'abcdefghijklmnopqrstuvwxyz'

print(sentence)

for letter in Letters:
    C = sentence.count(letter)
    if C == 0:
        None
    else:
        print('{} exists {} times.' .format(letter, C))
