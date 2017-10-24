# -*- coding: utf-8 -*-
"""
    Coin change
    ~~~~~~~~~~~
    https://leetcode.com/problems/coin-change/description/
    ~~~~~~~~~~~
    类似问题：剪绳子
"""


def coin_change(coins, amount):
    MAX = amount + 1  # or use float('inf')
    records = [MAX for _ in range(amount+1)]
    records[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                records[i] = min(records[i], records[i-coin]+1)
        # records[i] = min(records[i-c] if i >= c else MAX for c in coins) + 1
    return -1 if records[amount] > amount else records[amount]


def coin_change_bfs(coins, amount):
    level = seen = {0}
    number = 0
    while level:
        if amount in level:
            return number
        level = {a+c for a in level for c in coins if a+c <= amount} - seen
        seen |= level
        number += 1
    return -1


def old_coin_change(values, money):
    coins_used = {i: 0 for i in range(money+1)}
    for cents in range(1, money+1):
        min_coins = cents
        for value in values:
            if value <= cents:
                temp = coins_used[cents-value] + 1
                if temp < min_coins:
                    min_coins = temp

        coins_used[cents] = min_coins
        msg = '面值为: {0} 的最小硬币数目为: {1}'
        print(msg.format(cents, coins_used[cents]))


if __name__ == '__main__':
    values = [25, 21, 10, 5, 1]
    money = 63
    old_coin_change(values, money)
    print(coin_change(values, money))
