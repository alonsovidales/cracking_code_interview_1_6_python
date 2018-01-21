# Given an in nite number of quarters (25 cents), dimes (10 cents), nickels (5
# cents) and pennies (1 cent), write code to calculate the number of ways of
# representing n cents

PENNIE = 1
NICKEL = 5 * PENNIE
DIME =   10 * PENNIE
QUARTER = 25 * PENNIE

def get_possible_change(cents, ways=None, nickels=0, dimes=0, quarters=0, pennies=0):
    if cents < 0:
        return ways

    if ways is None:
        ways = set()

    if cents == 0:
        ways.add((pennies, nickels, dimes, quarters))

    if nickels == 0:
        for x in xrange(cents/NICKEL):
            ways |= get_possible_change(cents-NICKEL*(x+1), ways, x+1, dimes, quarters, pennies)
    if dimes == 0:
        for x in xrange(cents/DIME):
            ways |= get_possible_change(cents-DIME*(x+1), ways, nickels, x+1, quarters, pennies)
    if quarters == 0:
        for x in xrange(cents/QUARTER):
            ways |= get_possible_change(cents-QUARTER*(x+1), ways, nickels, dimes, x+1, pennies)
    if pennies == 0:
        for x in xrange(cents):
            ways |= get_possible_change(cents-(x+1), ways, nickels, dimes, quarters, x+1)

    return ways

print get_possible_change(10)
print len(get_possible_change(100))
