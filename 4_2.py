# Given a directed graph, design an algorithm to  nd out whether there is a
# route be- tween two nodes

import collections

class DirGraph(object):
    def __init__(self):
        self._paths = collections.defaultdict(set)

    def add_path(self, f, t):
        self._paths[f].add(t)

    def is_path(self, f, to):
        visited = set()
        to_go = self._paths[f]
        while len(to_go) > 0:
            new_to_go = set()
            for t in to_go:
                if to == t:
                    return True

                visited.add(t)
                new_to_go |= self._paths[t] - visited

            to_go = new_to_go

        return False

dr = DirGraph()
dr.add_path(0, 1)
dr.add_path(1, 2)
dr.add_path(1, 0)
dr.add_path(3, 4)
dr.add_path(2, 5)

assert(dr.is_path(0, 5))
assert(dr.is_path(0, 1))
assert(not dr.is_path(5, 0))
assert(not dr.is_path(0, 4))
assert(dr.is_path(3, 4))
