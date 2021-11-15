def natural_numbers():
    """Returnn 1, 2, 3"""
    n = 1
    
    while True:
        yield n
        n += 1
        

# for i in natural_numbers(1):
    # print("{0}".format(i))
    
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from iterator_generator import *


evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)
print(evens_below_20)

data = natural_numbers()
evens = (x for x in data if x % 2 == 0)

get_list = list(evens)
print(get_list)
