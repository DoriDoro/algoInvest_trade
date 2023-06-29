import csv

from itertools import combinations


def main():
    shares = load_data()
    generate_combinations = generate_all_combinations(shares)
    combo_budget = combinations_budget(generate_combinations)
    cal_profit = calculate_profit(combo_budget)
    result = bruteforce(cal_profit)
    print_results(result)


def load_data():
    """ load the share data from a csv file """
    data_shares = []

    with open('data_shares.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data_shares.append(row)

    # remove first list with header
    data_shares = data_shares[1:]

    return data_shares


def generate_all_combinations(data_of_shares):
    """ generates all possible combinations with `itertools.combinations` """

    all_possible_combinations = []

    for i in range(len(data_of_shares) + 1):
        combos = combinations(data_of_shares, i)

        for combo in combos:
            all_possible_combinations.append(combo)

    return all_possible_combinations


def combinations_budget(possible_combo):
    """ uses all possible combinations to check them and include the budget, budget = 500 """

    budget_combinations = []

    for combination in possible_combo:
        current_combinations = []
        budget = 500

        for combo in combination:
            if budget - int(combo[1]) >= 0:
                budget -= int(combo[1])
                current_combinations.append(combo)

        budget_combinations.append(current_combinations)

    return budget_combinations


def calculate_profit(budget_combo):
    """ amount = (profit * price of the share) + (profit * price of share) / length
    create profit_combinations like:
    [['Action-4', '70', '14'], ['Action-3', '50', '7.5'], ['Action-2', '30', '3'], average_profit]
    """

    profit_combinations = []

    for combination in budget_combo:
        result_profit = 0

        if len(combination) > 0:
            for i in range(0, len(combination)):
                price = float(combination[i][1])
                profit = float(combination[i][2])
                result_profit += price * profit
            average_profit = round(result_profit / len(combination), 2)
            combination.append(str(average_profit))
            profit_combinations.append(combination)

    return profit_combinations


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


def print_results(combo):
    """ print the final result of the found share combination """
    total_profit = combo.pop()

    print("The share-combination-result of the bruteforce algorythm: ", end='\n\n')

    for i, share in enumerate(combo):
        print(f"  {i+1}. share-name: {share[0]}")
        print(f"   buying price: {share[1]} €")
        print(f"   profit after 2 years: {share[2]} €", end='\n\n')

    print(f"  The total profit of this share-combination is: {total_profit} €", end='\n\n')


main()
