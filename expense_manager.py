import json

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(amount, category, date):
    expenses = load_expenses()
    expenses.append({
        "amount": amount,
        "category": category,
        "date": date
    })
    save_expenses(expenses)

def total_expense():
    expenses = load_expenses()
    return sum(exp["amount"] for exp in expenses)