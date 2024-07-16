def word_length_dict(sentence):
    return {word: len(word) for word in sentence.split()}

sentence = "Write a function that takes a sentence as input"
print(word_length_dict(sentence))

