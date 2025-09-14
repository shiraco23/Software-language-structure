# Shira Choen 212079875
# Shira Erel 213173636

# Regular recursion
def sum_array_regular(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array_regular(arr[1:])

# Tail recursion
def sum_array_tail_recursive(arr, accumulator=0):
    if len(arr) == 0:
        return accumulator
    return sum_array_tail_recursive(arr[1:], accumulator + arr[0])

def create_tuple_tail_recursive(n, accumulator=()):
    if n == 0:
        return accumulator
    return create_tuple_tail_recursive(n - 1, (n,) + accumulator)


numbers_tuple = create_tuple_tail_recursive(1000)

result_regular = sum_array_regular(numbers_tuple)
result_tail = sum_array_tail_recursive(numbers_tuple)

print(f"Regular: {result_regular}")
print(f"Tail: {result_tail}")