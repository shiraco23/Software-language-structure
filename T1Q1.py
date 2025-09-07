# Shira Choen 212079875
# Shira Erel 213173636

def get_penta_number(n):
    if n == 0:
        return 0
    else:
        return n * (3 * n - 1) // 2
    

def pentaNumRange(n1, n2):
    return list(map(get_penta_number, range(n1, n2)))