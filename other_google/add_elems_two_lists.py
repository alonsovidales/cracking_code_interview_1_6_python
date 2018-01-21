"""
Given two integer arrays list1 and list2 and an int target value. WAP to check
if there exists such a sum, where one number taken from list1 and other from
list2 to add up to become the target value. Return true if so, else return
false.
"""

import unittest

def two_sum_lists(l1, l2, total):
    l1_set = set(l1)
    for e in l2:
        if total-e in l1_set:
            return True

    return False

import unittest

class TestTwoSum(unittest.TestCase):
    def TestFound(self):
        self.assertTrue(two_sum_lists([1, 2, 3, 4, 5], [4, 3, 2, 9, 10], 15))

    def NotFound(self):
        self.assertFalse(two_sum_lists([], [4, 3, 2, 9, 10], 4))
        self.assertFalse(two_sum_lists([1, 2, 3, 4, 5], [], 4))
        self.assertFalse(two_sum_lists([1, 2, 3, 4, 5], [4, 3, 2, 9, 10], 222))

if __name__ == '__main__':
    unittest.main()
