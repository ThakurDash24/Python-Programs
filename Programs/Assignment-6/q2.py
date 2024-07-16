x = [1, 2, 3]
y = [1, 2, 3]

result = []
for i in x:
    for j in y:
        if i != j:
            result.append((i, j))

print(result)   

#USING SET
x = [1, 2, 3]
y = [1, 2, 3]

result_set = set()
for i in x:
    for j in y:
        if i != j:
            result_set.add((i, j))

result = (result_set)
print(result)
