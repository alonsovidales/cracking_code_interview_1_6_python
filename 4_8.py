# You are given a binary tree in which each node contains a value Design an
# algorithm to print all paths which sum up to that value Note that it can be
# any path in the tree - it does not have to start at the root

def get_paths(root, total, paths=None, curr_path=None):
    if paths is None:
        paths = set()
        curr_path = []

    curr_path.append(root.v)

    for i in xrange(len(curr_path)):
        for j in xrange(j, len(curr_path)):
            if sum(curr_path[i:j]) == total:
                paths.add(tuple(curr_path[i:j]))

    if root.l is not None:
        get_paths(root.l, total, paths, curr_path)
    if root.r is not None:
        get_paths(root.r, total, paths, curr_path)

    curr_path.pop()

    return paths
