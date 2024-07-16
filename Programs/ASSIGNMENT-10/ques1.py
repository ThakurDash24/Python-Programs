def is_palindrome(word):
    # Base case: an empty string or single character string is a palindrome
    if len(word) <= 1:
        return True
    # Check the first and last characters
    if word[0] != word[-1]:
        return False
    # Recurse on the substring excluding the first and last characters
    return is_palindrome(word[1:-1])

# Example usage:
word = "radar"
print(is_palindrome(word))  # Output: True

word = "hello"
print(is_palindrome(word))  # Output: False
