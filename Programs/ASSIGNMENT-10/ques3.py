def sum_of_digits(num):
    # Base case: if the number is a single digit
    if num < 10:
        return num
    # Recursive case: add the last digit to the sum of the digits of the rest of the number
    return num % 10 + sum_of_digits(num // 10)

# Example usage:
num = 1234
print(sum_of_digits(num))  # Output: 10

num = 9876
print(sum_of_digits(num))  # Output: 30
