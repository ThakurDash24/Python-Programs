def word_frequency(sentence):
    sentence = sentence.lower()
    punctuation = ',.!?;:'
    for char in punctuation:
        sentence = sentence.replace(char, '')
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = input('Enter the sentence :')
frequency = word_frequency(sentence)
print(frequency)
