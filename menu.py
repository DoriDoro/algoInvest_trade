from bruteforce import bruteforce_main
from optimization_branch_bound import optimization_bb_main
from optimization_greedy import optimization_main


def run_menu():
    while True:
        print(" ---------------------------------------------------------------")
        print(" ** MAIN MENU **", end='\n\n')
        print("  chose a file or exit the program:")
        print("   1. bruteforce.py")
        print("   2. optimization_greedy.py")
        print("   3. optimization_branch_bound.py")
        print("   4. Quit program", end='\n\n')

        choice = int(input("  Please enter your choice of the file: "))
        print()

        if choice == 1:
            bruteforce_main('bruteforce')
        elif choice == 2:
            optimization_main('optimization_greedy')
        elif choice == 3:
            optimization_bb_main('optimization_branch_bound')
        elif choice == 4:
            break
        else:
            print("  Invalid choice. Please enter a number between 1 and 2.", end='\n\n')
