def min_max_avg(*args):
    if not args:
        return None, None, None
    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)
    return minimum, maximum, average

numbers = [1, 2, 3, 4, 5]
print(min_max_avg(*numbers)) 
