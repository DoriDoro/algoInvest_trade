from bruteforce_utils import (
    load_data,
    generate_all_combinations_combinations,
    combinations_budget,
    calculate_profit,
    bruteforce,
    print_results,
)


def combinations_main():
    shares = load_data()
    generate_combinations = generate_all_combinations_combinations(shares)
    combo_budget = combinations_budget(generate_combinations, budget=500)
    cal_profit = calculate_profit(combo_budget)
    result = bruteforce(cal_profit)
    print_results(result)


if __name__ == '__menu__':
    combinations_main()
