# from williamfiset youtube channel
from collections import deque, defaultdict

def dfs(at, visited, ordering, adj_list):
    visited.add(at)

    edges = adj_list[at]
    for edge in edges:
        if edge not in visited:
            dfs(edge, visited, ordering, adj_list)
    
    ordering.appendleft(at)


def topological_sort_dfs(adj_list):
    visited = set()
    ordering = deque()
    n = len(adj_list)
    edges = list(adj_list.keys())
    for at in edges:
        if at not in visited:
            dfs(at, visited, ordering, adj_list)
    return ordering


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
        self.assertEqual(list(topological_sort_dfs(self.edgelist_to_adjlist(edgelist))), [3,2,1,0])


def main():
    test = TopologicalSortDFS()
    test.test_topological_sort_dfs()


main()