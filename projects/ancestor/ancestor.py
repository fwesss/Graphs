from typing import List, Tuple
from queue import LifoQueue
from operator import itemgetter


def earliest_ancestor(ancestors: List[Tuple[int, int]], starting_node: int) -> int:
    graph = {}
    for parent, child in ancestors:
        if child not in graph:
            graph[child] = set()

        graph[child].add(parent)

    if starting_node not in graph:
        return -1

    to_visit = LifoQueue()
    visited = set()

    to_visit.put([starting_node])
    tails = []

    while not to_visit.empty():
        path = to_visit.get()
        vertex = path[-1]

        tails.append((path[-1], len(path)))

        if vertex not in visited and vertex in graph:
            visited.add(vertex)
            for neighbor in [x for x in graph[vertex]]:
                new_path = list(path) if path is not None else None
                new_path.append(neighbor)
                to_visit.put(new_path)

    return max(tails, key=itemgetter(1))[0]
