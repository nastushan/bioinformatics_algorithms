'''

Find the Minimum Number of Coins Needed to Make Change

The Change Problem
Find the minimum number of coins needed to make change.

Given: An integer money and an array Coins of positive integers.

Return: The minimum number of coins with denominations Coins that changes money.

'''

def MinCoinsNum(money, coins):
    mincoins = {0:0}
    for i in range(1, money + 1):
        mincoins[i] = 10000
        
        for j in range(len(coins)):
            if i < coins[j]:
                continue
            numcoins = mincoins[i - coins[j]] + 1
            if numcoins < mincoins[i]:
                mincoins[i] = numcoins
    
    return mincoins[money]

if __name__ == "__main__":
    
    money = 19354
    coins = [1,3,5,9,11,15,16,18,24]
    
    print(MinCoinsNum(money, coins))