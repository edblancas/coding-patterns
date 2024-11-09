# from williamfiset youtube channel
from collections import deque, defaultdict


def topological_sort_kahns(adj_list):
    inbound = [0] * 4
    print(inbound)
    for _, to in adj_list.items():
        print(to)
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


import unittest


class TopologicalSortDFS(unittest.TestCase):
    def edgelist_to_adjlist(self, edgelist):
        adjlist = defaultdict(list)
        for f, to in edgelist:
            adjlist[f].append(to)

        return adjlist

    def test_topological_sort_dfs(self):
        edgelist = [[3, 2], [3, 0], [2, 0], [2, 1]]
        # possible answers: [3,2,1,0] or [3,2,0,1]
        self.assertEqual(
            list(topological_sort_kahns(self.edgelist_to_adjlist(edgelist))),
            [3, 2, 0, 1],
        )


def main():
    test = TopologicalSortDFS()
    test.test_topological_sort_dfs()


main()
