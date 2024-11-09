# from williamfiset youtube channel
from collections import deque, defaultdict


def topological_sort_kahns(adj_list, nvertices):
    inbound = [0] * nvertices
    for _, to in adj_list.items():
        for inb in to:
            inbound[inb] += 1

    order = []
    q = deque()
    for i, inb in enumerate(inbound):
        if inb == 0:
            q.append(i)

    def decrease_inbound(vertex):
        for v in adj_list[vertex]:
            inbound[v] -= 1
            if inbound[v] == 0:
                q.append(v)

    while q:
        vertex = q.popleft()
        order.append(vertex)
        decrease_inbound(vertex)

    if len(order) < len(adj_list):
        return []

    return order


def edgelist_to_adjlist(edgelist):
    adjlist = defaultdict(list)
    for f, to in edgelist:
        adjlist[f].append(to)

    return adjlist


import unittest


class TopologicalSortDFS(unittest.TestCase):

    def test_topological_sort_dfs(self):
        edgelist = [[3, 2], [3, 0], [2, 0], [2, 1]]
        # possible answers: [3,2,1,0] or [3,2,0,1]
        self.assertEqual(
            list(topological_sort_kahns(edgelist_to_adjlist(edgelist), 4)),
            [3, 2, 0, 1],
        )


def main():
    test = TopologicalSortDFS()
    test.test_topological_sort_dfs()


main()


edgelist=[[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
print('topological', topological_sort_kahns(edgelist_to_adjlist(edgelist), 7))
