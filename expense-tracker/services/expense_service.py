from models.expense import Expense
from utils.file_handler import load_expenses, save_expenses

def add_expense():
    title = input("Enter title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    expenses = load_expenses()

    expense = Expense(title, amount, category)
    expenses.append(expense.to_dict())

    save_expenses(expenses)

    print("✅ Expense added!")

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expense List ---")

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['title']:<15} ₹{exp['amount']:<10} {exp['category']}")

def total_expense():
    expenses = load_expenses()

    total = sum(exp["amount"] for exp in expenses)

    print(f"💰 Total Expense: ₹{total}")


def delete_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        index = int(input("Enter expense number to delete: ")) - 1

        if index < 0 or index >= len(expenses):
            print("Invalid index.")
            return

        removed = expenses.pop(index)
        save_expenses(expenses)

        print(f"Deleted: {removed['title']}")

    except ValueError:
        print("Please enter a valid number.")

def search_by_category():
    category = input("Enter category to search: ").lower()

    expenses = load_expenses()

    filtered = [
        exp for exp in expenses
        if exp["category"].lower() == category
    ]

    if not filtered:
        print("No matching expenses found.")
        return

    for exp in filtered:
        print(f"{exp['title']} - ₹{exp['amount']} ({exp['category']})")

