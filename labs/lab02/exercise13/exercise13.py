
def get_rate_per_kg(destination):
    """
    Returns 5.0 for Domestic, 15.0 for International.
    """
    # TODO: Implement this function
    if destination == "Domestic":
        rate = 5.0
    elif destination == "International":
        rate = 15.0
    return rate

def get_express_charge(is_express):
    """
    Returns 10.0 if is_express is True, otherwise 0.0.
    """
    # TODO: Implement this function
    if is_express:
        return 10.0
    else:
        return 0.0

def calculate_shipping_quote(weight, destination, is_express):
    """
    Calculates final quote: (weight * rate) + express_charge
    """
    # TODO: Implement this function
    final_quote = (weight * get_rate_per_kg(destination)) + get_express_charge(is_express)
    return final_quote
