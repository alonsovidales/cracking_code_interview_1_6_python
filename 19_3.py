# Write an algorithm which computes the number of trailing zeros in n factorial

def fact(n):
    if n == 1:
        return 1

    return n * fact(n-1)

result = fact(10)
zeroes = 1
while result % zeroes == 0:
    zeroes *= 10

print result
print len(str(zeroes))-2
