def sort(a, b, end_a):
    pos = len(a)-1
    lb = b.pop()
    while True:
        if end_a >= 0 and a[end_a] > lb:
            a[pos] = a[end_a]
            end_a -= 1
        else:
            a[pos] = lb
            try:
                lb = b.pop()
            except:
                return a

        pos -= 1

b = [1, 3, 4, 8, 9]
a = [2, 3, 3, 4, 10]
la = len(a)-1
a += [None]*len(b)
print sort(a, b, la)
