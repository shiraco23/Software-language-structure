# Shira Choen 212079875
# Shira Erel 213173636

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def taylor_exp_generator(x):
    n = 0
    current_sum = 0.0
    while True:
        term = (x ** n) / factorial(n)
        current_sum += term
        yield current_sum
        n += 1


if __name__ == "__main__":
    x = 2
    gen = taylor_exp_generator(x)
    
    for _ in range(15):
        print(next(gen))
