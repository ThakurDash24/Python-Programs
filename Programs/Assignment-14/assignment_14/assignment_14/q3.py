with open('Assignment-14/assignment_14/assignment_14/sowpods.txt', 'r') as f:
    words = f.readlines()

words = [word.strip() for word in words]

vowels = set('AEIOU')

words_with_all_vowels = []

for word in words:
    if vowels.issubset(set(word)):
        words_with_all_vowels.append(word)


for word in words_with_all_vowels:
    print(word)
