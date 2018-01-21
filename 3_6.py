# Write a program to sort a stack in ascending order You should not make any
# assump- tions about how the stack is implemented The following are the only
# functions that should be used to write this program: push | pop | peek |
# isEmpty

# 1 7 4 8 2 -> 1 2 4 7 8

def sort_stack(s):
    res = []
    aux = []
    while len(s) > 0:
        elem = s.pop()
        if len(res) == 0 or res[len(res)-1] < elem:
            res.append(elem)
        else:
            aux.append(elem)

        if len(s) == 0 and len(aux) > 0:
            while len(res) > 0:
                s.append(res.pop())
            while len(aux) > 0:
                s.append(aux.pop())
            

    return res

print sort_stack([1, 7, 4, 8, 2])
