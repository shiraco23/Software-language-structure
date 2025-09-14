# Shira Choen 212079875
# Shira Erel 213173636

def power_function(x):
    return lambda n: n**x

def all_powers(num_powers):
    return map(lambda n: (n, power_function(n)), range(0, num_powers))

def calculate_powers(base, powers):
    return tuple(map(lambda x: (x[0], x[1](base)), powers))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def taylor_expansion(base):
    return sum(map(lambda k: k[1] / factorial(k[0]), calculate_powers(base, all_powers(900))))

print(taylor_expansion(5))


n = int(input("Enter number of powers:"))
result = all_powers(n)
print(type(result))
base = int(input("Enter base:"))
print(calculate_powers(base, result))
