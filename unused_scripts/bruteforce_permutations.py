from bruteforce_utils import (
    load_data,
    generate_all_combinations_permutations,
    combinations_budget,
    calculate_profit,
    check_duplicate_profit,
    bruteforce,
    print_results,
)


def bruteforce_permutations_main():
    shares = load_data('pseudo_data_shares')
    generate_combinations = generate_all_combinations_permutations(shares)
    combo_budget = combinations_budget(generate_combinations, budget=150)
    cal_profit = calculate_profit(combo_budget)
    check_double_profit = check_duplicate_profit(cal_profit)
    result = bruteforce(check_double_profit)
    print_results(result, amount_of_shares=4, budget=150)


if __name__ == '__menu__':
    bruteforce_permutations_main()
