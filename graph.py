import numpy as np
import random
from copy import deepcopy




def print_graph(graph):
    print(np.matrix(graph))

def init_undirected_grpah(number_of_vertices):
    graph = [[0] * n for _ in range(n)]
    for i in range(0, n):
        graph[i][i] = '-'
        for j in range(0, i):
            graph[j][i] = '-'
    return graph

def init_random_edges(graph: [[int]] , n: int , m: int):
    for _ in range(0, m):
        print("yes")
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        while j == i:
            j = random.randint(0, n-1)
        print(j, i)
        edge = sorted((i, j))
        print(edge)
        graph[edge[1]][edge[0]] = 1
    return graph
    # print_graph(graph)

def get_graph_components(graph, n):
    components = set([])
    for i in range(0, n):
        components.add(frozenset([i]))

    # get graph components
    for i in range(1, n):
        for j in range(0, i):
            # if edge (i, j) exists in graph
            if graph[i][j] == 1:
                s1 = frozenset([i])
                s2 = frozenset([j])
                s_unified = s1.union(s2)
                s1_finished = False
                s2_finished = False
                old_components = deepcopy(components)

                for s in old_components:
                    if s_unified.issubset(s):
                        print("it is subset, going to break")
                        break

                    if s.intersection(frozenset([i])) != frozenset():
                        s1 = s
                        components.remove(s)
                        s1_finished = True

                    if s.intersection(frozenset([j])) != frozenset():
                        s2 = s
                        components.remove(s)
                        s2_finished = True

                    if s1_finished and s2_finished:
                        components.add(s1.union(s2))
                        break

    return components




if __name__ == '__main__':
    # number of vertices
    NUMBER_OF_VERTICES = n = 5
    NUMBER_OF_EDGES = m = 5

    # init undirected graph, with no edges. implemented as matrix
    # 0 = no edge , 1 = edge, -1 = irrelevant

    graph = init_undirected_grpah(n)

    graph = init_random_edges(graph, n, m)

    print_graph(graph)

    components = get_graph_components(graph, n)

    largest_component_size = len(max(components, key=len))
    print(largest_component_size)

    print(components)
