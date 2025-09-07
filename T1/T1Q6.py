# Shira Choen 212079875
# Shira Erel 213173636

unar_func = [("X*2",lambda x: x*2), ("X**2", lambda x: x**2), ("X**(-1)", lambda x: x**(-1))]

def unar_dict(lst, unar_func):
    return dict(map(lambda f: (f[0], list(map(f[1], lst))), unar_func))

print(unar_dict([1,2,3,4,5], unar_func))