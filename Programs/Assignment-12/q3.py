import random
def population(size):
    random_list=[random.randint(1,9) for _ in range (size)]
    return random_list
def sample(random_list,k):
    selected_items=random.sample(random_list,k)
    return selected_items
size=20
k=5
print('Generated list :' ,population(size))
print('Selected Sample',sample(population(size),k))