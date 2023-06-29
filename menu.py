from pseudo_bruteforce import pseudo_main
from bruteforce_permutations import permutations_main
from bruteforce_combinations import combinations_main


def run_menu():
    while True:
        print(" ** MAIN MENU **")
        print(" chose a file:")
        print(" 1. pseudo_bruteforce.py  -- uses itertools.permutations with just 4 shares")
        print(" 2. bruteforce_permutations.py  -- is just working with the pseudo_share_data")
        print(" 3. bruteforce_combinations.py  -- uses itertools.combinations with 20 shares")
        print(" 4. Quit program", end='\n\n')

        choice = int(input("  Please enter your choice: "))
        print()

        if choice == 1:
            pseudo_main()
        elif choice == 2:
            permutations_main()
        elif choice == 3:
            combinations_main()
        elif choice == 4:
            break
        else:
            print("  Invalid choice. Please enter a number between 1 to 4.")
