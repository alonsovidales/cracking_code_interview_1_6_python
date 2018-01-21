# Given two words of equal length that are in a dictionary, write a method to
# transform onewordintoanotherwordbychangingonlyoneletteratatime Thenewwordyou
# get in each step must be in the dictionary
# EXAMPLE
# Input: DAMP, LIKE
# Output: DAMP -> LAMP -> LIMP -> LIME -> LIKE

import collections

class SuperDict(object):
    def __init__(self, words):
        self._dict = collections.defaultdict(set)
        for w in words:
            for i in xrange(len(w)):
                nw = list(w)
                nw[i] = '*'
                self._dict[''.join(nw)].add(w)

    def find_path(self, word, target, path=None, known_words=None):
        if path is None:
            known_words=set()
            path = []

        if word in known_words:
            return None

        known_words.add(word)

        for i in xrange(len(word)):
            nw = list(word)
            nw[i] = '*'
            str_nw = ''.join(nw)
            if target in self._dict[str_nw]:
                path.append(target)
                return path

            for w in self._dict[str_nw]:
                new_path = path[:]
                new_path.append(w)
                possible_path = self.find_path(w, target, new_path, known_words)
                if possible_path is not None:
                    return possible_path

        return None

sd = SuperDict(('DAMP', 'LAMP', 'LIMP', 'LIME', 'LIKE'))
print sd.find_path('DAMP', 'LIKE')
