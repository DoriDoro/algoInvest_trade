from time import time

from bruteforce_utils import load_data

start_time = time()


share_data = load_data('data_shares')

share_data = [(a, int(b), float(c)) for a, b, c in share_data]

data_sorted = sorted(share_data, key=lambda x: x[2], reverse=True)

cost = 500
shares_list = []

for a, b, c in data_sorted:
    if cost - b >= 0:
        cost -= b
        shares_list.append(a)

print(shares_list)
