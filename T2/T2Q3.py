# Shira Choen 212079875
# Shira Erel 213173636

from datetime import datetime, timedelta

def generate_dates(start_date_str, num_jumps):
    return str(datetime.strptime(start_date_str, "%Y-%m-%d") + timedelta(days=num_jumps))


def al_dates_with_map(start_date_str, num_dates, num_jumps):
    return list(map(lambda i: generate_dates(start_date_str, i * num_jumps), range(num_dates)))


dates = al_dates_with_map("2023-01-01", 3, 3)
print(dates)