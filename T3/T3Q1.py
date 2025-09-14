# Shira Choen 212079875
# Shira Erel 213173636

# Regular Recursion
def create_tuple_regular(n):
    if n == 0:
        return ()
    
    return create_tuple_regular(n - 1) + (n,)


# Tail Recursion
def create_tuple_tail_recursive(n, accumulator=()):
    if n == 0:
        return accumulator
    
    return create_tuple_tail_recursive(n - 1, (n,) + accumulator)

regular_small = create_tuple_regular(1000)
tail_small = create_tuple_tail_recursive(1000)

print(f"Regular: {regular_small}")
print(f"Tail: {tail_small}")
