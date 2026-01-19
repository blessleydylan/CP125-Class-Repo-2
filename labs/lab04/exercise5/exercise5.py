def price_change(prices, day):
    return prices[day] - prices[day - 1]


def is_momentum_day(prices, day):
    if day < 2:
        return False 

    today_change = price_change(prices, day)
    prev_change = price_change(prices, day - 1)

    return today_change > 0 and today_change > prev_change


def find_momentum_days(prices):

    momentum_days = []

    for day in range(2, len(prices)):
        if is_momentum_day(prices, day):
            momentum_days.append(day)

    return momentum_days


# Test
prices = [100, 102, 105, 107, 106, 108, 112, 114]
result = find_momentum_days(prices)
print(f"Momentum days: {result}")  # Expected: [2, 5, 6]
