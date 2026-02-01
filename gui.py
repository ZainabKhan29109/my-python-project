import tkinter as tk
from tkinter import messagebox
from expense_manager import add_expense, total_expense
from investment_engine import calculate_savings, investment_suggestion


# ---------------- ADD EXPENSE ----------------
def add_expense_gui():
    try:
        amount_text = amount_entry.get().strip()

        if not amount_text.replace(".", "").isdigit():
            raise ValueError

        amount = float(amount_text)
        category = category_entry.get().strip()
        date = date_entry.get().strip()

        if category == "" or date == "":
            raise ValueError

        add_expense(amount, category, date)
        messagebox.showinfo("Success", "Expense added successfully!")

        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid expense details")


# ---------------- INVESTMENT PLAN ----------------
def show_investment_plan():
    try:
        income_text = income_entry.get().strip()

        if not income_text.replace(".", "").isdigit():
            raise ValueError

        income = float(income_text)
        risk = risk_var.get()

        expense = total_expense()
        savings = calculate_savings(income, expense)
        plan = investment_suggestion(savings, risk)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Total Expense: {expense}\n")
        result_text.insert(tk.END, f"Savings: {savings}\n\n")
        result_text.insert(tk.END, "Investment Plan:\n")

        for k, v in plan.items():
            result_text.insert(tk.END, f"{k}: {round(v, 2)}\n")

    except ValueError:
        messagebox.showerror("Error", "Please enter numeric income only")


# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Personal Finance & Investment App")
root.geometry("420x520")

# ---------- Expense Section ----------
tk.Label(root, text="Add Expense", font=("Arial", 12, "bold")).pack(pady=5)

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Date (DD/MM/YYYY)").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense_gui).pack(pady=5)

# ---------- Investment Section ----------
tk.Label(root, text="Investment Planner", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(root, text="Monthly Income").pack()
income_entry = tk.Entry(root)
income_entry.pack()

tk.Label(root, text="Risk Level").pack()
risk_var = tk.StringVar(value="low")
tk.OptionMenu(root, risk_var, "low", "medium", "high").pack(pady=5)

tk.Button(root, text="Show Investment Plan", command=show_investment_plan).pack()

result_text = tk.Text(root, height=10)
result_text.pack(pady=10)

# --------- VERY IMPORTANT: START THE APP ---------
root.mainloop()