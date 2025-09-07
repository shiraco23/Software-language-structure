# Shira Choen 212079875
# Shira Erel 213173636
#שאלות 4א, 4ג
# שאלה 4ב בבודק האוטומטי
def prime(n):
    if n <= 1:
        return False
    return list(filter(lambda x: n % x == 0, range(2, int(n**0.5) + 1))) == []

def twin_primes(n):
    if prime(n):
        if prime(n+2):
            return n+2
        elif prime(n-2):
            return n-2
    
    return "invalid input"

def n_twin_primes(n):
    twints = dict(map(lambda x: (x, twin_primes(x)), 
                      filter(lambda x: twin_primes(x) != "invalid input", range(2, int(n)+1))))
    return twints

print("enter prime number:")
u = input().strip()
print(n_twin_primes(u))