from bruteforce_utils import (
    load_pseudo_data,
    generate_all_combinations_permutations,
    combinations_budget,
    calculate_profit,
    check_duplicate_profit,
    bruteforce,
    print_results,
)


def permutations_main():
    shares = load_pseudo_data()
    generate_combinations = generate_all_combinations_permutations(shares)
    combo_budget = combinations_budget(generate_combinations, budget=150)
    cal_profit = calculate_profit(combo_budget)
    check_double_profit = check_duplicate_profit(cal_profit)
    result = bruteforce(check_double_profit)
    print_results(result)


if __name__ == '__menu__':
    permutations_main()
