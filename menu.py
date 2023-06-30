from pseudo_bruteforce import pseudo_bruteforce_main
from bruteforce_permutations import bruteforce_permutations_main
from bruteforce_combinations import bruteforce_combinations_main


def run_menu():
    while True:
        print(" ---------------------------------------------------------------")
        print(" ** MAIN MENU **", end='\n\n')
        print("  chose a file:")
        print("   1. pseudo_bruteforce.py  -- uses itertools.permutations with just 4 shares")
        print("   2. bruteforce_permutations.py  -- uses itertools.permutations "
              "and is just working with the pseudo_share_data (4 shares)")
        print("   3. bruteforce_combinations.py  -- uses itertools.combinations "
              "with choice of shares")
        print("   4. Quit program", end='\n\n')

        choice = int(input("  Please enter your choice: "))
        print()

        if choice == 1:
            pseudo_bruteforce_main()
        elif choice == 2:
            bruteforce_permutations_main()
        elif choice == 3:
            bruteforce_combinations_main()
        elif choice == 4:
            break
        else:
            print("  Invalid choice. Please enter a number between 1 and 4.", end='\n\n')
