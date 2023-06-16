import csv

# data_shares = []
#
# with open('data_shares.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         data_shares.append(row)
#
# # remove first list with header
# data_shares = data_shares[1:]
# # print('data', data_shares)

data_shares = [
    ["Action-1", 20, 0.25],
    ["Action-2", 30, 3],
    ["Action-3", 50, 7.5],
    ["Action-4", 70, 14],
    ["Action-5", 60, 10.2]
]


def generate_combinations(shares, budget):
    combinations = []
    generate_combinations_recursive(shares, budget, [], combinations)

    for combi in combinations:
        profit = 0
        for share in combi:
            profit += float(share[2])
        average_profit = float(profit / len(combi))
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


generate_combinations = generate_combinations(data_shares, budget=100)
print('end result', generate_combinations)
