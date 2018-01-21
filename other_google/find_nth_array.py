# Find the nth smallest number in an unsorted array

def find(arr, nth):
    lo = 0
    hi = len(arr)-1
    pivot = (hi-lo)/2+lo

    while pivot != nth and lo < hi:
        print "Arr:", arr, lo, hi
        pivot = (hi-lo)/2+lo

        while lo < hi:
            print lo, hi, arr
            if arr[lo] <= arr[pivot]:
                lo += 1
            elif arr[hi] >= arr[pivot]:
                hi -= 1
            else:
                arr[hi] ^= arr[lo]
                arr[lo] ^= arr[hi]
                arr[hi] ^= arr[lo]

        if arr[lo] > arr[hi]:
            arr[hi] ^= arr[lo]
            arr[lo] ^= arr[hi]
            arr[hi] ^= arr[lo]

        if pivot < nth:
            lo = pivot
        elif pivot > nth:
            hi = pivot

    print "Arr:", arr
    return arr[nth]

print find([4, 3, 9, 3, 4, 5, 1], 2)
