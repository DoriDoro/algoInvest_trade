from time import time

import pandas as pd

from bruteforce_utils import load_data, print_results


def optimization_bb_main(name_of_file):

    while True:
        print(" ---------------------------------------------------------------")
        print(" ** choose the data ** ", end='\n\n')
        print("  1. share_data with 4 shares")
        print("  2. share_data with 20 shares")
        print("  3. dataset 1 with about 1000 shares")
        print("  4. dataset 2 with about 1000 shares")
        print("  5. go back to Main Menu", end='\n\n')

        choice = int(input("  Please enter your choice: "))
        print()

        if choice == 1:
            pseudo = 'pseudo_data_shares'
            share_data = load_data(pseudo)
            print("  You have chosen the share_data with 4 shares.", end='\n\n')
            amount_of_shares = len(share_data)
            break
        elif choice == 2:
            all_shares = 'data_shares'
            share_data = load_data(all_shares)
            print("  You have chosen the share_data with 20 shares.", end='\n\n')
            amount_of_shares = len(share_data)
            break
        elif choice == 3:
            share_data = pd.read_csv('data/dataset1_P7.csv')
            print("  You have chosen the share_data with about 1000 shares.", end='\n\n')
            amount_of_shares = len(share_data)
            break
        elif choice == 4:
            share_data = pd.read_csv('data/dataset2_P7.csv')
            print("  You have chosen the share_data with about 1000 shares.", end='\n\n')
            amount_of_shares = len(share_data)
            break
        elif choice == 5:
            return
        else:
            print("   Invalid choice. Please enter a number between 1 and 3.", end='\n\n')

    print(" ---------------------------------------------------------------")
    print(" ** choose the budget ** ", end='\n\n')
    budget = int(input("  Please enter the budget: "))
    print()

    start_time = time()

    if amount_of_shares > 21:

        # Remove duplicates from shared_data
        share_data.drop_duplicates(inplace=True)

        # Remove rows with 0 and negative values
        share_data = share_data[~(share_data['price'] <= 0)]

        # Convert the pandas DataFrame beck to a list with tuples
        share_data = [tuple(data) for data in share_data.to_numpy()]

    # sort loaded data of shares by highest profit first:
    data_sorted = sorted(share_data, key=lambda x: x[2], reverse=True)
    print('sorted data', data_sorted)

    cost = budget
    shares_list = []
    result_profit = 0

    combination = {}

    """
        1. sort the dataset, done data_sorted
        2. set result_profit = 0, done
        3. for loop
        4. create criteria set budget, done: cost = budget
            5.1 first row of shares data
            5.2 calculate the result_profit, if next profit is higher then result_profit update result_profit
            5.3 check the budget, if budget == 0
            5.4 if budget is < budget, check other shares in the dataset if fits to improve the profit
    """
    index = 0
    while index < len(data_sorted) and cost > 0:
        a, b, c = data_sorted[index]
        if cost - b >= 0:
            cost -= b

            profit = b * c
            result_profit += profit

            shares_list.append([a, b, c])

        else:
            index += 1

    total_profit = round(result_profit / 100, 2)

    combination['combo'] = shares_list
    combination['total_profit'] = total_profit

    print_results(combination, amount_of_shares, budget, start_time, name_of_file)


if __name__ == '__menu__':
    optimization_bb_main()
