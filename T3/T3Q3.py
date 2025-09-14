# Shira Choen 212079875
# Shira Erel 213173636

# Regular recursion
def gcd_recursive(a, b):
    return a if b == 0 else gcd_recursive(b, a % b)

def lcm_recursive(a, b):
    return abs(a * b) // gcd_recursive(a, b)

# Tail recursion
def gcd_tail(a, b):
    def helper(x, y):
        if y == 0:
            return x
        return helper(y, x % y)
    return helper(a, b)

def lcm_tail(a, b):
    return abs(a * b) // gcd_tail(a, b)

print(f"LCM Regular: {lcm_recursive(48, 18)}")
print(f"LCM Tail: {lcm_tail(48, 18)}")