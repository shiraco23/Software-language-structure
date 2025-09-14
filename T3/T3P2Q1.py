# Shira Choen 212079875
# Shira Erel 213173636

import sys
import time
from itertools import islice

# Eager Evaluation
def eager_numbers():
    start = time.time()
    numbers = list(range(0, 10001))
    end = time.time()
    
    #print("Eager Evaluation:")
    #print("Time:", end - start, "seconds")
    #print("Memory size:", sys.getsizeof(numbers), "bytes")
    return numbers


# Lazy Evaluation, use generator expression
def lazy_numbers():
    start = time.time()
    numbers = (n for n in range(0, 10001))   
    end = time.time()
    
    #print("Lazy Evaluation:")
    #print("Time:", end - start, "seconds")
    #print("Memory size:", sys.getsizeof(numbers), "bytes")
    return numbers


# Eager Evaluation
def eager_first_5000():
    start = time.time()
    numbers = eager_numbers()
    first_5000 = numbers[:5000]
    end = time.time()

    print("\nEager Evaluation - first 5000:")
    print("Time:", end - start, "seconds")
    print("Memory size:", sys.getsizeof(first_5000), "bytes")
    print("Type:", type(first_5000))
    return first_5000


# Lazy Evaluation
def lazy_first_5000():
    start = time.time()
    numbers = lazy_numbers()
    first_5000 = list(islice(numbers, 5000))
    end = time.time()

    print("\nLazy Evaluation - first 5000:")
    print("Time:", end - start, "seconds")
    print("Memory size:", sys.getsizeof(first_5000), "bytes")
    print("Type:", type(first_5000))
    return first_5000


if __name__ == "__main__":
    #1.1
    eager_numbers()
    lazy_numbers()

    #1.2
    eager_first_5000()
    lazy_first_5000()
