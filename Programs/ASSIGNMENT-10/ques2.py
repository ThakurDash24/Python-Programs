def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0.0
    for value, weight in items:
        if capacity >= weight:
            # Take the whole item
            capacity -= weight
            total_value += value
        else:
            # Take the fraction of the item
            total_value += value * (capacity / weight)
            break
    return total_value

# Example usage:
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
print(fractional_knapsack(items, capacity))  # Output: 240.0
