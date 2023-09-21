def max_stock_profit(prices):
    # Initialize variables to track the minimum price and maximum profit
    min_price = float('inf')
    max_profit = 0
    buy_day = 0
    sell_day = 0

    # Iterate over the prices and update the minimum price and maximum profit
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            sell_day = i

    # If no profit can be made, return -1
    if max_profit == 0:
        return -1

    # Otherwise, return the maximum profit and the buy/sell days and prices
    return f"Buy on day {buy_day+1} at price {prices[buy_day]}\nSell on day {sell_day+1} at price {prices[sell_day]}\nMax profit: {max_profit}"

# Example usage
prices = [100, 180, 260, 310, 40, 535, 695]
max_profit = max_stock_profit(prices)
print(max_profit)  # Output: 'Buy on day 5 at price 40\nSell on day 7 at price 695\nMax profit: 655'
