
def coinChange(s, amount):
    if amount < 0:
        return float('inf')
    if amount == 0:
        return 0
    
    minCoins = float('inf')
    for coin in s:
        coins = coinChange(s, amount - coin) + 1
        if minCoins > coins:
            minCoins = coins
            
    return minCoins

s = [1,3,5,7]
amount = 18
print(coinChange(s, amount))