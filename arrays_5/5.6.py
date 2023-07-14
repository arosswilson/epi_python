prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
def stock_market(prices: list):
    cur_low = prices[0]
    greatest_profit = 0
    for price in prices:
        if price > cur_low and price - cur_low > greatest_profit:
            greatest_profit = price - cur_low
        elif price < cur_low:
            cur_low = price
    return greatest_profit

print(stock_market(prices))
