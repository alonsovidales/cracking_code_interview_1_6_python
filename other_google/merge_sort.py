def merge_sort(arr):
    print arr
    if len(arr) <= 1:
        return arr

    l = merge_sort(arr[:len(arr)/2])
    r = merge_sort(arr[len(arr)/2:])

    new_arr = []
    lp = 0
    rp = 0
    while lp < len(l) or rp < len(r):
        if lp >= len(l):
            new_arr += r[rp:]
            break
        elif rp >= len(r):
            new_arr += l[lp:]
            break
        else:
            if l[lp] < r[rp]:
                new_arr.append(l[lp])
                lp += 1
            else:
                new_arr.append(r[rp])
                rp += 1

    return new_arr

print merge_sort([4, 2, 9, 3, 4, 0, 1, 2, 9])
