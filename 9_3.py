"""
Given a sorted array of n integers that has been rotated an unknown number of
times,giveanO(logn)algorithmthat ndsanelementinthearray Youmayassume that the
array was originally sorted in increasing order
EXAMPLE:
Input:  nd 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
Output: 8 (the index of 5 in the array)
"""

def get_pos(arr, x, lo=0, hi=None):
    hi = len(arr)-1

    while hi > lo:
        m = (hi-lo)/2+lo
        if arr[m] == x:
            return m
        if arr[hi] == x:
            return hi
        if arr[lo] == x:
            return lo

        if arr[lo] < arr[m]:
            if x <= arr[m] and x >= arr[lo]:
                hi = m
            else:
                lo = m
        else:
            if x >= arr[m] and x <= arr[hi]:
                lo = m
            else:
                hi = m

    return None

print get_pos((15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14), 5)
print get_pos((15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14), 15)
print get_pos((15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14), 14)
print get_pos((15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14), 19)
