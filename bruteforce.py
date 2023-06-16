import csv


def load_data():
    data_shares = []

    with open('data_shares.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data_shares.append(row)

    # remove first list with header
    data_shares = data_shares[1:]

    return data_shares


def generate_combinations(shares, budget):
    """ final result list combinations_with_max_profit looks like:
    [[share[i], share[i+1], share[i+2], total_price, average_profit]
    """

    combinations = []
    generate_combinations_recursive(shares, budget, [], combinations)

    for combi in combinations:
        profit = 0
        total_price = 0
        for share in combi:
            profit += float(share[2])
            total_price += int(share[1])

        combi.append(total_price)
        average_profit = round(float(profit / len(combi[:-1])), 2)
        combi.append(average_profit)

    combinations_with_max_profit = max(combinations, key=lambda x: x[-1])

    return combinations_with_max_profit


def generate_combinations_recursive(shares, budget, current_combination, combinations):
    if budget < 0:
        return combinations

    if budget == 0:
        combinations.append(list(current_combination))
        return combinations

    if not shares:
        return combinations

    share = shares[0]
    # check if price is smaller/egal to budget
    if int(share[1]) <= budget:
        current_combination.append(share)
        combinations = generate_combinations_recursive(
            shares[1:], budget - int(share[1]), current_combination, combinations
        )
        current_combination.pop()

    combinations = generate_combinations_recursive(shares[1:], budget, current_combination, combinations)
    return combinations


data_shares = load_data()
generate_combinations = generate_combinations(data_shares, budget=500)
print('end result', generate_combinations)
