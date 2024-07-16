""" def solution(total_heads, total_legs):
    for chickens in range(total_heads + 1):
        rabbits = total_heads - chickens
        if 2 * chickens + 4 * rabbits == total_legs:
            return chickens, rabbits
    return None, None  # No solution found

# Given data
total_heads = 35
total_legs = 94

chickens, rabbits = solution(total_heads, total_legs)

if chickens is not None and rabbits is not None:
    print(f"Number of chickens: {chickens}")
    print(f"Number of rabbits: {rabbits}")
else:
    print("No solution found") """



""" x = [1, 2, 3]
y = [1, 2, 3]

result = []
for i in x:
    for j in y:
        if i != j:
            result.append((i, j))

print(result) """

x = [1,2,3]
y = [1,2,3]
result=set()
for i in x:
    for j in y:
        result.add((i,j))
print(x)