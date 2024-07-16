# Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

# Open the file and read its content
with open('Assignment-14/assignment_14/assignment_14/sowpods.txt', 'r') as f:
    words = f.readlines()

words = [word.strip() for word in words]

longest_palindrome = ""

# Check each word for being a palindrome and track the longest one
for word in words:
    if is_palindrome(word) and len(word) > len(longest_palindrome):
        longest_palindrome = word
        
print("The longest palindrome is:", longest_palindrome)
