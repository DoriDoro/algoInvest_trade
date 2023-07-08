from bruteforce_combinations import bruteforce_combinations_main


def run_menu():
    while True:
        print(" ---------------------------------------------------------------")
        print(" ** MAIN MENU **", end='\n\n')
        print("  chose a file or exit the program:")
        print("   1. bruteforce_combinations.py")
        print("   2. Quit program", end='\n\n')

        choice = int(input("  Please enter your choice: "))
        print()

        if choice == 1:
            bruteforce_combinations_main()
        elif choice == 2:
            break
        else:
            print("  Invalid choice. Please enter a number between 1 and 2.", end='\n\n')
