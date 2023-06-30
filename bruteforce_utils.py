import csv

from itertools import combinations
from itertools import permutations
from time import time

start_time = time()


def load_data():
    """ load the shares data from a csv file with 20 shares """

    data_shares = []

    with open('data_shares.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data_shares.append(row)

    # remove first list with header
    data_shares = data_shares[1:]
    length_data = len(data_shares)
    data_shares.append(length_data)

    return data_shares


def load_pseudo_data():
    """ load the shares data from a csv file with 4 shares """

    pseudo_data_shares = []

    with open('pseudo_data_shares.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            pseudo_data_shares.append(row)

    # remove first list with header
    pseudo_data_shares = pseudo_data_shares[1:]
    length_data = len(pseudo_data_shares)
    pseudo_data_shares.append(length_data)

    return pseudo_data_shares


def generate_all_combinations_combinations(data_of_shares):
    """ generates all possible combinations with `itertools.combinations` """

    data_of_shares = data_of_shares[0:-1]
    all_possible_combinations_combinations = []

    for i in range(len(data_of_shares) + 1):
        combos = combinations(data_of_shares, i)

        for combo in combos:
            all_possible_combinations_combinations.append(combo)

    return all_possible_combinations_combinations


def generate_all_combinations_permutations(data_of_shares):
    """ generates all possible combinations with `itertools.permutations` """

    data_of_shares = data_of_shares[0:-1]
    all_possible_combinations_permutations = []

    for combo in permutations(data_of_shares, len(data_of_shares)):
        all_possible_combinations_permutations.append(combo)

    return all_possible_combinations_permutations


def combinations_budget(possible_combo, budget):
    """ uses all possible combinations to check them and include the budget, budget = 500 """

    budget_combinations = []

    for combination in possible_combo:
        current_combinations = []
        remaining_budget = budget

        for combo in combination:
            if remaining_budget - int(combo[1]) >= 0:
                remaining_budget -= int(combo[1])
                current_combinations.append(combo)

        budget_combinations.append(current_combinations)

    return budget_combinations


def calculate_profit(budget_combo):
    """ amount = (profit * price of the share) + (profit * price of share) / length
    create profit_combinations like:
    [['Action-4', '70', '14'], ['Action-3', '50', '7.5'], ['Action-2', '30', '3'], total_profit]
    """

    profit_combinations = []

    for combination in budget_combo:
        result_profit = 0

        for i in range(0, len(combination)):
            price = float(combination[i][1])
            profit = float(combination[i][2])
            result_profit += price * profit
        total_profit = round(result_profit / 100, 2)
        combination.append(str(total_profit))
        profit_combinations.append(combination)

    return profit_combinations


def check_duplicate_profit(profit_combo):
    """ check for same value of the profit inside the combinations
     get rid of the duplicates
     """

    duplicate_free_profit_combo = []
    double_profit = []

    for combo in profit_combo:
        profit = combo[3]
        found_duplicat = False

        for double in double_profit:
            if profit == double:
                found_duplicat = True
                break

        if not found_duplicat:
            double_profit.append(profit)
            duplicate_free_profit_combo.append(combo)

    return duplicate_free_profit_combo


def bruteforce(pur_profit):
    """ get the most profitable share combination """

    highest_combo = ""
    highest_profit = 0.0

    for combo in pur_profit:
        # profit: last item of the inner list
        profit = float(combo[-1])

        if profit > highest_profit:
            highest_profit = profit
            highest_combo = combo

    return highest_combo


def print_results(combo, amount_of_shares, budget):
    """ print the results of the bruteforce algorithm. """

    total_profit = combo.pop()
    costs = 0

    print(" ---------------------------------------------------------------")
    print(" ** RESULTS ** ", end='\n\n')
    print(" The share-combination-result of the bruteforce algorythm: ", end='\n\n')
    print(f"  The amount of shares are: {amount_of_shares}.")
    print(f"  The buying budget is: {budget} €.", end='\n\n')

    for i, share in enumerate(combo):
        costs += int(share[1])
        print(f"   {i+1}. share-name: {share[0]}.")
        print(f"    buying price: {share[1]} €.")
        print(f"    profit after 2 years: {share[2]} %.", end='\n\n')

    print(f"  The costs for the shares are: {costs} €.")
    print(f"  The total profit of this share-combination is: {total_profit} %.", end='\n\n')
    print(f"  The process needed {round((time() - start_time), 6)} seconds.", end='\n\n')
