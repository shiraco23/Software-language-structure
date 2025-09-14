# Shira Choen 212079875
# Shira Erel 213173636

from functools import reduce
import time
import operator

func1 = lambda x: x/2 +2

def al_func(func):
    return list(map(func, range(10000+1)))

def al_reduce(al_func, func):
    return reduce(operator.add, al_func(func))

def imper_sum(al_func, func):
    sum = 0
    for i in al_func(func):
        sum += i
    return sum


start_time = time.time()
result1 = al_reduce(al_func, func1)
time_al = time.time() - start_time

start_time = time.time()
result2 = imper_sum(al_func, func1)
time_imper = time.time() - start_time

print("Time taken by al_reduce: {:.6f} seconds".format(time_al))
print("Time taken by imper_sum: {:.6f} seconds".format(time_imper))

al_sum = sum(map(func1, range(10000+1)))
