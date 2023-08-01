from time import time
import pandas as pd

from bruteforce_utils import (
    load_data,
    generate_all_combinations,
    combinations_budget,
    calculate_profit,
    bruteforce,
    print_results,
)


def bruteforce_main(name_of_file):

    while True:
        print(" ---------------------------------------------------------------")
        print(" ** choose the data ** ", end='\n\n')
        print("  1. share_data with 4 shares")
        print("  2. share_data with 20 shares")
        print("  3. dataset 1 with about 1000 shares")
        print("  4. dataset 2 with about 1000 shares")
        print("  5. go back to Main Menu", end='\n\n')

        choice = int(input("  Please enter your choice of the data: "))
        print()

        if choice == 1:
            share_data = load_data('pseudo_data_shares')
            print("  You have chosen the share_data with 4 shares.", end='\n\n')
            amount_of_shares = len(share_data)
            break
        elif choice == 2:
            share_data = load_data('data_shares')
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

    generate_combinations = generate_all_combinations(share_data)
    combo_budget = combinations_budget(generate_combinations, budget)
    cal_profit = calculate_profit(combo_budget)
    result = bruteforce(combo_budget, cal_profit)
    print_results(result, amount_of_shares, budget, start_time, name_of_file)


if __name__ == '__menu__':
    bruteforce_main()
