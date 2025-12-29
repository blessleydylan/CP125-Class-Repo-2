
def is_valid_multiple(amount):
    """
    Checks if the amount is a multiple of RM10.
    """
    # TODO: Implement this function
    if amount % 10 == 0 and amount > 0:
        return True
    else:
        return False

def is_balance_sufficient(amount, balance):
    """
    Checks if the balance is enough for the withdrawal.
    """
    # TODO: Implement this function
    if balance >= amount:
        return True
    else:
        return False

def process_withdrawal(amount, balance):
    """
    Processes the withdrawal.
    Returns the new balance if successful.
    Returns "Invalid Amount" if not a multiple of 10.
    Returns "Insufficient Funds" if balance is too low.
    """
    # TODO: Implement this function
    if amount == 0 or amount % 10 != 0:
        return "Invalid Amount"
    elif amount <= balance and amount % 10 == 0:
        leftover_balance = balance - amount
        return leftover_balance
    else:
        return "Insufficient Funds"


print(process_withdrawal(0,100))