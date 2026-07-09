from services.expense_service import *

def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Delete Expense")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()