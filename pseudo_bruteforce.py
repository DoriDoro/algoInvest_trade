import csv

from itertools import permutations


def load_pseudo_data():
    pseudo_data_shares = []

    with open('pseudo_data_shares.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            pseudo_data_shares.append(row)

    # remove first list with header
    pseudo_data_shares = pseudo_data_shares[1:]

    return pseudo_data_shares


def generate_all_combinations(data_of_shares):
    """ generates all possible combinations with `itertools combinations` """
    all_possible_combinations = []

    for combo in permutations(data_of_shares, len(data_of_shares)):
        all_possible_combinations.append(combo)

    return all_possible_combinations


def combinations_budget(possible_combo):
    """ uses all possible combinations to check them and include the budget, budget = 150 """
    budget_combinations = []

    for combination in possible_combo:
        current_combinations = []
        budget = 150

        for combo in combination:
            if budget - int(combo[1]) >= 0:
                budget -= int(combo[1])
                current_combinations.append(combo)

        budget_combinations.append(current_combinations)

    return budget_combinations


def check_profit(budget_combo):
    """ amount = (profit * price of the share) + (prifit * price of share) / length
    create profit_combinations like:
    [['Action-4', '70', '14'], ['Action-3', '50', '7.5'], ['Action-2', '30', '3'], average_profit]
    """
    profit_combinations = []

    for combination in budget_combo:
        result_profit = 0

        for i in range(0, len(combination)):
            price = float(combination[i][1])
            profit = float(combination[i][2])
            result_profit += price * profit
        average_profit = round(result_profit / len(combination), 2)
        combination.append(str(average_profit))
        profit_combinations.append(combination)

    return profit_combinations


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


pseudo_shares = load_pseudo_data()
generate_combinations = generate_all_combinations(pseudo_shares)
combinations_budget = combinations_budget(generate_combinations)
check_profit = check_profit(combinations_budget)

# bruteforce(shares, budget=500)
