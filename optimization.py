from time import time

from bruteforce_utils import load_data, print_results


def optimization_main(name_of_file):
    start_time = time()

    while True:
        print(" ---------------------------------------------------------------")
        print(" ** choose the data ** ", end='\n\n')
        print("  1. share_data with 4 shares")
        print("  2. share_data with 20 shares")
        print("  3. go back to Main Menu", end='\n\n')

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
            return
        else:
            print("   Invalid choice. Please enter a number between 1 and 3.", end='\n\n')

    print(" ---------------------------------------------------------------")
    print(" ** choose the budget ** ", end='\n\n')
    budget = int(input("  Please enter the budget: "))
    print()

    # sort loaded data of shares by highest profit first:
    data_sorted = sorted(share_data, key=lambda x: x[2], reverse=True)

    cost = budget
    shares_list = []
    result_profit = 0
    combination = {}

    for a, b, c in data_sorted:
        if cost - b >= 0:
            cost -= b

            profit = b * c
            result_profit += profit

            shares_list.append([a, b, c])

    total_profit = round(result_profit / 100, 2)

    combination['combo'] = shares_list
    combination['total_profit'] = total_profit

    print_results(combination, amount_of_shares, budget, start_time, name_of_file)


if __name__ == '__menu__':
    optimization_main()
