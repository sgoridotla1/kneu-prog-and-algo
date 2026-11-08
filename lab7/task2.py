"""Варіант 64. Завдання 2. Префікс обходу BFS"""
from collections import deque

from records import RECORD_TYPES, RecordN
from utils import format_ids


class Vertex:
    def __init__(self, vertex_id: int, record: RecordN):
        self.id = vertex_id
        self.record = record
        self.neighbors: list[Vertex] = []

class Graph:
    def __init__(self):
        self.vertices: dict[int, Vertex] = {}

    def add_vertex(self, vertex_id: int, record: RecordN):
        self.vertices[vertex_id] = Vertex(vertex_id, record)

    def add_edge(self, u: int, w: int):
        first, second = self.vertices[u], self.vertices[w]
        first.neighbors.append(second)
        second.neighbors.append(first)

    def bfs(self, start_id: int) -> list[Vertex]:
        start = self.vertices.get(start_id)
        if start is None:
            return []

        order: list[Vertex] = []
        visited = {start.id}
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            # print(vertex.id, [v.id for v in queue])
            for neighbor in sorted(vertex.neighbors, key=lambda v: v.id):
                if neighbor.id not in visited:
                    visited.add(neighbor.id)
                    queue.append(neighbor)
        return order

def read_graph(n: int, m: int) -> Graph:
    graph = Graph()
    for _ in range(n):
        vertex_id, kind, value = input().split()
        graph.add_vertex(int(vertex_id), RECORD_TYPES[kind](int(value)))
    for _ in range(m):
        u, w = map(int, input().split())
        graph.add_edge(u, w)
    return graph

def main():
    n, m, s = map(int, input().split())
    graph = read_graph(n, m)
    k, t = map(int, input().split())

    order = graph.bfs(s)
    prefix = order[:k]  # k=0
    selected = [vertex for vertex in prefix if vertex.record.score() >= t]

    print(f"Обхід: {format_ids([vertex.id for vertex in order])}")
    print(f"Префікс: {format_ids([vertex.id for vertex in prefix])}")
    print(f"Відібрано: {format_ids([vertex.id for vertex in selected])}")
    print(f"Кількість: {len(selected)}")
    print(f"Сума: {sum(vertex.record.score() for vertex in selected)}")


if __name__ == "__main__":
    main()
