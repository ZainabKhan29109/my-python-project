def calculate_savings(income, total_expense):
    return income - total_expense

def investment_suggestion(savings, risk):
    if savings <= 0:
        return {"Message": "No savings available"}

    if risk == "low":
        return {
            "Fixed Deposit": savings * 0.7,
            "Gold": savings * 0.3
        }

    elif risk == "medium":
        return {
            "Mutual Funds": savings * 0.6,
            "Stocks": savings * 0.4
        }

    elif risk == "high":
        return {
            "Stocks": savings * 0.6,
            "Crypto": savings * 0.4
        }

    else:
        return {"Error": "Invalid risk level"}