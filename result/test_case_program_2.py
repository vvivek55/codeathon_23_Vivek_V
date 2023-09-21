def test_max_stock_profit():
    # Test finding the maximum profit for a list of prices
    assert max_stock_profit([100, 180, 260, 310, 40, 535, 695]) == "Buy on day 5 at price 40\nSell on day 7 at price 695\nMax profit: 655"

    # Test finding the maximum profit for a list of prices with decreasing values
    assert max_stock_profit([50, 40, 30, 20, 10]) == -1

    # Test finding the maximum profit for a list of prices with equal values
    assert max_stock_profit([10, 10, 10, 10, 10]) == -1

    # Test finding the maximum profit for a list of prices with only one price
    assert max_stock_profit([10]) == -1

    # Test finding the maximum profit for a list of prices with multiple maximum profits
    assert max_stock_profit([10, 20, 30, 20, 10]) == "Buy on day 1 at price 10\nSell on day 3 at price 30\nMax profit: 20"

test_max_stock_profit()
