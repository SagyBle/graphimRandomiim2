import random
from copy import deepcopy

def create_set():
    s = list()
    s.append(0)
    s.append(1)
    s.append(2)
    s.append(3)
    s.append(4)
    s.append(5)
    # print(s)
    # random.shuffle(s)

    return s


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = 8
    components = set([])

    for i in range(0, n-1):
        components.add(frozenset([i]))
    components.add(frozenset([1]).union(frozenset([2])))
    print(components)

    # get largest component size
    print(len(max(components)))






    #
    # s1 = frozenset([1])
    # s2 = frozenset([2])
    # s_unified = s1.union(s2)
    # s1_finished = False
    # s2_finished = False
    # old_components = deepcopy(components)
    #
    # for s in old_components:
    #     if s_unified.issubset(s):
    #         print("it is subset, going to break")
    #         break
    #
    #     if s.intersection(frozenset([1])) != frozenset():
    #         s1 = s
    #         components.remove(s)
    #         s1_finished = True
    #
    #     if s.intersection(frozenset([2])) != frozenset():
    #         s2 = s
    #         components.remove(s)
    #         s2_finished = True
    #
    #     if s1_finished and s2_finished:
    #         print("both finished")
    #         components.add(s1.union(s2))
    #         break
    # print(components)





    # # trying to find subset that contains 1
    # s1 = frozenset([1])
    # for ss in s:
    #     print(ss)


