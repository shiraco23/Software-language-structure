# Shira Choen 212079875
# Shira Erel 213173636

def dict_3_add(d1, d2, d3):

    keys = set(d1) | set(d2) | set(d3)
    
    return dict(map(lambda k: (k, tuple(set(
        [d1.get(k), d2.get(k), d3.get(k)]
    ) - {None})), keys))


print(dict_3_add({1: 2, 2: 3}, {2: 4, 3: 5}, {1: 2, 3: 6}))