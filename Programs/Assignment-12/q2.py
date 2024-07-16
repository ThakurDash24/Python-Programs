import random
import string
def random_alpha():
    return random.choices(string.ascii_letters)

def alpha_string(l):
    return ''.join(random.choices(string.ascii_letters, k=l))
    
def random_fixed_alpha_str():
    fixed_len=10
    return ''.join(random.choices(string.ascii_letters, k=fixed_len)) 
#random_string1=alpha_string(1)

print('Random alphabetical letter :',random_alpha())
print('Random alphabetical string with length of 5:',
      alpha_string(5))
print('Random alphabetical string of fixed length 10:',
      random_fixed_alpha_str())
