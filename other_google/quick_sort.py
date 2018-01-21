def quick_sort(arr, in_lo=0, in_hi=-1):
    if in_hi == -1:
        in_hi = len(arr)-1

    if in_lo >= in_hi:
        return arr

    print "IN:", arr[in_lo:in_hi+1], in_lo, in_hi

    pivot = arr[in_lo]
    hi = in_hi
    lo = in_lo+1
    while lo < hi:
        print "IN loop:", lo, hi
        while arr[lo] < pivot and lo < in_hi:
            lo += 1
        while arr[hi] > pivot and hi > in_lo:
            hi -= 1

        print "End:", lo, hi, pivot, arr
        if lo < hi:
            arr[lo] ^= arr[hi] 
            arr[hi] ^= arr[lo] 
            arr[lo] ^= arr[hi] 

    arr[in_lo] ^= arr[hi] 
    arr[hi] ^= arr[in_lo] 
    arr[in_lo] ^= arr[hi] 

    quick_sort(arr, in_lo, hi-1)
    quick_sort(arr, hi+1, in_hi)

    return arr


print "Result:", quick_sort([2, 4, 5, 1, 5, 9, 7])
print "Result:", quick_sort([2, 1])
print "Result:", quick_sort([1])
