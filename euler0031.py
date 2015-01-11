#!/usr/bin/python
# -*- coding: utf-8 -*-
r"""Coin sums

    In England the currency is made up of pound, £, and pence, p, and there are
    eight coins in general circulation:

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

    It is possible to make £2 in the following way:

    $1\times £1 + 1\times 50p + 2\times 20p + 1\times 5p + 1\times 2p + 3\times
    1p$

    How many different ways can £2 be made using any number of coins?"""

def coinings(amount, coins):
    """Returns the number of ways to make `amount` pence using only the
       denominations in the (descending) list `coins`"""
    if amount == 0:
        return 1
    elif not coins:
        return 0
    elif coins == [2,1]:
    # This optimization alone is enough to reduce the runtime from 3.5s to 0.7s
    # on my machine.
        return amount // 2 + 1
    else:
        return sum(coinings(amount-x, coins[1:])
                   for x in range(0, amount+1, coins[0]))

print coinings(200, [200, 100, 50, 20, 10, 5, 2, 1])
