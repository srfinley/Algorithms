#!/usr/bin/python

import sys



def making_change(amount, denominations):
    total = 0
    if amount == 0:
        return 1
    if not denominations and amount > 0:
        return 0
    if amount < min(denominations):
        return 0
    # for every denomination less than the amount:
    # - determine how many of that denomination could be used (0 through amount // denomination)
    # - for every possible count of that denomination:
    #   - find the number of ways of making change for remaining amount without that denomination
    # end cases:
    # amount zero is passed because that count of a denomination sufficed: return 1
    # amount is less than the smallest denomination: return 0
    # no denominations are passed but value remains: return 0
    denominations = sorted(denominations)[::-1]
    remaining_denoms = denominations.copy()
    for denom in denominations:
        remaining_denoms.remove(denom)
        if amount >= denom:
            maximum = amount // denom
            for count in range(1, maximum+1):
                remainder = amount - (denom * count)
                total += making_change(remainder, remaining_denoms)
    return total

making_change(5, [1,5,10])


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")