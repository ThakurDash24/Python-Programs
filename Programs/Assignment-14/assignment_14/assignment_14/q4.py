# Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

# Open the file and read its content
with open('Assignment-14/assignment_14/assignment_14/sowpods.txt', 'r') as f:
    words = f.readlines()
words = [word.strip() for word in words]
palindrome_words = []
# Check each word for being a palindrome
for word in words:
    if is_palindrome(word):
        palindrome_words.append(word)

# Print each palindrome word
for word in palindrome_words:
    print(word)
