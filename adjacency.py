import random
import time
from queue import Queue


def init_edges(n: int, m: int):
    edges = list()
    for _ in range(0, m):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        while j == i or (sorted((i, j)) in edges):
            j = random.randint(0, n-1)
        edges.append(sorted((i, j)))
    print(edges)
    return edges

def init_adj_list(edges: [(int, int)], n: int):

    adj_list = dict()

    for i in range(0, n):
        adj_list[i] = []

    for edge in edges:
        u = edge[0]
        v = edge[1]
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


def run_bfs(n: int, adj_list: {int: [int]}):
    vertices = list(range(0, n))
    components = list()

    counter = 0

    is_visited = [False for i in range(0, n)]
    queue = Queue(n)

    while vertices:
        print(len(vertices))
        queue.put(vertices.pop())
        l = list()
        while not queue.empty():
            u = queue.get()
            is_visited[u] = True
            l.append(u)
            for v in adj_list[u]:
                if not is_visited[v]:
                    queue.put(v)
                    is_visited[v] = True
                    if v in vertices:
                        vertices.remove(v)

                    counter += 1
        components.append(l)
    print(components)
    print("largest component size: " + str(len(max(components, key=len))))


if __name__ == '__main__':
    n = 500000
    m = 50000
    start_time = time.time()
    edges = init_edges(n, m)
    adj_list = init_adj_list(edges, n)
    print(adj_list)
    run_bfs(n, adj_list)



    print("program end time: --- " + str((time.time() - start_time))[:7] + " seconds ---")

