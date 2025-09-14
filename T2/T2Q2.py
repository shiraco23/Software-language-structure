# Shira Choen 212079875
# Shira Erel 213173636

from functools import reduce

func1 = lambda x: x/2 +2
list_1000 = range(1, 1001)
def even_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False

def al_even_odd_lists(lst):
    return (
        list(filter(even_odd, lst)),
        list(filter(lambda x: not even_odd(x), lst))
    )

evens , odds = al_even_odd_lists(list_1000)

f1= lambda acc, x: acc * x
f2= lambda acc, x: func1(acc) + x

even_result = reduce(f1,evens)
odd_result =  reduce(f2, odds)

print("even_result:", even_result)
print("odd_result:", odd_result)

sum_even = reduce(lambda acc, x: acc + x, evens)
sum_odd = reduce(lambda acc, x: acc + x, odds)

print("sum_even:", sum_even)
print("sum_odd:", sum_odd)
