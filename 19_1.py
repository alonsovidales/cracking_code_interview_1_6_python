# Write a function to swap a number in place without temporary variables

def swap(x, y):
    x[0] ^= y[0]
    y[0] ^= x[0]
    x[0] ^= y[0]

x = [21]
y = [19]
swap(x, y)

print x[0], y[0]
