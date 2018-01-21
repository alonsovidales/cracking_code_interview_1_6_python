# Given a sorted array of strings which is interspersed with empty strings,
# write a meth- od to  nd the location of a given string
# Example:  nd "ball" in ["at", "", "", "", "ball", "", "", "car", "", "",
# "dad", "", ""] will return 4 Example:  nd "ballcar" in ["at", "", "", "", "",
# "ball", "car", "", "", "dad", "", ""] will return -1

def search_str(strings, string):
    lo = 0
    hi = len(strings)-1
    while lo < hi:
        m = (hi-lo)/2 + lo

        while strings[m] == "" and m < hi:
            m += 1

        if m == hi:
            m = (hi-lo)/2 + lo
            while strings[m] == "" and m > lo:
                m -= 1

            if m == lo:
                return -1

        if strings[m] == string:
            return m

        if strings[m] > string:
            hi = m
        else:
            lo = m

print search_str(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], 'ball')
print search_str(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], 'ballcar')
