from typing import Dict, Set, Optional, List
from util import Queue, Stack

"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self) -> None:
        self._vertices: Dict[int, Set[int]] = {}

    @property
    def vertices(self) -> Dict[int, Set[int]]:
        return self._vertices

    @vertices.setter
    def vertices(self, value: Dict[int, Set[int]]) -> None:
        self._vertices = value

    def add_vertex(self, vertex_id: int) -> None:
        """
        Add a vertex to the graph.
        """
        new_vertices = self.vertices
        new_vertices[vertex_id] = set()
        self.vertices = new_vertices

    def add_edge(self, v1: int, v2: int) -> Optional[KeyError]:
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            return KeyError(f"No {v1} vertex")

        new_vertices = self.vertices
        new_vertices[v1].add(v2)
        self.vertices = new_vertices

    def get_neighbors(self, vertex_id: int) -> List[int]:
        """
        Get all neighbors (edges) of a vertex.
        """
        return [neighbor for neighbor in self.vertices[vertex_id]]

    def bft(self, starting_vertex: int) -> None:
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        to_visit = Queue()
        for neighbor in self.get_neighbors(starting_vertex):
            to_visit.enqueue(neighbor)

        print(starting_vertex)
        visited.add(starting_vertex)
        current_vertex = to_visit.dequeue()
        while current_vertex is not None:
            if current_vertex not in visited:
                print(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    to_visit.enqueue(neighbor)
                    visited.add(current_vertex)

            current_vertex = to_visit.dequeue()

    def dft(self, starting_vertex: int) -> None:
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        to_visit = Stack()
        for neighbor in self.get_neighbors(starting_vertex):
            to_visit.push(neighbor)

        print(starting_vertex)
        visited.add(starting_vertex)
        current_vertex = to_visit.pop()
        while current_vertex is not None:
            if current_vertex not in visited:
                print(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    to_visit.push(neighbor)
                    visited.add(current_vertex)

            current_vertex = to_visit.pop()

    def dft_recursive(
        self, starting_vertex: int, visited=set(), to_visit=Stack()
    ) -> None:
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                to_visit.push(neighbor)

            return self.dft_recursive(to_visit.pop(), visited, to_visit)

    def bfs(self, starting_vertex: int, destination_vertex: int) -> Optional[int]:
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        to_visit = Queue()
        visited = set()

        to_visit.enqueue([starting_vertex])

        while to_visit.size() > 0:
            path = to_visit.dequeue()
            vertex = path[-1]

            if vertex == destination_vertex:
                return path

            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    new_path = list(path) if path is not None else None
                    new_path.append(neighbor)
                    to_visit.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    print("bft")
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    print("dft")
    graph.dft(1)
    print("dft_recursive")
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print("BFS")
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print("DFS")
    print(graph.dfs(1, 6))
    print("DFS Recursive")
    print(graph.dfs_recursive(1, 6))
