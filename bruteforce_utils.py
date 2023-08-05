import csv
import os
import psutil

from itertools import combinations
from itertools import permutations
from time import time


def load_data(name_of_file):
    """load the shares data from a csv file with 4 or 20 shares"""

    data_shares = []

    with open(f"data/{name_of_file}.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data_shares.append(row)

    # remove first list with header
    data_shares = data_shares[1:]
    data_shares = [(a, float(b), float(c)) for a, b, c in data_shares]

    return data_shares


def generate_all_combinations(data_of_shares):
    """generates all possible combinations with `itertools.combinations`"""

    all_possible_combinations = []

    for i in range(len(data_of_shares) + 1):
        combos = combinations(data_of_shares, i)

        for combo in combos:
            all_possible_combinations.append(combo)

    return all_possible_combinations


def generate_all_combinations_permutations(data_of_shares):
    """generates all possible combinations with `itertools.permutations`"""

    all_possible_combinations_permutations = []

    for combo in permutations(data_of_shares, len(data_of_shares)):
        all_possible_combinations_permutations.append(combo)

    return all_possible_combinations_permutations


def combinations_budget(possible_combo, budget):
    """uses all possible combinations to check them and include the budget"""

    budget_combinations = []

    for combination in possible_combo:
        current_combinations = []
        remaining_budget = budget

        for combo in combination:
            if remaining_budget - combo[1] >= 0:
                remaining_budget -= combo[1]
                current_combinations.append(combo)

        budget_combinations.append(current_combinations)

    return budget_combinations


def calculate_profit(budget_combo):
    """calculate the profit of all combinations
    (price * profit) + (price * profit)
    """

    profit_combinations = []

    for combination in budget_combo:
        result_profit = 0

        for i in range(0, len(combination)):
            price = combination[i][1]
            profit = combination[i][2]
            result_profit += price * profit

        total_profit = round(result_profit / 100, 2)
        profit_combinations.append(total_profit)

    return profit_combinations


def check_duplicate_profit(profit_combo):
    """check for same value of the profit inside the itertools.permutations combinations
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


def bruteforce(budget_combo, profit_combo):
    """get the most profitable share combination"""

    highest_profit = 0.0
    highest_combo = {}

    for i, profit in enumerate(profit_combo):
        if profit > highest_profit:
            highest_profit = profit
            index = i

    highest_combo["combo"] = budget_combo[index]
    highest_combo["total_profit"] = highest_profit

    return highest_combo


def print_results(combination, amount_of_shares, budget, start_time, name_of_file):
    """print the results of the bruteforce algorithm."""

    costs = 0

    print(" ---------------------------------------------------------------")
    print(" ** RESULTS ** ", end="\n\n")
    print(" The share-combination-result of the bruteforce algorythm: ", end="\n\n")

    print(f"  You have chosen: {name_of_file}.py")
    print(f"  The amount of shares are: {amount_of_shares}.")
    print(f"  The buying budget is: {budget} €.", end="\n\n")

    for i, share in enumerate(combination["combo"]):
        costs += share[1]
        print(f"   {i+1}. name: {share[0]}, price: {share[1]}, profit: {share[2]}")
    print()
    print(f"  The costs for the shares are: {round(costs, 2)} €.")
    print(
        f"  The total profit of this share-combination is: "
        f"{combination['total_profit']} %.",
    )
    print(f"  The process needed {round((time() - start_time), 6)} seconds.")
    print(
        f"  RAM used by the program: "
        f"{round((psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)), 3)} MB",
        end="\n\n",
    )
