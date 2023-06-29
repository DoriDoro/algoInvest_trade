import csv

from itertools import combinations


def load_data():
    data_shares = []

    with open('data_shares.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data_shares.append(row)

    # remove first list with header
    data_shares = data_shares[1:]

    return data_shares


def generate_combinations(data_of_shares):
    all_possible_combinations = []

    for i in range(1, len(data_of_shares) + 1):
        combies = combinations(data_of_shares, i)
        all_possible_combinations.extend(combies)
        print('here', all_possible_combinations)


def bruteforce(data_of_shares, budget):
    selected_shares = []
    best_profit = 0

    for i in range(0, len(data_of_shares)+1):
        print('i', i)
        for data_list in data_of_shares:
            print('data_list', data_list)
            price = int(data_list[1])
            if budget - price <= 0:
                break
            budget -= price
            profit = float(data_list[2])
            selected_shares.append(profit)

        average_rate = round((sum(selected_shares) / len(selected_shares) if selected_shares else 0), 2)

    print('length: ', len(selected_shares), 'budget: ', budget, 'average: ', average_rate)


# shares = load_data()
# generate_combinations(shares)

# bruteforce(shares, budget=500)
