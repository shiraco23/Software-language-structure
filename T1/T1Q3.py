# Shira Choen 212079875
# Shira Erel 213173636

gimatria = { 'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6,
             'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30,
             'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
                'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400}

def get_gimatria_value(word):
    num_word = list(map(lambda x: gimatria.get(x, 0), word))
    return sum(num_word)