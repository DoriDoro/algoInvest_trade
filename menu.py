from bruteforce import bruteforce_main
from optimization import optimization_main


def run_menu():
    while True:
        print(" ---------------------------------------------------------------")
        print(" ** MAIN MENU **", end='\n\n')
        print("  chose a file or exit the program:")
        print("   1. bruteforce.py")
        print("   2. optimization.py")
        print("   3. Quit program", end='\n\n')

        choice = int(input("  Please enter your choice: "))
        print()

        if choice == 1:
            bruteforce_main('bruteforce')
        elif choice == 2:
            optimization_main('optimization')
        elif choice == 3:
            break
        else:
            print("  Invalid choice. Please enter a number between 1 and 2.", end='\n\n')
