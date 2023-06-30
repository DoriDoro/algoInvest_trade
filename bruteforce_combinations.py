from bruteforce_utils import (
    load_data,
    load_pseudo_data,
    generate_all_combinations_combinations,
    combinations_budget,
    calculate_profit,
    bruteforce,
    print_results,
)


def bruteforce_combinations_main():
    amount_of_shares = 0

    while True:
        print(" ---------------------------------------------------------------")
        print(" ** choose the data ** ", end='\n\n')
        print("  1. pseudo_share_date with 4 shares")
        print("  2. share_data with 20 shares")
        print("  3. go back to Main Menu", end='\n\n')

        choice = int(input("  Please enter your choice: "))
        print()

        if choice == 1:
            shares = load_pseudo_data()
            print("  You have chosen the pseudo_share_data with 4 shares.", end='\n\n')
            amount_of_shares = shares[-1]
            break
        elif choice == 2:
            shares = load_data()
            print("  You have chosen the share_data with 20 shares.", end='\n\n')
            amount_of_shares = shares[-1]
            break
        elif choice == 3:
            return
        else:
            print("   Invalid choice. Please enter a number between 1 and 3.", end='\n\n')

    print(" ---------------------------------------------------------------")
    print(" ** choose the budget ** ", end='\n\n')
    budget = int(input("  Please enter the budget: "))
    print()

    generate_combinations = generate_all_combinations_combinations(shares)
    combo_budget = combinations_budget(generate_combinations, budget)
    cal_profit = calculate_profit(combo_budget)
    result = bruteforce(cal_profit)
    print_results(result, amount_of_shares, budget)


if __name__ == '__menu__':
    bruteforce_combinations_main()
