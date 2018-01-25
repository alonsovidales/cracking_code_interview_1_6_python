# Find The Longest Substring With K Unique Characters
# http://blog.gainlo.co/index.php/2016/04/12/find-the-longest-substring-with-k-unique-characters/

def search_longest_sub_str(s, k, max_substr=None):
	if max_substr is None:
		max_substr = [0]

	if len(s) < max_substr[0]:
		return max_substr[0]

	chars_in = len(set(s)) # O(n)
	if chars_in <= k and len(s) > max_substr[0]:
		max_substr[0] = len(s)
	elif chars_in < k:
		return max_substr[0]

        if len(s) > 0:
	    search_longest_sub_str(s[1:], k, max_substr)
        if len(s) > 1:
	    search_longest_sub_str(s[:len(s)-1], k, max_substr)


	return max_substr[0]


#print search_longest_sub_str('ababaacccccASDF123asdf', 4)

import collections

# Implementation using the freqs table:
def search_longest_sub_str_index(s, k, max_substr=None, freqs=None):
    if max_substr is None:
        max_substr = [0]
        freqs = collections.Counter(s)

    if len(s) < max_substr[0]:
        return max_substr[0]

    if len(freqs) <= k and len(s) > max_substr[0]:
        max_substr[0] = len(s)
    elif len(s) < max_substr[0]:
        return max_substr[0]

    if len(s) > 0:
        if freqs[s[0]] == 1:
            del freqs[s[0]]
        else:
            freqs[s[0]] -= 1
        search_longest_sub_str_index(s[1:], k, max_substr, freqs)
        if s[0] not in freqs:
            freqs[s[0]] = 1
        else:
            freqs[s[0]] += 1


    if len(s) > 1:
        l_c = s[len(s)-1]
        if freqs[l_c] == 1:
            del freqs[l_c]
        else:
            freqs[l_c] -= 1
        search_longest_sub_str_index(s[:len(s)-1], k, max_substr, freqs)
        if s[0] not in freqs:
            freqs[l_c] = 1
        else:
            freqs[l_c] += 1

    return max_substr[0]

s = 'ababaacccccASDF123asdf'

for i in xrange(10):
    print "Testing:", i
    assert(search_longest_sub_str_index(s, i) == search_longest_sub_str(s, i))
