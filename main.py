from expense_manager import total_expense
from investment_engine import calculate_savings, investment_suggestion

def get_investment_plan(income, risk):
    expense = total_expense()
    savings = calculate_savings(income, expense)
    plan = investment_suggestion(savings, risk)
    return savings, plan