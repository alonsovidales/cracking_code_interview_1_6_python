"""
A circus is designing a tower routine consisting of people standing atop one
anoth- er's shoulders For practical and aesthetic reasons, each person must be
both shorter and lighter than the person below him or her Given the heights and
weights of each person in the circus, write a method to compute the largest
possible number of peo- ple in such a tower
EXAMPLE:
Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
Output: The longest tower is length 6 and includes from top to bottom: (56, 90)
(60,95) (65,100) (68,110) (70,150) (75,190)
"""

def get_longest(people):
    people.sort(key=lambda x: x[1])
    people.sort(key=lambda x: x[0])
    latest_known = people[0]
    total = 1
    for p in people:
        if p[0] > latest_known[0] and p[1] > latest_known[1]:
            p = latest_known
            total += 1

    return total

print get_longest([(65, 100), (65, 90), (56, 90), (75, 190), (60, 95), (68, 110)])
print get_longest([(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)])
