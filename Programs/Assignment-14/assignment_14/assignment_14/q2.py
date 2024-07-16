f = open('Assignment-14/assignment_14/assignment_14/sowpods.txt', 'r')
words = f.readlines()
words = [word.strip() for word in words]
appearing_pairs = set()
for word in words:
    for i in range(len(word) - 1):
        pair = word[i:i+2]
        if pair[0] == pair[1]:  # Only consider pairs where both letters are the same
            appearing_pairs.add(pair)

# All possible pairs of consecutive identical letters
all_pairs = set(chr(c) * 2 for c in range(ord('A'), ord('Z') + 1))

# Pairs that never appear
never_appearing_pairs = set()
never_appearing_pairs = all_pairs - appearing_pairs

# Print the pairs that never appear
for pair in sorted(never_appearing_pairs):
    print(pair)

# Close the file
f.close()
