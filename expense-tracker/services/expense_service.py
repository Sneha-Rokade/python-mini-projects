from models.expense import Expense
from utils.file_handler import load_expenses, save_expenses

def add_expense():
    title = input("Enter title: ")
    amount = input("Enter amount: ")
    category = input("Enter category: ")

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

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['title']} - ₹{exp['amount']} ({exp['category']})")

def total_expense():
    expenses = load_expenses()

    total = sum(exp["amount"] for exp in expenses)

    print(f"💰 Total Expense: ₹{total}")

